# Coolify Quick Start Guide - ClawCustom v2.0

Deploy ClawCustom on Coolify in **5 minutes** from GitHub.

---

## 📋 Prerequisites

- ✅ Coolify instance installed and running
- ✅ Docker installed on Coolify server
- ✅ GitHub account (to access repository)
- ✅ LLM API key (OpenRouter, Anthropic, or DashScope)

---

## 🚀 Quick Deploy (5 Minutes)

### Step 1: Create Project in Coolify

1. Open your **Coolify Dashboard**
2. Click **"+ New"** → **"+ New Project"**
3. Name: `clawcustom` (or your preferred name)
4. Click **"Create"**

---

### Step 2: Add Service from GitHub

1. In your project, click **"+ New"** → **"+ New Service"**
2. Select **"Public Git Repository"**
3. Enter repository URL:
   ```
   https://github.com/jeccleston/clawcustom
   ```
4. Branch: `main` (or your branch)
5. Build Pack: **Docker Compose**
6. Compose file: `docker-compose.coolify.yml`
7. Click **"Save"**

---

### Step 3: Configure Environment Variables

In Coolify's **Environment Variables** tab, add these:

#### 🔑 Required (Choose ONE Provider)

```bash
# Option 1: OpenRouter (Recommended - All models)
# Get key: https://openrouter.ai/keys
OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here

# OR Option 2: Anthropic (Claude models)
# Get key: https://console.anthropic.com
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here

# OR Option 3: DashScope (Qwen models - China)
# Get key: https://dashscope.console.aliyun.com
DASHSCOPE_API_KEY=your-key-here
```

#### 🤖 Model Configuration

```bash
# Recommended model
AI_MODEL=anthropic/claude-opus-4-5

# Provider (auto-detects from API key)
AI_PROVIDER=auto

# Temperature (0.0 = focused, 1.0 = creative)
AI_TEMPERATURE=0.1

# Max response length
AI_MAX_TOKENS=8192
```

#### 🛡️ Security (Recommended)

```bash
# Restrict file access to workspace
RESTRICT_TO_WORKSPACE=true
```

#### 💾 Resource Limits

```bash
# Development / Light usage
CPU_LIMIT=1
MEMORY_LIMIT=1G

# Production / Heavy usage (recommended)
CPU_LIMIT=2
MEMORY_LIMIT=2G
```

#### 📱 Optional: Chat Channels

**Telegram:**
```bash
TELEGRAM_ENABLED=true
TELEGRAM_BOT_TOKEN=your-bot-token-from-botfather
```

**Discord:**
```bash
DISCORD_ENABLED=true
DISCORD_BOT_TOKEN=your-bot-token
```

**WhatsApp:** (Enable after deploy)
```bash
WHATSAPP_ENABLED=true
```

---

### Step 4: Deploy

1. Click **"Deploy"** button
2. Wait for build to complete (~2-3 minutes)
3. Watch the **Logs** tab for progress

**Build Success Indicators:**
```
✓ Build completed
✓ Container started
✓ Health check passed
✓ clawcustom status check passed
```

---

### Step 5: Test Installation

#### Option 1: Via Coolify Terminal

1. Go to **"Terminal"** tab in Coolify
2. Run:
   ```bash
   clawcustom agent -m "help"
   ```

#### Option 2: Via Docker Command

1. Go to **"Terminal"** tab
2. Get container name:
   ```bash
   docker ps
   ```
3. Execute command:
   ```bash
   docker exec -it <container-name> clawcustom agent -m "Hello! What can you do?"
   ```

**Expected Response:**
```
Hello! I'm ClawCustom, your AI assistant. I can help you with:

1. 🤖 Specialized worker agents (coder, researcher, writer, analyst, etc.)
2. 🐳 Docker development environments
3. 📈 Stock market analysis
4. 📄 Document processing (Word, PDF)
5. 💬 Multi-platform chat (Telegram, Discord, WhatsApp)

Type 'help' to see available commands.

What would you like to do today?
```

---

## ⚙️ Post-Deployment Setup

### 1. Interactive Onboarding (Recommended)

Run the guided setup:
```bash
docker exec -it <container> clawcustom onboard
```

The wizard will ask:
- Your name
- Primary use case
- Preferred chat channel
- LLM provider choice
- API key (if not set in env vars)

### 2. Enable Chat Channels

#### **Telegram** (5 minutes)

1. **Create Bot:**
   - Open Telegram → Search `@BotFather`
   - Send `/newbot`
   - Follow prompts to name your bot
   - Copy the bot token

2. **Configure in Coolify:**
   - Add to Environment Variables:
     ```bash
     TELEGRAM_ENABLED=true
     TELEGRAM_BOT_TOKEN=paste-your-token-here
     ```
   - Click **"Save"** then **"Redeploy"**

3. **Start Chatting:**
   - Open Telegram
   - Search for your bot by name
   - Send `/start`

