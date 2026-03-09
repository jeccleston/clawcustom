# ClawCustom: Enterprise AI Assistant Platform

**ClawCustom** is a powerful, customizable AI assistant platform built on nanobot with enterprise-grade features including specialized worker agents, stock analysis, document processing, and Docker sandbox environments.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)
[![Discord](https://img.shields.io/badge/Discord-Community-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.gg/MnCvHqpUGB)

---

## ✨ Features

### 🤖 Specialized Worker Agents

Spawn expert AI agents for specific task domains:

| Worker | Specialty | Use Case |
|--------|-----------|----------|
| **Coder** | Software development | Build features, fix bugs, write tests |
| **Researcher** | Information gathering | Market research, competitive analysis |
| **Writer** | Content creation | Documentation, articles, emails |
| **Analyst** | Data analysis | Financial analysis, metrics, insights |
| **Reviewer** | Code review | QA, security audit, best practices |
| **Architect** | System design | Architecture, APIs, databases |
| **DevOps** | Infrastructure | Docker, CI/CD, deployment |

**Example:**
```bash
nanobot agent -m "Spawn a coder worker to build a REST API for user management"
```

### 📈 Stock Market Analysis

Real-time stock market data and analysis tools:

- **Stock Analysis** - Price, financials, earnings, news for any ticker
- **Market Overview** - Major indices (S&P 500, Dow, NASDAQ)
- **Compare Stocks** - Compare multiple stocks by performance
- **Portfolio Tracking** - Analyze holdings and performance

**Example:**
```python
stock_analysis(symbol="AAPL", data_type="all")
market_overview(indices=True, movers=True)
compare_stocks(symbols="AAPL,GOOGL,MSFT", period="1mo")
```

### 📄 Document Processing

Work with Word and PDF documents:

- **DOCX Skill** - Create, read, edit Microsoft Word documents
- **PDF Skill** - Extract text, merge/split PDFs, get metadata
- **Tables & Images** - Handle complex document elements

**Example:**
```python
# Extract text from PDF
from pypdf import PdfReader
reader = PdfReader("document.pdf")
text = reader.pages[0].extract_text()

# Create Word document
from docx import Document
doc = Document()
doc.add_paragraph("Hello World")
doc.save("output.docx")
```

### 🛠️ Full-Stack Development Sandboxes

Docker-based isolated development environments:

- **Pre-built Templates** - Node.js, Python, Fullstack, Databases
- **One-Click Setup** - Spin up dev environments in seconds
- **Database Support** - PostgreSQL, MySQL, MongoDB, Redis
- **Auto Cleanup** - Destroy environments when done

**Available Templates:**
- `nodejs.yml` - Node.js 20 container
- `python.yml` - Python 3.11 container
- `fullstack.yml` - React + Node.js + PostgreSQL
- `nodejs-mysql.yml` - Node.js + MySQL
- `nodejs-mongo.yml` - Node.js + MongoDB
- `python-postgres.yml` - Python + PostgreSQL
- `redis.yml` - Redis cache

**Example:**
```bash
# Create development environment
cp templates/nodejs.yml docker-compose.yml
docker-compose up -d
docker-compose exec app npm install
```

### 💬 Multi-Platform Chat

Connect to your favorite chat platforms:

- **Telegram** - Bot integration with full feature support
- **Discord** - Server and DM support
- **WhatsApp** - QR code login, full messaging
- **Slack** - Socket mode, threads, reactions
- **Email** - IMAP/SMTP integration
- **Matrix** - E2EE support
- **Feishu/Lark** - WebSocket long connection
- **DingTalk** - Stream mode
- **QQ** - Bot integration

### 🔌 LLM Provider Support

Wide range of LLM providers:

| Provider | Models | Region |
|----------|--------|--------|
| **OpenRouter** | All major models | Global |
| **Anthropic** | Claude series | Global |
| **DashScope** | Qwen series | China/Global |
| **DeepSeek** | DeepSeek series | Global |
| **Groq** | Fast inference | Global |
| **vLLM** | Self-hosted | Local |
| **Azure OpenAI** | GPT series | Global |

### 🔧 MCP Support

Model Context Protocol integration for extended capabilities:

- **Filesystem MCP** - Enhanced file operations
- **Custom MCP Servers** - Connect any MCP-compatible server
- **HTTP & Stdio** - Multiple transport modes

### ⏰ Scheduled Tasks

Cron-based task automation:

```bash
# Schedule recurring tasks
nanobot agent -m "Every morning at 9am, check weather and stock market summary"
```

### 💓 Heartbeat System

Proactive periodic tasks:

- Runs every 30 minutes
- Checks `HEARTBEAT.md` for tasks
- Delivers results to active chat channel

---

## 🚀 Quick Start

### 1-Click Deploy on Coolify (Recommended)

The fastest way to get started:

**1. In Coolify Dashboard:**
```
New Project → New Service → Docker Compose
```

**2. Use docker-compose.coolify.yml**

**3. Set Environment Variables:**
```bash
# Required (choose one provider):
OPENROUTER_API_KEY=sk-or-v1-xxx
# OR
ANTHROPIC_API_KEY=sk-ant-xxx

# Model:
AI_MODEL=anthropic/claude-opus-4-5
```

**4. Deploy** - Wait 2-3 minutes

**5. Test:**
```bash
docker exec -it <container> nanobot agent -m "Hello!"
```

📖 **Full Coolify Guide**: See [COOLIFY_DEPLOY.md](COOLIFY_DEPLOY.md)

---

## 📦 Installation

### Option 1: Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/jeccleston/clawcustom.git
cd clawcustom

# Build image
docker build -t clawcustom .

# Initialize config
docker run -v ~/.clawcustom:/root/.nanobot --rm clawcustom onboard

# Edit config
vim ~/.clawcustom/config.json

# Run gateway
docker run -v ~/.clawcustom:/root/.nanobot -p 18790:18790 clawcustom gateway
```

### Option 2: Docker Compose

```bash
# Start with docker-compose
docker compose run --rm nanobot-cli onboard
vim ~/.nanobot/config.json
docker compose up -d nanobot-gateway

# View logs
docker compose logs -f nanobot-gateway
```

### Option 3: From Source (Development)

```bash
# Clone and install
git clone https://github.com/jeccleston/clawcustom.git
cd clawcustom
pip install -e .

# Install optional dependencies
pip install nanobot-ai[matrix]  # For Matrix support
pip install yfinance pandas     # For stock analysis

# Initialize
nanobot onboard

# Configure
vim ~/.nanobot/config.json

# Run
nanobot gateway
```

### Option 4: From PyPI

```bash
pip install nanobot-ai
nanobot onboard
vim ~/.nanobot/config.json
nanobot agent
```

---

## ⚙️ Configuration

### Basic Config (`~/.nanobot/config.json`)

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
  "tools": {
    "restrictToWorkspace": true
  }
}
```

### Environment Variables (Coolify/Docker)

```bash
# LLM Provider
OPENROUTER_API_KEY=sk-or-v1-xxx
ANTHROPIC_API_KEY=sk-ant-xxx
DASHSCOPE_API_KEY=xxx

# Model Settings
AI_MODEL=anthropic/claude-opus-4-5
AI_PROVIDER=auto
AI_TEMPERATURE=0.1
AI_MAX_TOKENS=8192

# Optional: Web Search
BRAVE_SEARCH_API_KEY=xxx

# Optional: Chat Channels
TELEGRAM_ENABLED=true
TELEGRAM_BOT_TOKEN=xxx
DISCORD_ENABLED=false

# Resource Limits
CPU_LIMIT=1
MEMORY_LIMIT=1G
RESTRICT_TO_WORKSPACE=true
```

### Enable Chat Channels

#### Telegram

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "YOUR_BOT_TOKEN",
      "allowFrom": ["YOUR_USER_ID"]
    }
  }
}
```

Get bot token: @BotFather on Telegram → `/newbot`

#### WhatsApp

```bash
# In container
docker exec -it <container> nanobot channels login

