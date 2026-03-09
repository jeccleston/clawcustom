"""Docker plugin - Environment management for agents."""

import asyncio
import hashlib
import json
import shutil
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from loguru import logger

from nanobot.agent.tools.base import Tool
from nanobot.plugins.base import BasePlugin


@dataclass
class Environment:
    """Represents a Docker environment."""

    id: str
    name: str
    template: str
    path: Path
    created_at: datetime = field(default_factory=datetime.now)
    status: str = "created"  # created, running, stopped, error
    services: list[str] = field(default_factory=list)
    ports: dict[str, int] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "template": self.template,
            "path": str(self.path),
            "created_at": self.created_at.isoformat(),
            "status": self.status,
            "services": self.services,
            "ports": self.ports,
            "metadata": self.metadata,
        }


class DockerManager:
    """Manages Docker environments for agents."""

    def __init__(self, base_path: Path):
        """
        Initialize Docker manager.

        Args:
            base_path: Base directory for environments
        """
        self.base_path = base_path / "environments"
        self.base_path.mkdir(parents=True, exist_ok=True)
        self._environments: dict[str, Environment] = {}

    async def create_environment(
        self, template: str, name: str | None = None, config: dict[str, Any] | None = None
    ) -> Environment:
        """
        Create a new Docker environment from template.

        Args:
            template: Template name to use
            name: Optional environment name
            config: Optional configuration overrides

        Returns:
            Created Environment instance
        """
        # Generate name if not provided
        if not name:
            name = f"env-{hashlib.md5(str(datetime.now()).encode()).hexdigest()[:8]}"

        # Create environment directory
        env_path = self.base_path / name
        env_path.mkdir(parents=True, exist_ok=True)

        # Copy template
        templates_dir = Path(__file__).parent / "templates"
        template_file = templates_dir / f"{template}.yml"

        if not template_file.exists():
            raise ValueError(f"Template {template} not found")

        # Read and apply template
        with open(template_file, encoding="utf-8") as f:
            compose_data = yaml.safe_load(f)

        # Apply config overrides if provided
        if config:
            compose_data = self._apply_config_overrides(compose_data, config)

        # Write docker-compose.yml
        compose_file = env_path / "docker-compose.yml"
        with open(compose_file, "w", encoding="utf-8") as f:
            yaml.dump(compose_data, f)

        # Create environment record
        env_id = f"{name}-{hashlib.md5(str(env_path).encode()).hexdigest()[:8]}"
        env = Environment(
            id=env_id,
            name=name,
            template=template,
            path=env_path,
            services=list(compose_data.get("services", {}).keys()),
        )

        self._environments[env_id] = env

        # Start environment
        await self._start_environment(env)

        logger.info("Created environment {} from template {}", env_id, template)
        return env

    def _apply_config_overrides(self, compose_data: dict, config: dict[str, Any]) -> dict:
        """Apply configuration overrides to compose data."""
        # TODO: Implement config override logic
        return compose_data

    async def _start_environment(self, env: Environment) -> None:
        """
        Start Docker environment.

        Args:
            env: Environment to start
        """
        try:
            # Run docker-compose up -d
            process = await asyncio.create_subprocess_exec(
                "docker-compose",
                "up",
                "-d",
                cwd=str(env.path),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, stderr = await process.communicate(timeout=120)

            if process.returncode != 0:
                env.status = "error"
                logger.error("Failed to start environment {}: {}", env.id, stderr.decode())
                raise RuntimeError(f"Failed to start environment: {stderr.decode()}")

            env.status = "running"

            # Get assigned ports
            await self._update_env_ports(env)

            logger.info("Started environment {}", env.id)

        except FileNotFoundError:
            env.status = "error"
            logger.error("Docker Compose not found")
            raise
        except Exception as e:
            env.status = "error"
            logger.error("Failed to start environment {}: {}", env.id, e)
            raise

    async def _update_env_ports(self, env: Environment) -> None:
        """Update environment with actual assigned ports."""
        try:
            process = await asyncio.create_subprocess_exec(
                "docker-compose",
                "port",
                "--all",
                cwd=str(env.path),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, _ = await process.communicate(timeout=30)

            if process.returncode == 0:
                # Parse port mappings
                ports = {}
                for line in stdout.decode().strip().split("\n"):
                    if ":" in line:
                        service_port, host_port = line.split(":")
                        ports[service_port] = int(host_port)
                env.ports = ports

        except Exception as e:
            logger.debug("Failed to get ports for {}: {}", env.id, e)

    async def execute_in_environment(
        self, environment_id: str, command: str, service: str = "app", timeout: int = 60
    ) -> str:
        """
        Execute command in running environment.

        Args:
            environment_id: Environment ID
            command: Command to execute
            service: Service name to execute in
            timeout: Command timeout in seconds

        Returns:
            Command output
        """
        env = self._environments.get(environment_id)
        if not env:
            raise ValueError(f"Environment {environment_id} not found")

        if env.status != "running":
            raise ValueError(f"Environment {environment_id} is not running")

        try:
            process = await asyncio.create_subprocess_exec(
                "docker-compose",
                "exec",
                "-T",
                service,
                "sh",
                "-c",
                command,
                cwd=str(env.path),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, stderr = await process.communicate(timeout=timeout)

            result = stdout.decode()
            if stderr and process.returncode != 0:
                result += f"\nError: {stderr.decode()}"

            return result

        except asyncio.TimeoutError:
            return f"Command timed out after {timeout} seconds"
        except Exception as e:
            return f"Failed to execute command: {str(e)}"

    async def get_logs(
        self, environment_id: str, service: str | None = None, tail: int = 100
    ) -> str:
        """
        Get logs from environment.

        Args:
            environment_id: Environment ID
            service: Optional service name (None = all services)
            tail: Number of lines to retrieve

        Returns:
            Log output
        """
        env = self._environments.get(environment_id)
        if not env:
            raise ValueError(f"Environment {environment_id} not found")

        try:
            cmd = ["docker-compose", "logs", f"--tail={tail}"]
            if service:
                cmd.append(service)

            process = await asyncio.create_subprocess_exec(
                *cmd,
                cwd=str(env.path),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, _ = await process.communicate(timeout=30)
            return stdout.decode()

        except Exception as e:
            return f"Failed to get logs: {str(e)}"

    async def stop_environment(self, environment_id: str) -> None:
        """
        Stop environment.

        Args:
            environment_id: Environment ID
        """
        env = self._environments.get(environment_id)
        if not env:
            raise ValueError(f"Environment {environment_id} not found")

        try:
            process = await asyncio.create_subprocess_exec(
                "docker-compose",
                "stop",
                cwd=str(env.path),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            await process.communicate(timeout=60)
            env.status = "stopped"

            logger.info("Stopped environment {}", environment_id)

        except Exception as e:
            logger.error("Failed to stop environment {}: {}", environment_id, e)
            raise

    async def destroy_environment(self, environment_id: str) -> None:
        """
        Completely destroy environment.

        Args:
            environment_id: Environment ID
        """
        env = self._environments.get(environment_id)
        if not env:
            return

        try:
            # Stop and remove containers
            process = await asyncio.create_subprocess_exec(
                "docker-compose",
                "down",
                "-v",
                cwd=str(env.path),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            await process.communicate(timeout=120)

            # Remove directory
            if env.path.exists():
                shutil.rmtree(env.path)

            # Remove from registry
            del self._environments[environment_id]

            logger.info("Destroyed environment {}", environment_id)

        except Exception as e:
            logger.error("Failed to destroy environment {}: {}", environment_id, e)
            raise

    def list_environments(self) -> list[dict]:
        """
        List all environments.

        Returns:
            List of environment info dicts
        """
        return [env.to_dict() for env in self._environments.values()]

    def get_environment(self, environment_id: str) -> Environment | None:
        """
        Get environment by ID.

        Args:
            environment_id: Environment ID

        Returns:
            Environment instance or None
        """
        return self._environments.get(environment_id)

    def get_environment_status(self, environment_id: str) -> dict | None:
        """
        Get environment status.

        Args:
            environment_id: Environment ID

        Returns:
            Status dict or None
        """
        env = self._environments.get(environment_id)
        if not env:
            return None
        return env.to_dict()


class DockerPlugin(BasePlugin):
    """Plugin for Docker environment management."""

    name = "docker"
    version = "1.0.0"
    description = "Docker environment management for full-stack development"

    def __init__(self):
        """Initialize Docker plugin."""
        super().__init__()
        self._manager: DockerManager | None = None
        self._tools: list[Tool] = []

    async def on_load(self) -> None:
        """Initialize Docker manager."""
        from nanobot.config import Config

        # Get workspace from config or use default
        workspace = Path("~/.nanobot/workspace").expanduser()

        self._manager = DockerManager(workspace)
        logger.info("Docker plugin loaded")

    def get_tools(self) -> list[Tool]:
        """Get tools provided by this plugin."""
        # TODO: Implement Docker tools
        return self._tools

    def get_skills(self) -> list[str]:
        """Get skills provided by this plugin."""
        return ["fullstack-coding"]

    def get_config_schema(self) -> dict[str, Any]:
        """Get configuration schema."""
        return {
            "type": "object",
            "properties": {
                "auto_cleanup": {
                    "type": "boolean",
                    "description": "Automatically cleanup environments after 24 hours",
                    "default": False,
                },
                "max_environments": {
                    "type": "integer",
                    "description": "Maximum number of concurrent environments",
                    "default": 5,
                    "minimum": 1,
                    "maximum": 20,
                },
                "default_template": {
                    "type": "string",
                    "description": "Default template to use",
                    "default": "python",
                },
            },
        }

    def get_manager(self) -> DockerManager | None:
        """Get Docker manager instance."""
        return self._manager
