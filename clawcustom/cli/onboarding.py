"""User-friendly onboarding system."""

import json
from pathlib import Path
from typing import Any

from loguru import logger


class OnboardingSystem:
    """
    Interactive onboarding for new users.

    Guides users through:
    - Setting their name
    - Choosing use cases
    - Selecting chat channels
    - Configuring LLM provider
    - Initial setup
    """

    ONBOARDING_QUESTIONS = [
        {
            "key": "name",
            "question": "What should I call you?",
            "type": "text",
            "validation": lambda x: len(x.strip()) > 0,
            "error": "Please enter your name",
        },
        {
            "key": "use_case",
            "question": "What would you like me to help with?",
            "type": "choice",
            "options": [
                "coding",
                "research",
                "automation",
                "data_analysis",
                "all",
            ],
            "descriptions": [
                "Coding and software development",
                "Research and information gathering",
                "Automation and workflows",
                "Data analysis and insights",
                "All of the above",
            ],
            "default": "all",
        },
        {
            "key": "chat_channel",
            "question": "How would you like to chat with me?",
            "type": "choice",
            "options": [
                "cli",
                "telegram",
                "discord",
                "whatsapp",
            ],
            "descriptions": [
                "Command line (terminal)",
                "Telegram",
                "Discord",
                "WhatsApp",
            ],
            "default": "cli",
        },
        {
            "key": "llm_provider",
            "question": "Which AI provider would you like to use?",
            "type": "choice",
            "options": [
                "openrouter",
                "anthropic",
                "openai",
                "deepseek",
                "later",
            ],
            "descriptions": [
                "OpenRouter (recommended - access to all models)",
                "Anthropic (Claude models)",
                "OpenAI (GPT models)",
                "DeepSeek (cost-effective)",
                "I'll configure later",
            ],
            "default": "openrouter",
        },
        {
            "key": "api_key",
            "question": "Enter your API key (or press Enter to skip)",
            "type": "secret",
            "optional": True,
            "show_if": {
                "llm_provider": ["openrouter", "anthropic", "openai", "deepseek"],
            },
        },
    ]

    def __init__(self, config_path: Path):
        """
        Initialize onboarding system.

        Args:
            config_path: Path to config file
        """
        self.config_path = config_path
        self.answers: dict[str, Any] = {}

    async def run(self) -> dict[str, Any]:
        """
        Run interactive onboarding.

        Returns:
            User configuration dict
        """
        print("\n🎉 Welcome to ClawCustom!")
        print("Let me help you get set up.\n")

        for question in self.ONBOARDING_QUESTIONS:
            # Check if question should be shown based on previous answers
            if not self._should_show_question(question):
                continue

            answer = await self._ask_question(question)
            if answer is not None:
                self.answers[question["key"]] = answer

        # Generate config from answers
        config = self._generate_config()

        # Save config
        self._save_config(config)

        print("\n✅ Setup complete! Here's what I configured:")
        self._show_summary(config)

        return config

    def _should_show_question(self, question: dict) -> bool:
        """Check if question should be shown based on previous answers."""
        if "show_if" not in question:
            return True

        for key, values in question["show_if"].items():
            if key not in self.answers or self.answers[key] not in values:
                return False

        return True

    async def _ask_question(self, question: dict) -> Any:
        """Ask a single question and get answer."""
        print(f"\n{question['question']}")

        if question["type"] == "choice":
            return await self._ask_choice(question)
        elif question["type"] == "secret":
            return await self._ask_secret(question)
        else:
            return await self._ask_text(question)

    async def _ask_text(self, question: dict) -> str:
        """Ask text question."""
        while True:
            try:
                answer = input("> ").strip()

                if not answer and question.get("optional"):
                    return None

                if question.get("validation") and not question["validation"](answer):
                    print(f"❌ {question.get('error', 'Invalid input')}")
                    continue

                return answer

            except (EOFError, KeyboardInterrupt):
                print("\n\nOnboarding cancelled.")
                return None

    async def _ask_secret(self, question: dict) -> str:
        """Ask for secret input (masked)."""
        import getpass

        try:
            answer = getpass.getpass("> ")

            if not answer and question.get("optional"):
                return None

            return answer

        except (EOFError, KeyboardInterrupt):
            print("\n\nOnboarding cancelled.")
            return None

    async def _ask_choice(self, question: dict) -> str:
        """Ask multiple choice question."""
        options = question["options"]
        descriptions = question.get("descriptions", options)

        for i, (opt, desc) in enumerate(zip(options, descriptions)):
            print(f"  [{i + 1}] {desc}")

        default_idx = options.index(question.get("default", options[0]))
        print(f"\n(Default: {default_idx + 1})")

        while True:
            try:
                answer = input("> ").strip()

                if not answer:
                    return question.get("default", options[0])

                try:
                    idx = int(answer) - 1
                    if 0 <= idx < len(options):
                        return options[idx]
                except ValueError:
                    # Try to match by text
                    answer_lower = answer.lower()
                    for opt in options:
                        if opt.lower().startswith(answer_lower):
                            return opt

                print(f"Please enter a number between 1 and {len(options)}")

            except (EOFError, KeyboardInterrupt):
                print("\n\nOnboarding cancelled.")
                return None

    def _generate_config(self) -> dict[str, Any]:
        """Generate configuration from answers."""
        config = {
            "user": {
                "name": self.answers.get("name", "User"),
                "use_case": self.answers.get("use_case", "all"),
                "preferred_channel": self.answers.get("chat_channel", "cli"),
            },
            "agents": {
                "defaults": {
                    "model": self._get_model_for_provider(),
                    "provider": self.answers.get("llm_provider", "openrouter"),
                },
            },
        }

        # Add API key if provided
        api_key = self.answers.get("api_key")
        if api_key:
            provider = self.answers.get("llm_provider")
            if provider and provider != "later":
                config["providers"] = {
                    provider: {
                        "apiKey": api_key,
                    },
                }

        # Add channel config if not CLI
        channel = self.answers.get("chat_channel")
        if channel and channel != "cli":
            config["channels"] = {
                channel: {
                    "enabled": True,
                },
            }

        return config

    def _get_model_for_provider(self) -> str:
        """Get recommended model for selected provider."""
        provider = self.answers.get("llm_provider", "openrouter")

        models = {
            "openrouter": "anthropic/claude-3-5-sonnet",
            "anthropic": "claude-3-5-sonnet-20241022",
            "openai": "gpt-4o",
            "deepseek": "deepseek-chat",
            "later": "anthropic/claude-3-5-sonnet",
        }

        return models.get(provider, "anthropic/claude-3-5-sonnet")

    def _save_config(self, config: dict) -> None:
        """Save configuration to file."""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

        logger.info("Saved onboarding config to {}", self.config_path)

    def _show_summary(self, config: dict) -> None:
        """Show configuration summary."""
        user = config.get("user", {})
        print(f"\n  👤 Name: {user.get('name', 'User')}")
        print(f"  🎯 Use case: {user.get('use_case', 'all')}")
        print(f"  💬 Chat channel: {user.get('preferred_channel', 'cli')}")

        agents = config.get("agents", {}).get("defaults", {})
        print(f"  🤖 Model: {agents.get('model', 'unknown')}")
        print(f"  🔑 Provider: {agents.get('provider', 'unknown')}")

        if config.get("channels"):
            channels = [k for k, v in config["channels"].items() if v.get("enabled")]
            if channels:
                print(f"  📱 Channels enabled: {', '.join(channels)}")

        print("\n📝 Configuration saved to:", self.config_path)
        print("\nYou can always change these settings later by editing the config file.\n")


async def onboard(config_path: Path | None = None) -> dict[str, Any]:
    """
    Run onboarding process.

    Args:
        config_path: Optional config path

    Returns:
        User configuration
    """
    if config_path is None:
        config_path = Path("~/.clawcustom/config.json").expanduser()

    onboarding = OnboardingSystem(config_path)
    return await onboarding.run()