# Scan QR with WhatsApp → Settings → Linked Devices
```

#### Discord

1. Create app at https://discord.com/developers
2. Enable **MESSAGE CONTENT INTENT**
3. Copy bot token
4. Add to config

---

## 💡 Usage Examples

### Worker Agents

```bash
# Spawn a coder worker
nanobot agent -m "Spawn a coder to build a REST API with FastAPI"

# Spawn a researcher
nanobot agent -m "Spawn a researcher to analyze the AI assistant market"

# Spawn a writer
nanobot agent -m "Spawn a writer to create API documentation"

# Multi-worker workflow
nanobot agent -m "
1. Spawn researcher to study OAuth2 best practices
2. Spawn architect to design OAuth2 flow
3. Spawn coder to implement
4. Spawn reviewer for security audit
5. Spawn writer for documentation
"
```

### Stock Analysis

```bash
# Get stock info
nanobot agent -m "What's the current price and P/E ratio of AAPL?"

# Compare stocks
nanobot agent -m "Compare NVDA, AMD, and INTC performance over the last 3 months"

# Market overview
nanobot agent -m "Show me today's market overview with major indices"

# Portfolio analysis
nanobot agent -m "Analyze my portfolio: 50 AAPL, 20 GOOGL, 30 MSFT"
```

### Document Processing

```bash
# Extract PDF text
nanobot agent -m "Extract all text from report.pdf and summarize it"

# Create Word doc
nanobot agent -m "Create a Word document with meeting notes including a table"

# Merge PDFs
nanobot agent -m "Merge file1.pdf, file2.pdf, and file3.pdf into combined.pdf"
```

### Development Sandboxes

```bash
# Create Node.js environment
cd ~/projects/my-app
cp ~/clawcustom/nanobot/skills/fullstack-coding/templates/nodejs.yml docker-compose.yml
docker-compose up -d
docker-compose exec app npm init -y

