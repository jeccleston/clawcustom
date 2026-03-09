"""Comprehensive help system with contextual assistance."""

from typing import Any


class HelpSystem:
    """
    Context-aware help system for ClawCustom.

    Provides:
    - General help
    - Topic-specific help
    - Command reference
    - Examples
    - Troubleshooting
    """

    HELP_TOPICS = {
        "getting_started": {
            "title": "Getting Started",
            "aliases": ["start", "begin", "intro", "welcome"],
            "content": """
# Getting Started with ClawCustom

Welcome! Here's how to use your new AI assistant:

## Quick Commands
- `help [topic]` - Show this help or topic-specific help
- `skills` - List all available skills and workers
- `env list` - List Docker environments
- `status` - Check system status
- `config` - View/edit configuration

## Workers
Specialized AI agents for different tasks:
- `use coder to build a REST API` - Spawn coding worker
- `use researcher to find info about...` - Spawn research worker
- `use analyst to analyze data` - Spawn analysis worker

## Environments
Docker-based development sandboxes:
- `create python environment` - Create Python dev environment
- `list environments` - Show all environments
- `stop environment xyz` - Stop an environment

## Files
- `read file X` - View file contents
- `write file Y with content...` - Create/edit file
- `list directory` - Show directory contents

## Next Steps
1. Try spawning a worker: "use coder to create a hello world script"
2. Create an environment: "create python environment"
3. Ask for help on specific topics: "help workers"
            """,
        },
        "workers": {
            "title": "Worker Agents",
            "aliases": ["worker", "agents", "specialists"],
            "content": """
# Worker Agents

I have specialized AI agents for different tasks:

## Available Workers

🤖 **Coder** - Software development
   - Build features and APIs
   - Fix bugs
   - Write tests
   - Refactor code

📚 **Researcher** - Information gathering
   - Market research
   - Competitive analysis
   - Fact-finding missions
   - Literature reviews

✍️ **Writer** - Content creation
   - Documentation
   - Articles and blogs
   - Emails and communications
   - Technical writing

📊 **Analyst** - Data analysis
   - Financial analysis
   - Metrics and KPIs
   - Trend identification
   - Stock market analysis

🔍 **Reviewer** - Code review
   - Security audits
   - Quality assurance
   - Best practices check
   - Performance review

🏗️ **Architect** - System design
   - Architecture planning
   - API design
   - Database schema
   - System integration

🛠️ **DevOps** - Infrastructure
   - Docker setup
   - CI/CD pipelines
   - Deployment automation
   - Monitoring setup

## Usage Examples

```
"Spawn a coder to build a REST API with FastAPI"
"Use researcher to analyze the AI assistant market"
"Have a writer create API documentation"
"Ask analyst to review Q4 sales data"
```

## Multi-Worker Workflows

Complex tasks can use multiple workers:

1. Researcher → Gather requirements
2. Architect → Design solution
3. Coder → Implement
4. Reviewer → Quality check
5. Writer → Documentation
            """,
        },
        "environments": {
            "title": "Docker Environments",
            "aliases": ["env", "docker", "sandbox", "container"],
            "content": """
# Docker Development Environments

Create isolated development sandboxes instantly.

## Available Templates

| Template | Services | Use Case |
|----------|----------|----------|
| `python` | Python 3.11 | Python scripts, APIs |
| `nodejs` | Node.js 20 | Node.js projects |
| `python-postgres` | Python + PostgreSQL | Full Python apps |
| `fullstack-react` | React + Node + PostgreSQL | Full-stack web apps |
| `fastapi` | FastAPI + PostgreSQL + Redis | Python web APIs |
| `nodejs-mongo` | Node.js + MongoDB | NoSQL apps |
| `nextjs` | Next.js + PostgreSQL | Next.js applications |
| `ml-gpu` | TensorFlow + Jupyter + GPU | Machine learning |

## Commands

```bash
# Create environment
create environment from <template>
create python environment
create fullstack environment

# List environments
list environments
env list

# Environment info
env status <name>
env logs <name>

# Execute commands
exec in <env> "npm install"
exec in my-app "python main.py"

# Stop/destroy
stop environment <name>
destroy environment <name>
```

## Workflow

1. **Create**: "create python environment"
2. **Develop**: Agent writes code in environment
3. **Test**: "exec in env 'python test.py'"
4. **Deploy**: Agent handles deployment
5. **Cleanup**: "destroy environment" (optional)

## Benefits

- ✅ Isolated dependencies
- ✅ Reproducible setups
- ✅ Easy cleanup
- ✅ Multiple projects
- ✅ Production-like
            """,
        },
        "stock_analysis": {
            "title": "Stock Market Analysis",
            "aliases": ["stock", "stocks", "market", "investing", "trading"],
            "content": """
# Stock Market Analysis

Real-time stock data and portfolio analysis.

## Commands

```bash
# Get stock info
"price of AAPL"
"show me AAPL stock info"
"AAPL financial metrics"

# Market overview
"market overview today"
"show major indices"
"S&P 500 performance"

# Compare stocks
"compare AAPL, GOOGL, MSFT"
"NVDA vs AMD performance"

# Portfolio analysis
"analyze my portfolio: 50 AAPL, 20 GOOGL"
"portfolio performance YTD"
```

## Available Data

- **Price & Metrics**: Current price, P/E, market cap, volume
- **Financials**: Income statement, balance sheet, cash flow
- **Earnings**: Quarterly earnings, estimates
- **News**: Recent company news
- **Historical**: Price history, trends
- **Comparison**: Multi-stock performance

## Examples

```
"What's the current price and P/E ratio of Apple?"
"Compare NVIDIA and AMD stock performance"
"Show me today's market overview with major indices"
"Analyze my portfolio: 50 AAPL, 20 GOOGL, 30 MSFT"
"Get latest news for Tesla"
```

## ⚠️ Disclaimer

This is for research purposes only. Not financial advice.
Always do your own research before making investment decisions.
            """,
        },
        "commands": {
            "title": "Command Reference",
            "aliases": ["cmds", "command", "reference"],
            "content": """
# Command Reference

## General Commands

| Command | Description |
|---------|-------------|
| `help [topic]` | Show help (general or topic-specific) |
| `skills` | List available skills and workers |
| `status` | Check system status |
| `config` | View/edit configuration |
| `onboard` | Run interactive onboarding |
| `clear` | Clear screen |
| `exit` | Exit application |

## Worker Commands

| Command | Description |
|---------|-------------|
| `spawn <worker> to <task>` | Spawn specialized worker |
| `use <worker> for <task>` | Alternative spawn syntax |
| `workers list` | List all worker types |
| `worker status` | Show active workers |

## Environment Commands

| Command | Description |
|---------|-------------|
| `create env from <template>` | Create new environment |
| `env list` | List environments |
| `env status <name>` | Show environment status |
| `env logs <name>` | Show environment logs |
| `exec in <env> <cmd>` | Execute command in env |
| `stop env <name>` | Stop environment |
| `destroy env <name>` | Destroy environment |

## File Commands

| Command | Description |
|---------|-------------|
| `read <file>` | Read file contents |
| `write <file> with <content>` | Create/edit file |
| `list <directory>` | List directory contents |
| `edit <file>` | Edit file interactively |

## Stock Commands

| Command | Description |
|---------|-------------|
| `price <ticker>` | Get stock price |
| `compare <tickers>` | Compare stocks |
| `market overview` | Market indices |
| `portfolio <holdings>` | Analyze portfolio |

## Chat Commands

| Command | Description |
|---------|-------------|
| `/new` | Start new conversation |
| `/stop` | Stop current task |
| `/help` | Show help |
            """,
        },
        "troubleshooting": {
            "title": "Troubleshooting",
            "aliases": ["trouble", "issues", "problems", "errors"],
            "content": """
# Troubleshooting

## Common Issues

### "Command not found"
**Solution**: Type `help commands` to see available commands.

### Worker won't spawn
**Possible causes**:
- Worker type not recognized → `help workers` for list
- Task description unclear → Be more specific
- System busy → Wait for current task to complete

### Environment creation fails
**Check**:
1. Docker installed? → `docker --version`
2. Docker running? → `docker ps`
3. Docker Compose installed? → `docker-compose --version`

**Solution**: Install Docker Desktop from https://docker.com

### API errors
**Check**:
1. API key configured? → `config` to verify
2. API key valid? → Check provider dashboard
3. Rate limit exceeded? → Wait and retry

### Files not accessible
**Check**:
1. `restrictToWorkspace` setting
2. File path correct?
3. Permissions OK?

### High memory usage
**Solutions**:
1. Stop unused environments → `env list` then `stop env <name>`
2. Reduce concurrent workers
3. Lower `AI_MAX_TOKENS` setting

## Getting Help

1. **Check this help**: `help <topic>`
2. **View logs**: Check system logs for errors
3. **Status check**: `status` command
4. **Restart**: Sometimes helps → restart service

## Still Stuck?

- **Documentation**: See README.md, WORKER_AGENTS.md
- **GitHub Issues**: https://github.com/jeccleston/clawcustom/issues
- **Discord**: https://discord.gg/MnCvHqpUGB

## Debug Mode

Enable verbose logging:
```bash
LOG_LEVEL=debug
```

Then check logs for detailed error messages.
            """,
        },
    }

    def __init__(self):
        """Initialize help system."""
        self._index_topics()

    def _index_topics(self) -> None:
        """Build search index for help topics."""
        self._search_index: dict[str, str] = {}

        for topic_key, topic_data in self.HELP_TOPICS.items():
            # Index by topic key
            self._search_index[topic_key] = topic_key

            # Index by aliases
            for alias in topic_data.get("aliases", []):
                self._search_index[alias.lower()] = topic_key

            # Index by keywords in title
            title_words = topic_data["title"].lower().split()
            for word in title_words:
                if len(word) > 3:  # Skip short words
                    self._search_index[word] = topic_key

    def get_help(self, topic: str | None = None) -> str:
        """
        Get help content for a topic.

        Args:
            topic: Topic name or None for general help

        Returns:
            Formatted help content
        """
        if not topic:
            return self._get_general_help()

        # Normalize topic
        topic_lower = topic.lower().strip()

        # Look up topic
        topic_key = self._search_index.get(topic_lower)

        if not topic_key:
            # Fuzzy match
            topic_key = self._fuzzy_match(topic_lower)

        if not topic_key or topic_key not in self.HELP_TOPICS:
            return self._topic_not_found(topic)

        topic_data = self.HELP_TOPICS[topic_key]
        return f"# {topic_data['title']}\n{topic_data['content']}"

    def _get_general_help(self) -> str:
        """Get general help message."""
        lines = [
            "# ClawCustom Help",
            "",
            "Welcome! I'm here to help you with:",
            "",
            "## Main Features",
            "",
            "1. **Specialized Workers** - AI agents for coding, research, writing, analysis",
            "2. **Docker Environments** - Instant dev sandboxes",
            "3. **Stock Analysis** - Real-time market data",
            "4. **Document Processing** - Work with PDF and Word files",
            "5. **Multi-Platform Chat** - Telegram, Discord, WhatsApp",
            "",
            "## Quick Start",
            "",
            "```",
            "# Spawn a worker",
            "use coder to build a REST API",
            "",
            "# Create environment",
            "create python environment",
            "",
            "# Get help",
            "help workers",
            "help environments",
            "help commands",
            "```",
            "",
            "## Help Topics",
            "",
        ]

        for key, data in self.HELP_TOPICS.items():
            lines.append(f"- `{key}` - {data['title']}")

        lines.extend(
            [
                "",
                "Type `help <topic>` to learn more about a specific topic.",
                "",
            ]
        )

        return "\n".join(lines)

    def _fuzzy_match(self, query: str) -> str | None:
        """
        Fuzzy match query to topic.

        Args:
            query: Search query

        Returns:
            Best matching topic key or None
        """
        # Try substring match
        for key, indexed_key in self._search_index.items():
            if query in key or key in query:
                return indexed_key

        # Try keyword match
        query_words = set(query.split())
        for key, indexed_key in self._search_index.items():
            key_words = set(key.split())
            if query_words & key_words:  # Has common words
                return indexed_key

        return None

    def _topic_not_found(self, topic: str) -> str:
        """
        Return message when topic not found.

        Args:
            topic: Topic that wasn't found

        Returns:
            Help message with suggestions
        """
        lines = [
            f"❓ Help topic '{topic}' not found.",
            "",
            "Available topics:",
            "",
        ]

        for key, data in self.HELP_TOPICS.items():
            lines.append(f"- `{key}` - {data['title']}")

        lines.extend(
            [
                "",
                "Try one of these, or ask a question like:",
                "- 'How do I create an environment?'",
                "- 'What workers are available?'",
                "- 'Help me get started'",
                "",
            ]
        )

        return "\n".join(lines)

    def search_help(self, query: str) -> list[dict[str, str]]:
        """
        Search help topics by query.

        Args:
            query: Search query

        Returns:
            List of matching topics
        """
        results = []
        query_lower = query.lower()

        for key, data in self.HELP_TOPICS.items():
            # Search in title
            if query_lower in data["title"].lower():
                results.append(
                    {
                        "topic": key,
                        "title": data["title"],
                        "match": "title",
                    }
                )
                continue

            # Search in aliases
            for alias in data.get("aliases", []):
                if query_lower in alias.lower():
                    results.append(
                        {
                            "topic": key,
                            "title": data["title"],
                            "match": "alias",
                        }
                    )
                    break

            # Search in content
            if query_lower in data["content"].lower():
                results.append(
                    {
                        "topic": key,
                        "title": data["title"],
                        "match": "content",
                    }
                )

        return results


# Singleton instance
_help_system = HelpSystem()


def get_help(topic: str | None = None) -> str:
    """
    Get help for a topic.

    Args:
        topic: Topic name or None for general help

    Returns:
        Formatted help content
    """
    return _help_system.get_help(topic)


def search_help(query: str) -> list[dict[str, str]]:
    """
    Search help topics.

    Args:
        query: Search query

    Returns:
        List of matching topics
    """
    return _help_system.search_help(query)
