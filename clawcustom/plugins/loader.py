"""Dynamic plugin loader for ClawCustom."""

import importlib
from pathlib import Path
from typing import Any

from loguru import logger

from .base import BasePlugin
from .registry import PluginRegistry


class PluginLoader:
    """
    Dynamically loads and manages plugins.

    Discovers plugins in the plugins directory,
    loads them, and registers with the registry.
    """

    def __init__(self, registry: PluginRegistry):
        """
        Initialize plugin loader.

        Args:
            registry: Plugin registry to register plugins with
        """
        self.registry = registry
        self.plugins_dir = Path(__file__).parent
        self._loaded_modules: dict[str, Any] = {}

    async def load_all(self, enabled_plugins: list[str] | None = None) -> int:
        """
        Load all plugins from the plugins directory.

        Args:
            enabled_plugins: List of plugin names to enable (None = all)

        Returns:
            Number of plugins loaded
        """
        loaded_count = 0

        # Discover plugin directories
        for plugin_dir in self.plugins_dir.iterdir():
            if not plugin_dir.is_dir():
                continue

            # Skip special directories
            if plugin_dir.name.startswith("_") or plugin_dir.name == "__pycache__":
                continue

            # Check if plugin has __init__.py (indicates it's a plugin)
            init_file = plugin_dir / "__init__.py"
            if not init_file.exists():
                continue

            # Load the plugin
            try:
                await self.load_plugin(plugin_dir.name)
                loaded_count += 1
            except Exception as e:
                logger.error("Failed to load plugin {}: {}", plugin_dir.name, e)

        # Enable specified plugins
        if enabled_plugins:
            for plugin_name in enabled_plugins:
                if self.registry.has(plugin_name):
                    await self.registry.enable(plugin_name)
                else:
                    logger.warning("Plugin {} not found, cannot enable", plugin_name)
        else:
            # Enable all by default
            await self.registry.enable_all()

        logger.info("Loaded {} plugins", loaded_count)
        return loaded_count

    async def load_plugin(self, name: str) -> BasePlugin:
        """
        Load a single plugin by name.

        Args:
            name: Plugin name (directory name)

        Returns:
            Loaded plugin instance
        """
        # Check if already loaded
        if self.registry.has(name):
            logger.debug("Plugin {} already loaded", name)
            return self.registry.get(name)

        # Import plugin module
        try:
            module = importlib.import_module(f"clawcustom.plugins.{name}")
        except ImportError as e:
            raise ImportError(f"Failed to import plugin {name}: {e}")

        # Find plugin class (convention: PluginName = name.title() + "Plugin")
        plugin_class_name = f"{name.title().replace('_', '')}Plugin"
        plugin_class = getattr(module, plugin_class_name, None)

        if not plugin_class:
            # Try to find any class that inherits from BasePlugin
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, BasePlugin) and attr != BasePlugin:
                    plugin_class = attr
                    break

        if not plugin_class:
            raise ImportError(
                f"Plugin {name} has no class named {plugin_class_name} or subclass of BasePlugin"
            )

        # Instantiate plugin
        try:
            plugin = plugin_class()
        except Exception as e:
            raise ImportError(f"Failed to instantiate plugin {name}: {e}")

        # Call lifecycle hook
        try:
            await plugin.on_load()
        except Exception as e:
            logger.error("Plugin {} on_load failed: {}", name, e)
            raise

        # Register plugin
        self.registry.register(plugin)
        self._loaded_modules[name] = module

        logger.info("Loaded plugin: {} v{}", plugin.name, plugin.version)
        return plugin

    async def unload_plugin(self, name: str) -> None:
        """
        Unload a plugin by name.

        Args:
            name: Plugin name to unload
        """
        if not self.registry.has(name):
            logger.warning("Plugin {} not loaded, cannot unload", name)
            return

        # Unregister from registry (calls on_unload)
        await self.registry.unregister(name)

        # Remove from loaded modules
        if name in self._loaded_modules:
            del self._loaded_modules[name]

        logger.info("Unloaded plugin: {}", name)

    async def reload_plugin(self, name: str) -> BasePlugin:
        """
        Reload a plugin.

        Args:
            name: Plugin name to reload

        Returns:
            Reloaded plugin instance
        """
        # Unload
        await self.unload_plugin(name)

        # Clear module cache
        if f"clawcustom.plugins.{name}" in importlib.sys.modules:
            del importlib.sys.modules[f"clawcustom.plugins.{name}"]

        # Load again
        return await self.load_plugin(name)

    def discover_plugins(self) -> list[dict[str, str]]:
        """
        Discover available plugins without loading them.

        Returns:
            List of plugin info dicts (name, version, description)
        """
        plugins = []

        for plugin_dir in self.plugins_dir.iterdir():
            if not plugin_dir.is_dir() or plugin_dir.name.startswith("_"):
                continue

            init_file = plugin_dir / "__init__.py"
            if not init_file.exists():
                continue

            # Try to extract metadata without importing
            try:
                info = self._extract_plugin_info(plugin_dir)
                if info:
                    plugins.append(info)
            except Exception as e:
                logger.debug("Failed to extract info from {}: {}", plugin_dir.name, e)

        return plugins

    def _extract_plugin_info(self, plugin_dir: Path) -> dict[str, str] | None:
        """
        Extract plugin metadata from __init__.py without importing.

        Args:
            plugin_dir: Plugin directory path

        Returns:
            Dict with name, version, description or None
        """
        init_file = plugin_dir / "__init__.py"
        if not init_file.exists():
            return None

        content = init_file.read_text(encoding="utf-8")

        # Extract metadata using simple string matching
        info = {"name": plugin_dir.name}

        # Look for name = "..."
        if 'name = "' in content:
            start = content.find('name = "') + len('name = "')
            end = content.find('"', start)
            if end > start:
                info["name"] = content[start:end]

        # Look for version = "..."
        if 'version = "' in content:
            start = content.find('version = "') + len('version = "')
            end = content.find('"', start)
            if end > start:
                info["version"] = content[start:end]
            else:
                info["version"] = "unknown"
        else:
            info["version"] = "unknown"

        # Look for description = "..."
        if 'description = "' in content:
            start = content.find('description = "') + len('description = "')
            end = content.find('"', start)
            if end > start:
                info["description"] = content[start:end]
            else:
                info["description"] = "No description"
        else:
            info["description"] = "No description"

        return info

    def get_status(self) -> dict:
        """
        Get loader status.

        Returns:
            Dict with loader statistics
        """
        return {
            "plugins_dir": str(self.plugins_dir),
            "loaded_plugins": list(self._loaded_modules.keys()),
            "registry_status": self.registry.get_status(),
        }
