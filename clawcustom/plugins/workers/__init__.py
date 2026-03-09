"""Worker plugin - Specialized AI agents for different tasks."""

import asyncio
from pathlib import Path
from typing import Any

import yaml
from loguru import logger

from .tools.base import Tool
from .tools.spawn_worker import SpawnWorkerTool
from .worker import WorkerAgentManager, WorkerConfig, WorkerType
from .base import BasePlugin


class WorkerPlugin(BasePlugin):
    """
    Plugin for specialized worker agents.

    Provides:
    - Worker agent spawning
    - YAML-based worker configuration
    - Dynamic worker discovery
    """

    name = "workers"
    version = "2.0.0"
    description = "Specialized worker agents for coding, research, writing, analysis, and more"

    def __init__(self):
        """Initialize worker plugin."""
        super().__init__()
        self.worker_configs: dict[str, WorkerConfig] = {}
        self._manager: WorkerAgentManager | None = None
        self._tools: list[Tool] = []

    async def on_load(self) -> None:
        """Load worker configurations."""
        # Discover and load worker YAML files
        workers_dir = Path(__file__).parent / "workers"
        if workers_dir.exists():
            await self._discover_workers(workers_dir)

        logger.info("Worker plugin loaded with {} worker types", len(self.worker_configs))

    async def _discover_workers(self, workers_dir: Path) -> None:
        """
        Discover workers from YAML files.

        Args:
            workers_dir: Directory containing worker definitions
        """
        for worker_dir in workers_dir.iterdir():
            if not worker_dir.is_dir():
                continue

            yaml_file = worker_dir / "worker.yaml"
            if not yaml_file.exists():
                # Check if it's an enum-based worker (legacy)
                if worker_dir.name.upper() in [wt.value.upper() for wt in WorkerType]:
                    continue
                continue

            try:
                config = await self._load_worker_yaml(yaml_file)
                self.worker_configs[config.worker_type.value] = config
                logger.debug("Loaded worker config: {}", config.worker_type.value)
            except Exception as e:
                logger.error("Failed to load worker {}: {}", worker_dir.name, e)

    async def _load_worker_yaml(self, yaml_file: Path) -> WorkerConfig:
        """
        Load worker configuration from YAML file.

        Args:
            yaml_file: Path to worker.yaml

        Returns:
            WorkerConfig instance
        """
        with open(yaml_file, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        # Convert to WorkerConfig
        worker_type = WorkerType(data.get("type", data.get("name", "coder")))

        return WorkerConfig(
            worker_type=worker_type,
            system_prompt=data.get("system_prompt", ""),
            tools=data.get("tools", []),
            max_iterations=data.get("parameters", {}).get("max_iterations", 25),
            temperature=data.get("parameters", {}).get("temperature", 0.1),
            max_tokens=data.get("parameters", {}).get("max_tokens", 6144),
            description=data.get("description", ""),
        )

    def set_manager(self, manager: WorkerAgentManager) -> None:
        """
        Set the worker agent manager.

        Args:
            manager: WorkerAgentManager instance
        """
        self._manager = manager

    def get_tools(self) -> list[Tool]:
        """Get tools provided by this plugin."""
        if self._manager:
            return [SpawnWorkerTool(self._manager)]
        return []

    def get_skills(self) -> list[str]:
        """Get skills provided by this plugin."""
        return ["worker"]

    def get_config_schema(self) -> dict[str, Any]:
        """Get configuration schema."""
        return {
            "type": "object",
            "properties": {
                "default_worker": {
                    "type": "string",
                    "description": "Default worker type to use",
                    "enum": [wt.value for wt in WorkerType],
                    "default": "coder",
                },
                "max_concurrent_workers": {
                    "type": "integer",
                    "description": "Maximum concurrent workers",
                    "default": 5,
                    "minimum": 1,
                    "maximum": 20,
                },
                "auto_cleanup": {
                    "type": "boolean",
                    "description": "Automatically cleanup workers after completion",
                    "default": False,
                },
            },
        }

    def get_worker_types(self) -> list[dict[str, str]]:
        """
        Get list of available worker types.

        Returns:
            List of worker type info dicts
        """
        types = []

        # Add YAML-defined workers
        for config in self.worker_configs.values():
            types.append(
                {
                    "type": config.worker_type.value,
                    "description": config.description,
                    "source": "yaml",
                }
            )

        # Add enum-based workers (legacy)
        for worker_type in WorkerType:
            if worker_type.value not in self.worker_configs:
                types.append(
                    {
                        "type": worker_type.value,
                        "description": f"Built-in {worker_type.value} worker",
                        "source": "builtin",
                    }
                )

        return types

    def list_workers(self) -> str:
        """
        Get formatted list of available workers.

        Returns:
            Formatted string with worker info
        """
        lines = ["Available Workers:", ""]

        for worker_info in self.get_worker_types():
            lines.append(f"  • {worker_info['type']}: {worker_info['description']}")

        return "\n".join(lines)