#### **Discord** (10 minutes)

1. **Create Discord App:**
   - Go to https://discord.com/developers
   - Click "New Application"
   - Go to "Bot" → "Add Bot"
   - Copy bot token

2. **Enable Intents:**
   - Bot settings → Enable **MESSAGE CONTENT INTENT**

3. **Invite Bot to Server:**
   - OAuth2 → URL Generator
   - Scopes: `bot`
   - Permissions: `Send Messages`, `Read Message History`
   - Open generated URL and add to server

4. **Configure in Coolify:**
   ```bash
   DISCORD_ENABLED=true
   DISCORD_BOT_TOKEN=paste-your-token-here
   ```
   - Save and Redeploy

#### **WhatsApp** (2 minutes)

1. **Open Terminal in Coolify**

2. **Run Login Command:**
   ```bash
   docker exec -it <container> clawcustom channels login
   ```

3. **Scan QR Code:**
   - Open WhatsApp on phone
   - Settings → Linked Devices
   - Link a Device
   - Scan the QR code shown in terminal

4. **Configure:**
   ```bash
   WHATSAPP_ENABLED=true
   ```
   - Save and Redeploy

---

## 💡 Usage Examples

### Spawn Specialized Workers

```bash
# Coder - Build features
clawcustom agent -m "use coder to build a REST API with FastAPI"

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

## 🔧 Configuration

### Config File Location

Configuration is stored in:
```
/root/.clawcustom/config.json
```

To edit:
```bash
# Via Terminal
docker exec -it <container> nano /root/.clawcustom/config.json

# Or mount as volume in docker-compose.coolify.yml:
volumes:
  - ./config.json:/root/.clawcustom/config.json
```

### Environment Variables Reference

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPENROUTER_API_KEY` | OpenRouter API key | - | ✅ (or Anthropic) |
| `ANTHROPIC_API_KEY` | Anthropic API key | - | ✅ (or OpenRouter) |
| `DASHSCOPE_API_KEY` | DashScope API key | - | ❌ |
| `AI_MODEL` | Model to use | `anthropic/claude-opus-4-5` | ❌ |
| `AI_PROVIDER` | Provider preference | `auto` | ❌ |
| `AI_TEMPERATURE` | Temperature (0.0-1.0) | `0.1` | ❌ |
| `AI_MAX_TOKENS` | Max response tokens | `8192` | ❌ |
| `BRAVE_SEARCH_API_KEY` | Web search API key | - | ❌ |
| `TELEGRAM_ENABLED` | Enable Telegram | `false` | ❌ |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | - | ❌ |
| `DISCORD_ENABLED` | Enable Discord | `false` | ❌ |
| `DISCORD_BOT_TOKEN` | Discord bot token | - | ❌ |
| `WHATSAPP_ENABLED` | Enable WhatsApp | `false` | ❌ |
| `RESTRICT_TO_WORKSPACE` | Restrict file access | `true` | ❌ |
| `CPU_LIMIT` | CPU cores limit | `1` | ❌ |
| `MEMORY_LIMIT` | Memory limit | `1G` | ❌ |

---

## 🐛 Troubleshooting

### Container Won't Start

**Check logs:**
```bash
# In Coolify: Logs tab
# Or via Terminal:
docker logs <container-id>
```

**Common Issues:**

1. **Missing API Key**
   - Error: "No API key found"
   - Solution: Set `OPENROUTER_API_KEY` or `ANTHROPIC_API_KEY` in env vars

2. **Invalid Model**
   - Error: "Model not found"
   - Solution: Verify `AI_MODEL` format (e.g., `anthropic/claude-opus-4-5`)

3. **Port Conflict**
   - Error: "Port already in use"
   - Solution: Change `GATEWAY_PORT` to different port (e.g., 18791)

4. **Out of Memory**
   - Error: "Killed" or OOM
   - Solution: Increase `MEMORY_LIMIT` to `2G`

### Workers Not Spawning

```bash
# Check if plugins loaded
clawcustom agent -m "status"

# Verify yfinance installed (for stock analysis)
docker exec -it <container> pip show yfinance

# Install if missing
docker exec -it <container> pip install yfinance pandas
```

### Can't Access Chat Channels

1. **Verify tokens in env vars**
2. **Check bot permissions** (Discord: MESSAGE CONTENT INTENT)
3. **Review logs** for auth errors
4. **Ensure enabled** (`TELEGRAM_ENABLED=true`)

### Environment Creation Fails

```bash
# Check Docker installed
docker --version
docker-compose --version

# Verify Docker running
docker ps

# Check permissions
docker exec -it <container> docker ps
```

### High Memory Usage

1. **Stop unused environments:**
   ```bash
   clawcustom agent -m "list environments"
   clawcustom agent -m "stop environment <name>"
   ```

2. **Reduce concurrent workers:**
   Edit config to limit max workers

