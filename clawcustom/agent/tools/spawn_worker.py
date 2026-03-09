"""Spawn worker tool for creating specialized task agents."""

from typing import Any

from .worker import WorkerAgentManager, WorkerType


class SpawnWorkerTool:
    """Tool to spawn a specialized worker agent for task execution."""

    def __init__(self, manager: WorkerAgentManager):
        self._manager = manager

    @property
    def name(self) -> str:
        return "spawn_worker"

    @property
    def description(self) -> str:
        return "Spawn a specialized worker agent optimized for specific task types (coder, researcher, writer, analyst, reviewer, architect, devops). Use when you need focused expertise."

    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "task": {
                    "type": "string",
                    "description": "The specific task for the worker to complete. Be detailed and include expected output.",
                },
                "worker_type": {
                    "type": "string",
                    "enum": [
                        "coder",
                        "researcher",
                        "writer",
                        "analyst",
                        "reviewer",
                        "architect",
                        "devops",
                    ],
                    "description": "Type of specialized worker: coder (software dev), researcher (info gathering), writer (content creation), analyst (data analysis), reviewer (code review), architect (system design), devops (infrastructure)",
                },
                "label": {
                    "type": "string",
                    "description": "Short descriptive label for tracking progress (e.g., 'Auth Module', 'Market Research')",
                },
            },
            "required": ["task", "worker_type"],
        }

    async def execute(self, **kwargs: Any) -> str:
        task = kwargs.get("task", "")
        worker_type = kwargs.get("worker_type", "coder")
        label = kwargs.get("label")

        if not task:
            return "Error: Task description is required"

        return await self._manager.spawn(
            task=task,
            worker_type=worker_type,
            label=label,
        )