# Create fullstack environment
mkdir ~/projects/fullstack-app
cd ~/projects/fullstack-app
cp ~/clawcustom/nanobot/skills/fullstack-coding/templates/fullstack.yml docker-compose.yml
docker-compose up -d
# Now you have frontend, backend, and PostgreSQL running!
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                   ClawCustom                        │
├─────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────┐   │
│  │            Specialized Workers              │   │
│  │  Coder │ Researcher │ Writer │ Analyst │... │   │
│  └─────────────────────────────────────────────┘   │
│                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │  Stock   │  │ Document │  │  Full-Stack      │  │
│  │ Analysis │  │  Tools   │  │  Sandboxes       │  │
│  └──────────┘  └──────────┘  └──────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │        Multi-Platform Chat Channels          │  │
│  │ Telegram │ Discord │ WhatsApp │ Slack │...   │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │          LLM Provider Gateway                │  │
│  │ OpenRouter │ Anthropic │ DashScope │ vLLM   │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
clawcustom/
├── nanobot/
│   ├── agent/
│   │   ├── loop.py           # Core agent loop
│   │   ├── worker.py         # Worker agent system ⭐
│   │   ├── subagent.py       # Background tasks
│   │   └── tools/
│   │       ├── stock.py      # Stock analysis tools ⭐
│   │       ├── spawn_worker.py # Worker spawning ⭐
│   │       └── ...
│   ├── skills/
│   │   ├── worker/           # Worker skill ⭐
│   │   ├── stock-insight/    # Stock research ⭐
│   │   ├── docx/             # Word documents ⭐
│   │   ├── pdf/              # PDF processing ⭐
│   │   └── fullstack-coding/ # Docker sandboxes ⭐
│   └── ...
├── docker-compose.coolify.yml
├── COOLIFY_DEPLOY.md
├── WORKER_AGENTS.md
└── README.md
```

⭐ = Custom ClawCustom additions

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

When enabled, all file operations are restricted to the workspace directory.

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

Empty `allowFrom` denies all access by default (new behavior).

### API Key Security

- Never commit API keys
- Use environment variables in production
- Rotate keys regularly
- Use separate keys for dev/prod

---

## 📊 Monitoring & Logs

### Check Status

```bash
nanobot status
```

### View Logs

```bash
# Docker
docker compose logs -f nanobot-gateway

# Systemd
journalctl --user -u nanobot-gateway -f

# Direct
tail -f ~/.nanobot/logs/*.log
```

### Health Check

```bash
docker exec -it <container> nanobot status
```

---

## 🔄 Updates

### Docker

```bash
docker compose pull
docker compose up -d
```

### From Source

```bash
git pull
pip install -e .
nanobot gateway  # Auto-restarts
```

### Coolify

Click **Redeploy** in Coolify dashboard or enable **Auto Deploy**.

---

## 🛠️ CLI Reference

| Command | Description |
|---------|-------------|
| `nanobot onboard` | Initialize config & workspace |
| `nanobot agent -m "..."` | Chat with agent |
| `nanobot agent` | Interactive mode |
| `nanobot gateway` | Start gateway server |
| `nanobot status` | Show system status |
| `nanobot channels login` | Link WhatsApp |
| `nanobot channels status` | Channel status |
| `nanobot provider login` | OAuth login (Codex, Copilot) |

---

## 🐛 Troubleshooting

### Container Won't Start

```bash
# Check logs
docker logs <container-id>

# Common issues:
# 1. Missing API key - Check env vars
# 2. Invalid model - Verify AI_MODEL
# 3. Port conflict - Change GATEWAY_PORT
```

### Workers Not Spawning

```bash
# Verify worker skill is loaded
nanobot agent -m "List available skills"

# Check yfinance for stock tools
pip install yfinance pandas
```

### Can't Access Chat Channels

1. Verify tokens in config/env
2. Check bot permissions
3. Review logs for auth errors
4. Ensure `enabled: true` in config

### Memory Issues

Increase resource limits in Coolify/docker-compose:

```yaml
deploy:
  resources:
    limits:
      memory: 2G  # Increase from 1G
```

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [COOLIFY_DEPLOY.md](COOLIFY_DEPLOY.md) | Complete Coolify deployment guide |
| [WORKER_AGENTS.md](WORKER_AGENTS.md) | Worker agent system guide |
| [WORKER_EXAMPLES.md](WORKER_EXAMPLES.md) | Real-world worker examples |
| [WORKER_IMPLEMENTATION.md](WORKER_IMPLEMENTATION.md) | Technical implementation details |

---

## 🤝 Contributing

Contributions welcome! Areas of interest:

- [ ] More worker types (QA tester, project manager, etc.)
- [ ] Additional stock analysis features
- [ ] More document processing tools
- [ ] Additional Docker sandbox templates
- [ ] New chat channel integrations
- [ ] UI/dashboard for monitoring

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
- [ ] Enhanced monitoring

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

ClawCustom is built on top of [nanobot](https://github.com/HKUDS/nanobot), an ultra-lightweight AI assistant framework. Special thanks to the nanobot team for creating the foundation.

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

For questions or issues:

1. Check documentation above
2. Search existing issues
3. Open a new issue on GitHub
4. Join Discord community

---

*ClawCustom is for educational, research, and technical exchange purposes only. Not financial advice.*

**Built with ❤️ by [@jeccleston](https://github.com/jeccleston)**
