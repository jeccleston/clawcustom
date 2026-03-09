"""Plugin registry for managing loaded plugins."""

from pathlib import Path
from typing import Any

from loguru import logger

from nanobot.plugins.base import BasePlugin


class PluginRegistry:
    """
    Central registry for all loaded plugins.

    Manages plugin lifecycle, tool registration, and skill discovery.
    """

    def __init__(self):
        """Initialize plugin registry."""
        self._plugins: dict[str, BasePlugin] = {}

    # ========== Registration ==========

    def register(self, plugin: BasePlugin) -> None:
        """
        Register a plugin.

        Args:
            plugin: Plugin instance to register
        """
        if plugin.name in self._plugins:
            logger.warning("Plugin {} already registered, skipping", plugin.name)
            return

        self._plugins[plugin.name] = plugin
        logger.info("Registered plugin: {} v{}", plugin.name, plugin.version)

    async def unregister(self, name: str) -> None:
        """
        Unregister a plugin by name.

        Args:
            name: Plugin name to unregister
        """
        if name not in self._plugins:
            logger.warning("Plugin {} not found, cannot unregister", name)
            return

        plugin = self._plugins[name]
        await plugin.on_unload()
        del self._plugins[name]
        logger.info("Unregistered plugin: {}", name)

    # ========== Access ==========

    def get(self, name: str) -> BasePlugin | None:
        """
        Get a plugin by name.

        Args:
            name: Plugin name

        Returns:
            Plugin instance or None
        """
        return self._plugins.get(name)

    def has(self, name: str) -> bool:
        """
        Check if a plugin is registered.

        Args:
            name: Plugin name

        Returns:
            True if plugin is registered
        """
        return name in self._plugins

    def list_plugins(self) -> list[dict[str, Any]]:
        """
        List all registered plugins with their info.

        Returns:
            List of plugin info dicts
        """
        return [plugin.get_info() for plugin in self._plugins.values()]

    def get_enabled_plugins(self) -> list[BasePlugin]:
        """
        Get all enabled plugins.

        Returns:
            List of enabled plugin instances
        """
        return [p for p in self._plugins.values() if p.enabled]

    # ========== Tools ==========

    def get_all_tools(self) -> list[Any]:
        """
        Get all tools from all enabled plugins.

        Returns:
            List of all Tool instances
        """
        tools = []
        for plugin in self.get_enabled_plugins():
            tools.extend(plugin.get_tools())
        return tools

    def get_tool_names(self) -> list[str]:
        """
        Get names of all tools from all enabled plugins.

        Returns:
            List of tool names
        """
        names = []
        for plugin in self.get_enabled_plugins():
            names.extend(plugin.get_tool_names())
        return names

    def get_tool(self, name: str) -> Any | None:
        """
        Get a tool by name from any enabled plugin.

        Args:
            name: Tool name

        Returns:
            Tool instance or None
        """
        for plugin in self.get_enabled_plugins():
            tool = plugin.get_tool(name)
            if tool:
                return tool
        return None

    # ========== Skills ==========

    def get_all_skills(self) -> list[str]:
        """
        Get all skill names from all enabled plugins.

        Returns:
            List of skill directory names
        """
        skills = []
        for plugin in self.get_enabled_plugins():
            skills.extend(plugin.get_skills())
        return skills

    def get_skill_path(self, skill_name: str) -> Path | None:
        """
        Get path to a skill's SKILL.md file.

        Args:
            skill_name: Name of skill directory

        Returns:
            Path to SKILL.md or None
        """
        # Search in plugin directories
        plugins_dir = Path(__file__).parent
        for plugin_dir in plugins_dir.iterdir():
            if not plugin_dir.is_dir():
                continue

            # Check plugin's skills
            skill_path = plugin_dir / skill_name / "SKILL.md"
            if skill_path.exists():
                return skill_path

        return None

    # ========== Lifecycle ==========

    async def enable(self, name: str) -> bool:
        """
        Enable a plugin.

        Args:
            name: Plugin name

        Returns:
            True if successful
        """
        plugin = self.get(name)
        if not plugin:
            logger.error("Cannot enable plugin {}: not found", name)
            return False

        await plugin.on_enable()
        logger.info("Enabled plugin: {}", name)
        return True

    async def disable(self, name: str) -> bool:
        """
        Disable a plugin.

        Args:
            name: Plugin name

        Returns:
            True if successful
        """
        plugin = self.get(name)
        if not plugin:
            logger.error("Cannot disable plugin {}: not found", name)
            return False

        await plugin.on_disable()
        logger.info("Disabled plugin: {}", name)
        return True

    async def enable_all(self) -> None:
        """Enable all registered plugins."""
        for plugin in self._plugins.values():
            await plugin.on_enable()
        logger.info("Enabled all {} plugins", len(self._plugins))

    async def disable_all(self) -> None:
        """Disable all registered plugins."""
        for plugin in self._plugins.values():
            await plugin.on_disable()
        logger.info("Disabled all plugins")

    # ========== Status ==========

    def get_status(self) -> dict[str, Any]:
        """
        Get registry status.

        Returns:
            Dict with registry statistics
        """
        enabled_plugins = self.get_enabled_plugins()
        return {
            "total_plugins": len(self._plugins),
            "enabled_plugins": len(enabled_plugins),
            "disabled_plugins": len(self._plugins) - len(enabled_plugins),
            "total_tools": len(self.get_tool_names()),
            "total_skills": len(self.get_all_skills()),
            "plugins": self.list_plugins(),
        }

    def __len__(self) -> int:
        """Get number of registered plugins."""
        return len(self._plugins)

    def __contains__(self, name: str) -> bool:
        """Check if plugin is registered."""
        return name in self._plugins

    def __iter__(self):
        """Iterate over registered plugins."""
        return iter(self._plugins.values())