3. **Lower AI_MAX_TOKENS:**
   ```bash
   AI_MAX_TOKENS=4096
   ```

---

## 📊 Monitoring

### View Logs

**Coolify UI:**
- Go to **"Logs"** tab
- Real-time streaming logs

**Via Terminal:**
```bash
docker logs -f <container-id>
```

### Check Status

```bash
docker exec -it <container> clawcustom status
```

### Resource Usage

**Coolify UI:**
- Go to **"Metrics"** tab
- View CPU, memory, network usage

**Via Terminal:**
```bash
docker stats <container-id>
```

---

## 🔄 Updates

### Manual Update

1. **In Coolify:**
   - Go to service
   - Click **"Redeploy"**

2. **Or pull latest changes:**
   - Settings → Advanced → Pull Latest Changes
   - Redeploy

### Auto-Deploy (Recommended)

1. **Enable in Coolify:**
   - Settings → **Auto Deploy**
   - Toggle **ON**

2. **Now pushes to main branch trigger automatic deployment**

---

## 💾 Backup & Restore

### Backup Configuration

```bash
# Create backup
docker run --rm \
  -v clawcustom-data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/clawcustom-backup-$(date +%Y%m%d).tar.gz /data
```

### Restore from Backup

```bash
# Stop container in Coolify
docker compose down

# Restore
docker run --rm \
  -v clawcustom-data:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/clawcustom-backup-YYYYMMDD.tar.gz -C /data

# Start container in Coolify
docker compose up -d
```

---

## 📈 Production Configuration

### Recommended for Production

```bash
# More resources
CPU_LIMIT=2
CPU_RESERVATION=0.5
MEMORY_LIMIT=2G
MEMORY_RESERVATION=512M

# Security
RESTRICT_TO_WORKSPACE=true

# Provider (use dedicated key)
OPENROUTER_API_KEY=sk-or-v1-prod-key

# Domain (optional)
DOMAIN=clawcustom.yourdomain.com
```

### High Availability

For production with high traffic:

1. **Multiple instances:**
   - Deploy 2-3 instances
   - Different ports: 18790, 18791, 18792
   - Load balancer in front

2. **Persistent storage:**
   - Use external volume driver
   - Backup regularly

3. **Monitoring:**
   - Set up alerts in Coolify
   - Monitor memory usage
   - Check logs daily

---

## 💰 Cost Estimation

### Coolify Server Costs

| Provider | Instance | RAM | Cost/Mo |
|----------|----------|-----|---------|
| Hetzner | CPX11 | 2GB | ~€5 |
| DigitalOcean | Basic | 1GB | $6 |
| AWS | t3.small | 2GB | ~$15 |
| GCP | e2-small | 2GB | ~$10 |

### LLM API Costs (Estimate)

| Provider | Model | Cost/1K tokens | Est. Monthly* |
|----------|-------|----------------|---------------|
| OpenRouter | Claude-3.5-Sonnet | $0.003 | $5-20 |
| Anthropic | Claude-Opus | $0.015 | $10-50 |
| DeepSeek | DeepSeek-Chat | $0.00014 | $1-5 |
| DashScope | Qwen-Max | $0.002 | $2-10 |

*Based on moderate personal usage (100-500 messages/day)

---

## 📚 Additional Documentation

- **[README.md](README.md)** - Main project documentation
- **[MODULAR_SYSTEM.md](MODULAR_SYSTEM.md)** - v2.0 architecture details
- **[WORKER_AGENTS.md](WORKER_AGENTS.md)** - Worker system guide
- **[WORKER_EXAMPLES.md](WORKER_EXAMPLES.md)** - Usage examples

---

## 🆘 Support

- **Discord Community**: https://discord.gg/MnCvHqpUGB
- **GitHub Issues**: https://github.com/jeccleston/clawcustom/issues
- **Discussions**: https://github.com/jeccleston/clawcustom/discussions

---

## ✅ Deployment Checklist

- [ ] Coolify project created
- [ ] Service added from GitHub
- [ ] docker-compose.coolify.yml selected
- [ ] API key configured (OPENROUTER_API_KEY or ANTHROPIC_API_KEY)
- [ ] AI_MODEL set (recommended: anthropic/claude-opus-4-5)
- [ ] RESTRICT_TO_WORKSPACE=true for security
- [ ] Deploy completed successfully
- [ ] Health check passed
- [ ] Tested with `clawcustom agent -m "help"`
- [ ] (Optional) Chat channels configured
- [ ] (Optional) Auto-deploy enabled

---

**🎉 Congratulations! Your ClawCustom instance is running on Coolify!**

**Next Steps:**
1. Run `clawcustom onboard` for interactive setup
2. Try spawning a worker: `use coder to build a REST API`
3. Explore the help system: `help workers`
4. Join our Discord community for support

**Happy coding! 🚀**
