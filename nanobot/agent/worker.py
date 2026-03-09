"""Worker agent system for specialized task execution."""

import asyncio
import json
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Awaitable, Callable

from loguru import logger

from nanobot.agent.tools.filesystem import EditFileTool, ListDirTool, ReadFileTool, WriteFileTool
from nanobot.agent.tools.registry import ToolRegistry
from nanobot.agent.tools.shell import ExecTool
from nanobot.agent.tools.web import WebFetchTool, WebSearchTool
from nanobot.bus.events import InboundMessage, OutboundMessage
from nanobot.bus.queue import MessageBus
from nanobot.config.schema import ExecToolConfig
from nanobot.providers.base import LLMProvider


class WorkerType(str, Enum):
    """Specialized worker types."""

    CODER = "coder"
    RESEARCHER = "researcher"
    WRITER = "writer"
    ANALYST = "analyst"
    REVIEWER = "reviewer"
    ARCHITECT = "architect"
    DEVOPS = "devops"


@dataclass
class WorkerConfig:
    """Configuration for a worker type."""

    worker_type: WorkerType
    system_prompt: str
    tools: list[str]
    max_iterations: int
    temperature: float
    max_tokens: int
    description: str


WORKER_CONFIGS: dict[WorkerType, WorkerConfig] = {
    WorkerType.CODER: WorkerConfig(
        worker_type=WorkerType.CODER,
        system_prompt="""You are an expert software engineer specializing in clean, production-ready code.

Your responsibilities:
- Write well-structured, tested, and maintainable code
- Follow existing code conventions and project structure
- Include proper error handling and logging
- Add clear comments for complex logic
- Prefer simplicity and readability over cleverness
- Consider security implications
- Write tests when appropriate

Always explain your approach before implementing. After coding, verify the solution works.""",
        tools=[
            "read_file",
            "write_file",
            "edit_file",
            "list_dir",
            "exec",
            "web_search",
            "web_fetch",
        ],
        max_iterations=30,
        temperature=0.1,
        max_tokens=8192,
        description="Software development, debugging, refactoring, testing",
    ),
    WorkerType.RESEARCHER: WorkerConfig(
        worker_type=WorkerType.RESEARCHER,
        system_prompt="""You are an expert researcher specializing in gathering comprehensive, verified information.

Your responsibilities:
- Search multiple sources for thorough coverage
- Cross-reference information for accuracy
- Distinguish between facts, opinions, and speculation
- Organize findings logically with clear structure
- Cite all sources clearly
- Summarize key insights concisely
- Highlight contradictions or gaps in information

Always provide a summary of findings with key takeaways. Include links to sources.""",
        tools=["web_search", "web_fetch", "read_file", "write_file"],
        max_iterations=25,
        temperature=0.2,
        max_tokens=6144,
        description="Information gathering, market research, competitive analysis",
    ),
    WorkerType.WRITER: WorkerConfig(
        worker_type=WorkerType.WRITER,
        system_prompt="""You are an expert writer specializing in clear, engaging content.

Your responsibilities:
- Write for the target audience with appropriate tone
- Use clear, concise language
- Structure content logically with proper formatting
- Ensure grammar and spelling accuracy
- Make content engaging and informative
- Follow any style guides or templates provided
- Include examples where helpful

Focus on clarity and readability. Break up long paragraphs. Use headings and lists appropriately.""",
        tools=["read_file", "write_file", "edit_file", "web_fetch"],
        max_iterations=20,
        temperature=0.3,
        max_tokens=6144,
        description="Documentation, articles, emails, content creation",
    ),
    WorkerType.ANALYST: WorkerConfig(
        worker_type=WorkerType.ANALYST,
        system_prompt="""You are an expert data analyst specializing in extracting insights from data.

Your responsibilities:
- Analyze data systematically and objectively
- Identify trends, patterns, and anomalies
- Quantify findings with specific metrics
- Create clear summaries and visualizations where helpful
- Highlight risks and opportunities
- Draw data-driven conclusions
- Explain methodology clearly

Always start by understanding the data structure. Present findings with supporting evidence.""",
        tools=[
            "read_file",
            "write_file",
            "exec",
            "web_search",
            "stock_analysis",
            "market_overview",
            "compare_stocks",
        ],
        max_iterations=25,
        temperature=0.1,
        max_tokens=6144,
        description="Data analysis, financial modeling, metrics, insights",
    ),
    WorkerType.REVIEWER: WorkerConfig(
        worker_type=WorkerType.REVIEWER,
        system_prompt="""You are an expert code reviewer specializing in quality, security, and best practices.

Your responsibilities:
- Identify bugs, vulnerabilities, and code smells
- Check adherence to coding standards
- Evaluate test coverage and quality
- Suggest specific improvements
- Flag security concerns immediately
- Consider performance implications
- Verify error handling is adequate

Be constructive but thorough. Prioritize issues by severity. Provide actionable recommendations.""",
        tools=["read_file", "list_dir", "exec", "web_search"],
        max_iterations=20,
        temperature=0.1,
        max_tokens=6144,
        description="Code review, security audit, quality assurance",
    ),
    WorkerType.ARCHITECT: WorkerConfig(
        worker_type=WorkerType.ARCHITECT,
        system_prompt="""You are an expert system architect specializing in scalable, maintainable designs.

Your responsibilities:
- Design for scalability and maintainability
- Define clear component boundaries and interfaces
- Consider trade-offs explicitly
- Follow established architectural patterns
- Document decisions and rationale
- Plan for failure scenarios
- Consider security from the start

Always start by understanding requirements and constraints. Present multiple options when appropriate.""",
        tools=["read_file", "write_file", "web_search", "web_fetch"],
        max_iterations=25,
        temperature=0.2,
        max_tokens=8192,
        description="System design, API design, database schema, architecture",
    ),
    WorkerType.DEVOPS: WorkerConfig(
        worker_type=WorkerType.DEVOPS,
        system_prompt="""You are an expert DevOps engineer specializing in infrastructure and automation.

Your responsibilities:
- Implement infrastructure as code
- Create automated CI/CD pipelines
- Follow security best practices
- Set up monitoring and alerting
- Plan for disaster recovery
- Optimize for reliability and performance
- Document deployment procedures

Always consider security, scalability, and maintainability. Prefer proven tools and patterns.""",
        tools=["read_file", "write_file", "exec", "web_search"],
        max_iterations=25,
        temperature=0.1,
        max_tokens=6144,
        description="Infrastructure, CI/CD, deployment, monitoring, Docker, Kubernetes",
    ),
}


