# nanobot: Ultra-Lightweight Personal AI Assistant

**nanobot** is an ultra-lightweight personal AI assistant inspired by [OpenClaw](https://github.com/openclaw/openclaw).

- **~4,000 lines** of core agent code — 99% smaller than alternatives
- **Research-ready** — Clean, readable code easy to understand and extend
- **Lightning fast** — Minimal footprint, faster startup, lower resource usage
- **Easy to deploy** — One-click deployment on Coolify, Docker, or bare metal

[![PyPI](https://img.shields.io/pypi/v/nanobot-ai)](https://pypi.org/project/nanobot-ai/)
[![Downloads](https://static.pepy.tech/badge/nanobot-ai)](https://pepy.tech/project/nanobot-ai)
![Python](https://img.shields.io/badge/python-≥3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)
[![Discord](https://img.shields.io/badge/Discord-Community-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.gg/MnCvHqpUGB)

---

## Table of Contents

- [Quick Start](#quick-start)
- [Installation](#installation)
- [Deployment](#deployment)
  - [Docker](#docker)
  - [Coolify](#coolify-deployment)
  - [Linux Service](#linux-service)
- [Chat Channels](#chat-channels)
- [Configuration](#configuration)
- [CLI Reference](#cli-reference)
- [Project Structure](#project-structure)

---

## Quick Start

**1. Install**

```bash
pip install nanobot-ai
```

**2. Initialize**

```bash
nanobot onboard
```

**3. Configure** (`~/.nanobot/config.json`)

```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-xxx"
    }
  },
  "agents": {
    "defaults": {
      "model": "anthropic/claude-opus-4-5"
    }
  }
}
```

**4. Chat**

```bash
nanobot agent -m "Hello!"
```

---

## Installation

### From Source (Recommended for Development)

```bash
git clone https://github.com/HKUDS/nanobot.git
cd nanobot
pip install -e .
```

### With uv (Fast)

```bash
uv tool install nanobot-ai
```

### From PyPI

```bash
pip install nanobot-ai
```

---

## Deployment

### Docker

**Docker Compose**

```bash
docker compose run --rm nanobot-cli onboard
vim ~/.nanobot/config.json
docker compose up -d nanobot-gateway
```

**Docker**

```bash
docker build -t nanobot .
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot onboard
docker run -v ~/.nanobot:/root/.nanobot -p 18790:18790 nanobot gateway
```

### Coolify Deployment

Deploy on [Coolify](https://coolify.io) - self-hosted Vercel/Netlify alternative.

**1. In Coolify Dashboard:**
- Create new project → Add new service → Select "Docker Compose"
- Use `docker-compose.coolify.yml`

**2. Set Environment Variables:**

```bash
OPENROUTER_API_KEY=sk-or-v1-xxx
AI_MODEL=anthropic/claude-opus-4-5
```

**3. Deploy:**
- Click "Deploy" and wait (~2-3 min)

📖 **Full guide**: See [`COOLIFY_DEPLOY.md`](COOLIFY_DEPLOY.md)

### Linux Service

**1. Create service file** (`~/.config/systemd/user/nanobot-gateway.service`):

```ini
[Unit]
Description=Nanobot Gateway
After=network.target

[Service]
Type=simple
ExecStart=%h/.local/bin/nanobot gateway
Restart=always

[Install]
WantedBy=default.target
```

**2. Enable and start:**

```bash
systemctl --user daemon-reload
systemctl --user enable --now nanobot-gateway
loginctl enable-linger $USER
```

---

## Chat Channels

Connect nanobot to your favorite chat platform.

| Channel | What You Need |
|---------|---------------|
| **Telegram** | Bot token from @BotFather |
| **Discord** | Bot token + Message Content intent |
| **WhatsApp** | QR code scan |
| **Feishu** | App ID + App Secret |
| **Slack** | Bot token + App-Level token |
| **Email** | IMAP/SMTP credentials |
| **Matrix** | Access token + User ID |

### Telegram (Recommended)

**1. Create bot:** Open Telegram → @BotFather → `/newbot`

**2. Configure:**

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

**3. Run:**

```bash
nanobot gateway
```

### WhatsApp

```bash
nanobot channels login
# Scan QR with WhatsApp → Settings → Linked Devices
```

### Discord

1. Create app at https://discord.com/developers
2. Enable **MESSAGE CONTENT INTENT**
3. Get bot token and configure in `config.json`
4. Invite bot to your server

See details for other channels in the full documentation.

---

## Configuration

### Providers

| Provider | Models | Get API Key |
|----------|--------|-------------|
| `openrouter` | All models | [openrouter.ai](https://openrouter.ai) |
| `anthropic` | Claude | [console.anthropic.com](https://console.anthropic.com) |
| `dashscope` | Qwen | [dashscope.console.aliyun.com](https://dashscope.console.aliyun.com) |
| `deepseek` | DeepSeek | [platform.deepseek.com](https://platform.deepseek.com) |
| `groq` | Fast inference | [console.groq.com](https://console.groq.com) |
| `vllm` | Local models | — |

**Example:**

```json
{
  "providers": {
    "anthropic": {
      "apiKey": "sk-ant-xxx"
    }
  },
  "agents": {
    "defaults": {
      "model": "anthropic/claude-3-5-sonnet"
    }
  }
}
```

### MCP (Model Context Protocol)

```json
{
  "tools": {
    "mcpServers": {
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
      }
    }
  }
}
```

### Security

```json
{
  "tools": {
    "restrictToWorkspace": true
  },
  "channels": {
    "telegram": {
      "allowFrom": ["your-user-id"]
    }
  }
}
```

---

## CLI Reference

| Command | Description |
|---------|-------------|
| `nanobot onboard` | Initialize config & workspace |
| `nanobot agent -m "..."` | Chat with the agent |
| `nanobot gateway` | Start the gateway |
| `nanobot status` | Show status |
| `nanobot channels login` | Link WhatsApp (scan QR) |

---

## Project Structure

```
nanobot/
├── agent/          # Core agent logic
│   ├── loop.py     # Agent loop (LLM ↔ tool execution)
│   ├── context.py  # Prompt builder
│   ├── memory.py   # Persistent memory
│   ├── skills.py   # Skills loader
│   ├── subagent.py # Background task execution
│   └── tools/      # Built-in tools
├── skills/         # Bundled skills
├── channels/       # Chat channel integrations
├── bus/            # Message routing
├── cron/           # Scheduled tasks
├── providers/      # LLM providers
├── session/        # Conversation sessions
├── config/         # Configuration
└── cli/            # Commands
```

---

## Contributing

PRs welcome! The codebase is intentionally small and readable.

**Roadmap:**
- [ ] Multi-modal support (images, voice, video)
- [ ] Long-term memory improvements
- [ ] Better reasoning and planning
- [ ] More integrations (Calendar, etc.)
- [ ] Self-improvement from feedback

---

## Contributors

<a href="https://github.com/HKUDS/nanobot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/nanobot&max=100&columns=12" alt="Contributors" />
</a>

---

## Support

- **Documentation**: See files in this repository
- **Discord**: https://discord.gg/MnCvHqpUGB
- **Issues**: https://github.com/HKUDS/nanobot/issues

---

*nanobot is for educational, research, and technical exchange purposes only*
