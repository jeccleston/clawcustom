# ClawCustom v2.0 - Modular AI Assistant Platform

**ClawCustom** is a next-generation, modular AI assistant platform with specialized worker agents, Docker development environments, and enterprise-grade features.

[![Version](https://img.shields.io/badge/version-2.0.0-blue)](https://github.com/jeccleston/clawcustom)
![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Discord](https://img.shields.io/badge/Discord-Community-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.gg/MnCvHqpUGB)

---

## 🎉 What's New in v2.0

✨ **Complete Platform Rewrite** with:

- 🧩 **Plugin System** - Modular architecture, easy to extend
- 🤖 **Worker Agents 2.0** - 7 specialized AI workers (YAML-based)
- 🐳 **Docker Environments** - Full-stack dev sandboxes
- 👤 **Interactive Onboarding** - Guided setup wizard
- 📚 **Context-Aware Help** - Built-in assistance

---

## ✨ Core Features

### 🤖 Specialized Worker Agents

Spawn expert AI agents for specific tasks:

| Worker | Specialty | Command |
|--------|-----------|---------|
| 🤖 **Coder** | Software development | `use coder to build API` |
| 📚 **Researcher** | Information gathering | `use researcher to analyze market` |
| ✍️ **Writer** | Content creation | `use writer for documentation` |
| 📊 **Analyst** | Data analysis | `use analyst for portfolio review` |
| 🔍 **Reviewer** | Code review | `use reviewer for security audit` |
| 🏗️ **Architect** | System design | `use architect to design system` |
| 🛠️ **DevOps** | Infrastructure | `use devops for CI/CD pipeline` |

**Example:**
```bash
clawcustom agent -m "use coder to build a REST API with FastAPI"
```

### 🐳 Docker Development Environments

Instant full-stack development sandboxes:

**8 Pre-built Templates:**
- `python` - Python 3.11
- `nodejs` - Node.js 20
- `python-postgres` - Python + PostgreSQL
- `fullstack-react` - React + Node + PostgreSQL
- `fastapi` - FastAPI + PostgreSQL + Redis
- `nodejs-mongo` - Node.js + MongoDB
- `nextjs` - Next.js + PostgreSQL
- `ml-gpu` - TensorFlow + Jupyter + GPU

**Agent-Managed Workflow:**
```
User: "Build a REST API for user management"
Agent:
  1. Creates python-postgres environment
  2. Installs dependencies
  3. Implements API
  4. Writes tests
  5. Documents
  6. Shows result: http://localhost:8000
```

### 📈 Stock Market Analysis

Real-time market data and portfolio tracking:

```bash
clawcustom agent -m "What's AAPL's current price and P/E ratio?"
clawcustom agent -m "Compare NVDA, AMD, INTC performance"
clawcustom agent -m "Analyze my portfolio: 50 AAPL, 20 GOOGL"
```

### 📄 Document Processing

Work with Word and PDF files:

- **DOCX** - Create, read, edit Word documents
- **PDF** - Extract text, merge/split, get metadata
- **Tables & Images** - Handle complex elements

### 💬 Multi-Platform Chat

Connect to your favorite platforms:

- **Telegram** - Full-featured bot
- **Discord** - Server & DM support
- **WhatsApp** - QR code login
- **Slack** - Socket mode
- **Email** - IMAP/SMTP
- **Matrix** - E2EE support
- **Feishu/Lark** - WebSocket
- **DingTalk** - Stream mode
- **QQ** - Bot integration

### 🔌 LLM Provider Support

**Primary Provider: DashScope (Alibaba Cloud Qwen)** ⭐

Optimized for Alibaba Cloud DashScope with excellent Chinese/English bilingual support.

| Provider | Models | Get API Key |
|----------|--------|-------------|
| **DashScope ⭐** | Qwen (qwen3.5-plus, qwen-max, etc.) | [dashscope.console.aliyun.com](https://dashscope.console.aliyun.com) |
| OpenRouter | All models | [openrouter.ai](https://openrouter.ai) |
| Anthropic | Claude | [console.anthropic.com](https://console.anthropic.com) |
| DeepSeek | DeepSeek | [platform.deepseek.com](https://platform.deepseek.com) |
| Groq | Fast inference | [console.groq.com](https://console.groq.com) |
| vLLM | Self-hosted | Local deployment |

**💡 DashScope Coding Plan:** Use endpoint `https://coding-intl.dashscope.aliyuncs.com/v1` for optimized coding performance.

---

## 🚀 Quick Start

### 1-Click Deploy on Coolify

**Fastest way to get started (5 minutes):**

**1. In Coolify Dashboard:**
```
New Project → New Service → Docker Compose
Paste: docker-compose.coolify.yml
```

**2. Set Environment Variables:**
```bash
# Required (choose one):
OPENROUTER_API_KEY=sk-or-v1-xxx
# OR
ANTHROPIC_API_KEY=sk-ant-xxx

# Model:
AI_MODEL=anthropic/claude-opus-4-5
```

**3. Deploy** - Wait 2-3 minutes

**4. Test:**
```bash
docker exec -it <container> clawcustom agent -m "help"
```

📖 **Full Guide**: [COOLIFY_DEPLOY.md](COOLIFY_DEPLOY.md)

---

## 📦 Installation

### Option 1: From Source (Recommended)

```bash
# Clone repository
git clone https://github.com/jeccleston/clawcustom.git
cd clawcustom

# Install
pip install -e .

# Interactive onboarding (new!)
clawcustom onboard

# Start chatting
clawcustom agent
```

### Option 2: Docker

```bash
# Build image
docker build -t clawcustom .

# Initialize (interactive onboarding)
docker run -v ~/.clawcustom:/root/.clawcustom --rm clawcustom onboard

# Run gateway
docker run -v ~/.clawcustom:/root/.clawcustom -p 18790:18790 clawcustom gateway
```

### Option 3: Docker Compose

```bash
# Start services
docker compose run --rm clawcustom-cli onboard
docker compose up -d clawcustom-gateway

# View logs
docker compose logs -f clawcustom-gateway
```

### Option 4: PyPI (Coming Soon)

```bash
pip install clawcustom
clawcustom onboard
```

---

## 💡 Usage Examples

### Worker Agents

```bash
# Coder - Build features
clawcustom agent -m "use coder to create a Python module for CSV parsing"

# Researcher - Market research
clawcustom agent -m "use researcher to analyze the AI assistant market"

# Writer - Documentation
clawcustom agent -m "use writer to create API documentation"

# Analyst - Data analysis
clawcustom agent -m "use analyst to review Q4 sales data"

# Reviewer - Code review
clawcustom agent -m "use reviewer to audit authentication module"

# Architect - System design
clawcustom agent -m "use architect to design microservices architecture"

# DevOps - Infrastructure
clawcustom agent -m "use devops to create CI/CD pipeline"
```

### Docker Environments

```bash
# Create environment
clawcustom agent -m "create python environment"
clawcustom agent -m "create fullstack environment named my-app"

# List environments
clawcustom agent -m "list environments"

# Execute commands
clawcustom agent -m "exec in my-app 'npm install'"
clawcustom agent -m "exec in my-app 'python main.py'"

# Manage
clawcustom agent -m "stop environment my-app"
clawcustom agent -m "destroy environment my-app"
```

### Multi-Worker Workflow

```bash
clawcustom agent -m "
Build a complete e-commerce platform:
1. Research market requirements
2. Design system architecture
3. Set up Docker environment
4. Implement core features
5. Review code quality
6. Write documentation
"
```

### Stock Analysis

```bash
# Get stock info
clawcustom agent -m "price of AAPL"
clawcustom agent -m "AAPL financial metrics"

# Compare stocks
clawcustom agent -m "compare AAPL, GOOGL, MSFT"

# Market overview
clawcustom agent -m "market overview today"

# Portfolio
clawcustom agent -m "analyze portfolio: 50 AAPL, 20 GOOGL, 30 MSFT"
```

### Get Help

```bash
# General help
clawcustom agent -m "help"

# Topic-specific help
clawcustom agent -m "help workers"
clawcustom agent -m "help environments"
clawcustom agent -m "help commands"
clawcustom agent -m "help troubleshooting"
```

---

## ⚙️ Configuration

### Basic Config (`~/.clawcustom/config.json`)

```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-xxx"
    }
  },
  "agents": {
    "defaults": {
      "model": "anthropic/claude-opus-4-5",
      "provider": "openrouter",
      "temperature": 0.1,
      "max_tokens": 8192
    }
  },
  "plugins": {
    "enabled": ["workers", "docker", "stock"]
  },
  "tools": {
    "restrictToWorkspace": true
  }
}
```

### Environment Variables

```bash
# LLM Provider (choose one)
export CLAWCUSTOM__PROVIDERS__OPENROUTER__API_KEY=sk-or-v1-xxx
export CLAWCUSTOM__PROVIDERS__ANTHROPIC__API_KEY=sk-ant-xxx

# Model Settings
export CLAWCUSTOM__AGENTS__DEFAULTS__MODEL=anthropic/claude-opus-4-5
export CLAWCUSTOM__AGENTS__DEFAULTS__TEMPERATURE=0.1

# Chat Channels
export CLAWCUSTOM__CHANNELS__TELEGRAM__ENABLED=true
export CLAWCUSTOM__CHANNELS__TELEGRAM__TOKEN=xxx

# Resource Limits
export CLAWCUSTOM__MEMORY_LIMIT=1G
```

---

## 🏗️ Architecture

```
┌────────────────────────────────────────────────┐
│                ClawCustom v2.0                 │
├────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────┐ │
│  │          Plugin System                   │ │
│  │  Workers │ Docker │ Stock │ Custom...   │ │
│  └──────────────────────────────────────────┘ │
│                                                │
│  ┌──────────────────────────────────────────┐ │
│  │        Specialized Workers               │ │
│  │  Coder │ Researcher │ Writer │ Analyst  │ │
│  └──────────────────────────────────────────┘ │
│                                                │
│  ┌──────────────────────────────────────────┐ │
│  │     Docker Environment Manager           │ │
│  │  Templates │ Execution │ Lifecycle      │ │
│  └──────────────────────────────────────────┘ │
│                                                │
│  ┌──────────────────────────────────────────┐ │
│  │      Multi-Platform Chat Channels        │ │
│  │  Telegram │ Discord │ WhatsApp │ Slack  │ │
│  └──────────────────────────────────────────┘ │
└────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
clawcustom/
├── clawcustom/
│   ├── agent/              # Core agent system
│   │   ├── loop.py         # Agent loop
│   │   ├── worker.py       # Worker manager
│   │   └── tools/          # Agent tools
│   ├── plugins/            # NEW: Plugin system ⭐
│   │   ├── base.py         # BasePlugin class
│   │   ├── registry.py     # Plugin registry
│   │   ├── loader.py       # Dynamic loader
│   │   ├── workers/        # Worker plugins
│   │   │   ├── coder/
│   │   │   ├── researcher/
│   │   │   └── ...
│   │   └── docker/         # Docker plugin
│   │       ├── __init__.py
│   │       └── templates/
│   ├── cli/
│   │   ├── onboarding.py   # NEW: Interactive setup ⭐
│   │   └── help_system.py  # NEW: Help system ⭐
│   ├── channels/           # Chat platforms
│   ├── providers/          # LLM providers
│   └── skills/             # Skills library
├── docker-compose.yml
├── docker-compose.coolify.yml
├── pyproject.toml
└── README.md
```

⭐ = New in v2.0

---

## 🔒 Security

### Workspace Restriction

```json
{
  "tools": {
    "restrictToWorkspace": true
  }
}
```

Restricts all file operations to workspace directory.

### Channel Allowlists

```json
{
  "channels": {
    "telegram": {
      "allowFrom": ["user-id-1", "user-id-2"]
    }
  }
}
```

Empty `allowFrom` denies all access by default.

### Best Practices

- ✅ Never commit API keys
- ✅ Use environment variables in production
- ✅ Rotate keys regularly
- ✅ Use separate keys for dev/prod
- ✅ Enable workspace restriction in production

---

## 🛠️ CLI Reference

| Command | Description |
|---------|-------------|
| `clawcustom onboard` | Interactive setup wizard ⭐ |
| `clawcustom agent -m "..."` | Chat with agent |
| `clawcustom agent` | Interactive mode |
| `clawcustom gateway` | Start gateway server |
| `clawcustom status` | Show system status |
| `clawcustom channels login` | Link WhatsApp |
| `clawcustom provider login` | OAuth login |

---

## 🐛 Troubleshooting

### Container Won't Start

```bash
# Check logs
docker logs <container-id>

# Common issues:
# 1. Missing API key → Check env vars
# 2. Invalid model → Verify AI_MODEL
# 3. Port conflict → Change port
```

### Workers Not Spawning

```bash
# Verify plugins loaded
clawcustom agent -m "status"

# Check dependencies
pip install yfinance pandas
```

### Environment Creation Fails

```bash
# Check Docker
docker --version
docker-compose --version

# Verify Docker running
docker ps
```

### Memory Issues

Increase in docker-compose.yml:
```yaml
deploy:
  resources:
    limits:
      memory: 2G
```

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [COOLIFY_DEPLOY.md](COOLIFY_DEPLOY.md) | Coolify deployment guide |
| [MODULAR_SYSTEM.md](MODULAR_SYSTEM.md) | v2.0 architecture details |
| [WORKER_AGENTS.md](WORKER_AGENTS.md) | Worker system guide |
| [WORKER_EXAMPLES.md](WORKER_EXAMPLES.md) | Usage examples |
| [RENAME_SUMMARY.md](RENAME_SUMMARY.md) | Migration from nanobot |

---

## 🤝 Contributing

Contributions welcome! Priority areas:

- [ ] More worker types (QA tester, project manager)
- [ ] Additional Docker templates
- [ ] New chat channel integrations
- [ ] Web UI dashboard
- [ ] Plugin marketplace
- [ ] Enhanced monitoring

### Development Setup

```bash
git clone https://github.com/jeccleston/clawcustom.git
cd clawcustom
pip install -e ".[dev]"

# Run tests
pytest

# Lint
ruff check .
```

---

## 📈 Roadmap

### Q2 2026
- [ ] Web UI dashboard
- [ ] Worker collaboration (shared state)
- [ ] Custom worker templates
- [ ] Plugin marketplace

### Q3 2026
- [ ] Multi-modal support (images, voice)
- [ ] Long-term memory improvements
- [ ] Advanced analytics
- [ ] Mobile app

### Q4 2026
- [ ] Self-improvement from feedback
- [ ] Advanced reasoning
- [ ] Enterprise SSO
- [ ] Audit logging

---

## 🙏 Acknowledgments

ClawCustom v2.0 is a complete rewrite inspired by [nanobot](https://github.com/HKUDS/nanobot). Special thanks to the nanobot team for creating the foundation that made this possible.

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file.

---

## 💬 Community

- **Discord**: https://discord.gg/MnCvHqpUGB
- **GitHub Issues**: https://github.com/jeccleston/clawcustom/issues
- **Discussions**: https://github.com/jeccleston/clawcustom/discussions

---

## 📧 Support

1. Check documentation above
2. Search [existing issues](https://github.com/jeccleston/clawcustom/issues)
3. Open a [new issue](https://github.com/jeccleston/clawcustom/issues/new)
4. Join [Discord community](https://discord.gg/MnCvHqpUGB)

---

*ClawCustom v2.0 is for educational, research, and technical exchange purposes only. Not financial advice.*

**Built with ❤️ by [@jeccleston](https://github.com/jeccleston)**

---

## 🚀 Quick Links

- [Get Started](#-quick-start)
- [Installation](#-installation)
- [Usage Examples](#-usage-examples)
- [Configuration](#️-configuration)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
