"""Base plugin system for ClawCustom."""

from abc import ABC, abstractmethod
from typing import Any

from .tools.base import Tool


class BasePlugin(ABC):
    """
    Abstract base class for all ClawCustom plugins.

    Plugins extend ClawCustom with new capabilities like:
    - Specialized agents/workers
    - New tools and capabilities
    - External service integrations
    - Custom workflows
    """

    # Plugin metadata (override in subclasses)
    name: str = "base"
    version: str = "1.0.0"
    description: str = "Base plugin"

    def __init__(self):
        """Initialize plugin."""
        self.enabled = False
        self.config = {}

    # ========== Lifecycle Hooks ==========

    async def on_load(self) -> None:
        """
        Called when plugin is loaded.

        Use for:
        - Initializing connections
        - Loading configuration
        - Setting up resources
        """
        pass

    async def on_unload(self) -> None:
        """
        Called when plugin is unloaded.

        Use for:
        - Cleaning up resources
        - Closing connections
        - Saving state
        """
        pass

    async def on_enable(self) -> None:
        """
        Called when plugin is enabled.

        Use for:
        - Activating features
        - Registering tools
        - Starting services
        """
        self.enabled = True

    async def on_disable(self) -> None:
        """
        Called when plugin is disabled.

        Use for:
        - Deactivating features
        - Unregistering tools
        - Stopping services
        """
        self.enabled = False

    # ========== Required Methods ==========

    @abstractmethod
    def get_tools(self) -> list[Tool]:
        """
        Get list of tools provided by this plugin.

        Returns:
            List of Tool instances
        """
        return []

    @abstractmethod
    def get_skills(self) -> list[str]:
        """
        Get list of skill files provided by this plugin.

        Returns:
            List of skill names (directory names containing SKILL.md)
        """
        return []

    @abstractmethod
    def get_config_schema(self) -> dict[str, Any]:
        """
        Get configuration schema for this plugin.

        Returns:
            JSON schema dict for plugin configuration
        """
        return {
            "type": "object",
            "properties": {},
        }

    # ========== Helper Methods ==========

    def configure(self, config: dict[str, Any]) -> None:
        """
        Configure plugin with provided settings.

        Args:
            config: Configuration dictionary
        """
        self.config = config

    def get_tool_names(self) -> list[str]:
        """Get names of all tools provided by this plugin."""
        return [tool.name for tool in self.get_tools()]

    def has_tool(self, name: str) -> bool:
        """Check if plugin provides a specific tool."""
        return any(tool.name == name for tool in self.get_tools())

    def get_tool(self, name: str) -> Tool | None:
        """Get a specific tool by name."""
        for tool in self.get_tools():
            if tool.name == name:
                return tool
        return None

    # ========== Metadata ==========

    def get_info(self) -> dict[str, Any]:
        """Get plugin information."""
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "enabled": self.enabled,
            "tools": self.get_tool_names(),
            "skills": self.get_skills(),
        }

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name}, version={self.version}, enabled={self.enabled})"