class WorkerAgentManager:
    """Manages specialized worker agents for task-specific execution."""

    def __init__(
        self,
        provider: LLMProvider,
        workspace: Path,
        bus: MessageBus,
        model: str | None = None,
        exec_config: ExecToolConfig | None = None,
        restrict_to_workspace: bool = False,
    ):
        self.provider = provider
        self.workspace = workspace
        self.bus = bus
        self.model = model or provider.get_default_model()
        self.exec_config = exec_config or ExecToolConfig()
        self.restrict_to_workspace = restrict_to_workspace
        self._running_workers: dict[str, asyncio.Task] = {}

    async def spawn(
        self,
        task: str,
        worker_type: WorkerType | str,
        label: str | None = None,
        origin_channel: str = "cli",
        origin_chat_id: str = "direct",
    ) -> str:
        """Spawn a specialized worker agent."""
        if isinstance(worker_type, str):
            try:
                worker_type = WorkerType(worker_type.lower())
            except ValueError:
                return f"Error: Unknown worker type '{worker_type}'. Valid types: {', '.join(w.value for w in WorkerType)}"

        config = WORKER_CONFIGS[worker_type]
        task_id = f"worker-{worker_type.value}-{label or task[:20]}".replace(" ", "-").lower()
        display_label = label or task[:40] + ("..." if len(task) > 40 else "")

        logger.info("Spawning {} worker: {}", worker_type.value, display_label)

        bg_task = asyncio.create_task(
            self._run_worker(task_id, task, display_label, config, origin_channel, origin_chat_id)
        )
        self._running_workers[task_id] = bg_task

        def _cleanup(_: asyncio.Task) -> None:
            self._running_workers.pop(task_id, None)

        bg_task.add_done_callback(_cleanup)

        return f"Worker [{worker_type.value}] spawned: {display_label}. I'll notify you when it completes."

    async def _run_worker(
        self,
        task_id: str,
        task: str,
        label: str,
        config: WorkerConfig,
        origin_channel: str,
        origin_chat_id: str,
    ) -> None:
        """Execute the worker task with specialized configuration."""
        try:
            tools = self._build_worker_tools(config)
            messages = [
                {"role": "system", "content": config.system_prompt},
                {"role": "user", "content": task},
            ]

            final_result: str | None = None
            iteration = 0

            while iteration < config.max_iterations:
                iteration += 1

                response = await self.provider.chat(
                    messages=messages,
                    tools=tools.get_definitions(),
                    model=self.model,
                    temperature=config.temperature,
                    max_tokens=config.max_tokens,
                )

                if response.has_tool_calls:
                    tool_call_dicts = [
                        {
                            "id": tc.id,
                            "type": "function",
                            "function": {
                                "name": tc.name,
                                "arguments": json.dumps(tc.arguments, ensure_ascii=False),
                            },
                        }
                        for tc in response.tool_calls
                    ]
                    messages.append(
                        {
                            "role": "assistant",
                            "content": response.content or "",
                            "tool_calls": tool_call_dicts,
                        }
                    )

                    for tool_call in response.tool_calls:
                        args_str = json.dumps(tool_call.arguments, ensure_ascii=False)
                        logger.debug(
                            "Worker [{}] executing: {} with arguments: {}",
                            task_id,
                            tool_call.name,
                            args_str[:200],
                        )
                        result = await tools.execute(tool_call.name, tool_call.arguments)
                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "name": tool_call.name,
                                "content": result,
                            }
                        )
                else:
                    final_result = response.content
                    break

            if final_result is None:
                final_result = "Task completed but no final response was generated."

            logger.info("Worker [{}] completed successfully", task_id)
            await self._announce_result(
                task_id, label, task, final_result, origin_channel, origin_chat_id, "ok"
            )

        except Exception as e:
            error_msg = f"Error: {str(e)}"
            logger.error("Worker [{}] failed: {}", task_id, e)
            await self._announce_result(
                task_id, label, task, error_msg, origin_channel, origin_chat_id, "error"
            )

    def _build_worker_tools(self, config: WorkerConfig) -> ToolRegistry:
        """Build tool registry with only the tools needed for this worker type."""
        tools = ToolRegistry()
        allowed_dir = self.workspace if self.restrict_to_workspace else None

        tool_map = {
            "read_file": ReadFileTool(workspace=self.workspace, allowed_dir=allowed_dir),
            "write_file": WriteFileTool(workspace=self.workspace, allowed_dir=allowed_dir),
            "edit_file": EditFileTool(workspace=self.workspace, allowed_dir=allowed_dir),
            "list_dir": ListDirTool(workspace=self.workspace, allowed_dir=allowed_dir),
            "exec": ExecTool(
                working_dir=str(self.workspace),
                timeout=self.exec_config.timeout,
                restrict_to_workspace=self.restrict_to_workspace,
                path_append=self.exec_config.path_append,
            ),
            "web_search": WebSearchTool(api_key=None, proxy=None),
            "web_fetch": WebFetchTool(proxy=None),
            "stock_analysis": None,
            "market_overview": None,
            "compare_stocks": None,
        }

        for tool_name in config.tools:
            if tool_name in ("stock_analysis", "market_overview", "compare_stocks"):
                try:
                    from nanobot.agent.tools.stock import (
                        StockAnalysisTool,
                        MarketOverviewTool,
                        CompareStocksTool,
                    )

                    stock_tools = {
                        "stock_analysis": StockAnalysisTool(),
                        "market_overview": MarketOverviewTool(),
                        "compare_stocks": CompareStocksTool(),
                    }
                    if tool := stock_tools.get(tool_name):
                        tools.register(tool)
                        logger.debug("Registered stock tool: {}", tool_name)
                except ImportError:
                    logger.debug("Stock tools not available, skipping {}", tool_name)
            elif tool := tool_map.get(tool_name):
                tools.register(tool)
                logger.debug("Registered tool: {}", tool_name)

        return tools

    async def _announce_result(
        self,
        task_id: str,
        label: str,
        task: str,
        result: str,
        origin_channel: str,
        origin_chat_id: str,
        status: str,
    ) -> None:
        """Announce the worker result to the main agent."""
        status_text = "completed successfully" if status == "ok" else "failed"
        worker_type = task_id.split("-")[1] if "-" in task_id else "worker"

        announce_content = f"""[Specialized Worker '{label}' ({worker_type}) {status_text}]

Task: {task}

Result:
{result}

Summarize this naturally for the user. Keep it brief and focus on the outcome."""

        msg = InboundMessage(
            channel="system",
            sender_id="worker",
            chat_id=f"{origin_channel}:{origin_chat_id}",
            content=announce_content,
        )

        await self.bus.publish_inbound(msg)
        logger.debug(
            "Worker [{}] announced result to {}:{}", task_id, origin_channel, origin_chat_id
        )

    def get_running_count(self) -> int:
        """Return the number of currently running workers."""
        return len(self._running_workers)

    def list_worker_types(self) -> list[dict[str, str]]:
        """List available worker types with descriptions."""
        return [
            {
                "type": config.worker_type.value,
                "description": config.description,
                "tools": ", ".join(config.tools),
                "max_iterations": str(config.max_iterations),
            }
            for config in WORKER_CONFIGS.values()
        ]
