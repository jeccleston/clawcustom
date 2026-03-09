# 🚀 Coolify Quick Start Guide

Deploy ClawCustom on Coolify in 5 minutes.

---

## Prerequisites

- Coolify instance installed and running
- Docker installed on Coolify server
- LLM API key (OpenRouter, Anthropic, or DashScope)

---

## Step 1: Create Project in Coolify

1. Open your Coolify dashboard
2. Click **"+ New"** → **"+ New Project"**
3. Name: `clawcustom`
4. Click **"Create"**

---

## Step 2: Add New Service

1. In your project, click **"+ New"** → **"+ New Service"**
2. Select **"Docker Compose"**
3. In **Compose file** field, paste contents of `docker-compose.coolify.yml`
4. Click **"Save"**

---

## Step 3: Configure Environment Variables

In Coolify's **Environment Variables** tab, add these required variables:

### Required (Choose One Provider)

```bash
# Option 1: OpenRouter (Recommended)
OPENROUTER_API_KEY=sk-or-v1-your-actual-key

# OR Option 2: Anthropic
ANTHROPIC_API_KEY=sk-ant-your-actual-key

# OR Option 3: DashScope
DASHSCOPE_API_KEY=your-actual-key
```

### Model Configuration

```bash
AI_MODEL=anthropic/claude-opus-4-5
AI_PROVIDER=auto
AI_TEMPERATURE=0.1
AI_MAX_TOKENS=8192
```

### Security (Recommended for Production)

```bash
RESTRICT_TO_WORKSPACE=true
```

### Resource Limits

```bash
CPU_LIMIT=1
MEMORY_LIMIT=1G
```

---

## Step 4: Deploy

1. Click **"Deploy"** button
2. Wait for build to complete (~2-3 minutes)
3. Check **"Logs"** tab for startup messages

**Build is successful when you see:**
```
✓ nanobot status check passed
✓ Agent loop started
```

---

## Step 5: Test Installation

### Option 1: Via Coolify Terminal

1. Go to **"Terminal"** tab in Coolify
2. Run:
```bash
nanobot agent -m "Hello! What can you do?"
```

### Option 2: Via Docker Command

```bash
# Get container ID
docker ps | grep nanobot

# Execute command
docker exec -it <container-id> nanobot agent -m "Hello!"
```

### Expected Response

You should see a response like:
```
Hello! I'm ClawCustom, your AI assistant. I can help you with:

1. 🤖 Specialized worker agents (coder, researcher, writer, analyst, etc.)
2. 📈 Stock market analysis and portfolio tracking
3. 📄 Document processing (Word, PDF)
4. 💬 Multi-platform chat (Telegram, Discord, WhatsApp)
5. 🛠️ Full-stack development with Docker sandboxes

What would you like to do today?
```

---

## Step 6: Enable Chat Channels (Optional)

### Telegram

1. **Get Bot Token:**
   - Open Telegram, search `@BotFather`
   - Send `/newbot`, follow prompts
   - Copy the token

2. **Add to Coolify:**
```bash
TELEGRAM_ENABLED=true
TELEGRAM_BOT_TOKEN=your-bot-token-from-botfather
```

3. **Redeploy** in Coolify

4. **Find your User ID:**
   - Message your bot on Telegram
   - Check logs in Coolify for your user ID
   - Add to `TELEGRAM_ALLOW_FROM`

### WhatsApp

1. **Open Terminal in Coolify**

2. **Run:**
```bash
nanobot channels login
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

5. **Redeploy**

### Discord

1. **Create Discord App:**
   - Go to https://discord.com/developers
   - Create Application → Bot → Add Bot
   - Copy bot token

2. **Enable Intents:**
   - Bot settings → Enable **MESSAGE CONTENT INTENT**

3. **Add to Coolify:**
```bash
DISCORD_ENABLED=true
DISCORD_BOT_TOKEN=your-bot-token
```

4. **Invite Bot:**
   - OAuth2 → URL Generator
   - Scopes: `bot`
   - Permissions: `Send Messages`, `Read Message History`
   - Open URL and add to server

5. **Redeploy**

---

## Step 7: Usage Examples

### Specialized Workers

```bash
# Coder worker
nanobot agent -m "Spawn a coder to build a REST API with FastAPI"

# Researcher worker
nanobot agent -m "Spawn a researcher to analyze the AI market"

# Writer worker
nanobot agent -m "Spawn a writer to create API documentation"
```

### Stock Analysis

```bash
# Get stock info
nanobot agent -m "What's the price and P/E ratio of AAPL?"

# Compare stocks
nanobot agent -m "Compare NVDA, AMD, INTC performance"

# Market overview
nanobot agent -m "Show me today's market overview"
```

### Document Processing

```bash
# Extract PDF
nanobot agent -m "Extract text from report.pdf and summarize"

# Create Word doc
nanobot agent -m "Create a Word document with meeting notes"
```

---

## Troubleshooting

### Container Won't Start

**Check logs:**
```bash
# In Coolify: Logs tab
# Or via SSH:
docker logs <container-id>
```

**Common issues:**

1. **Missing API Key**
   - Check `OPENROUTER_API_KEY` or other provider
   - Ensure no extra spaces

2. **Invalid Model**
   - Verify `AI_MODEL` format: `provider/model-name`
   - Check model is available with your provider

3. **Port Conflict**
   - Change `GATEWAY_PORT` to different port
   - Check port is not in use

### Workers Not Spawning

```bash
# Verify installation
nanobot status

# Check if yfinance installed
pip show yfinance

# Install if missing
pip install yfinance pandas
```

### Memory Issues

If container is killed for OOM:

1. Increase in Coolify Environment Variables:
```bash
MEMORY_LIMIT=2G
MEMORY_RESERVATION=512M
```

2. Or reduce model complexity:
```bash
AI_MAX_TOKENS=4096
```

### Can't Access Chat Channels

1. **Verify tokens** in Coolify env vars
2. **Check bot permissions** (Discord: MESSAGE CONTENT INTENT)
3. **Review logs** for authentication errors
4. **Ensure enabled** (`TELEGRAM_ENABLED=true`)

---

## Monitoring

### View Logs

**Coolify UI:**
- Go to **"Logs"** tab
- Real-time streaming logs

**Via SSH:**
```bash
docker logs -f <container-id>
```

### Check Status

```bash
docker exec -it <container-id> nanobot status
```

### Resource Usage

**Coolify UI:**
- Go to **"Metrics"** tab
- View CPU, memory, network

**Via SSH:**
```bash
docker stats <container-id>
```

---

## Updates

### Manual Update

1. **In Coolify:**
   - Go to service
   - Click **"Redeploy"**

2. **Or via Git:**
   ```bash
   git pull
   # Coolify auto-deploys if enabled
   ```

### Enable Auto-Deploy

1. **In Coolify:**
   - Settings → **Auto Deploy**
   - Toggle **ON**
   - Now pushes to main branch trigger deploy

---

## Backup & Restore

### Backup Configuration

```bash
# Create backup
docker run --rm \
  -v nanobot-data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/clawcustom-backup-$(date +%Y%m%d).tar.gz /data
```

### Restore from Backup

```bash
# Stop container
docker compose down

# Restore
docker run --rm \
  -v nanobot-data:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/clawcustom-backup-YYYYMMDD.tar.gz -C /data

# Restart
docker compose up -d
```

---

## Production Configuration

### Recommended for Production

```bash
# More resources
CPU_LIMIT=2
CPU_RESERVATION=0.5
MEMORY_LIMIT=2G
MEMORY_RESERVATION=512M

# Security
RESTRICT_TO_WORKSPACE=true
ALLOW_FROM=user-id-1,user-id-2

# Provider (use dedicated key)
OPENROUTER_API_KEY=sk-or-v1-prod-key
AI_MODEL=anthropic/claude-opus-4-5

# Domain
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

## Cost Estimation

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

## Next Steps

1. ✅ **Test basic functionality**
2. ✅ **Enable chat channels** (Telegram, Discord, etc.)
3. ✅ **Configure worker agents** for your use cases
4. ✅ **Set up monitoring** and alerts
5. ✅ **Schedule backups**
6. ✅ **Invite team members** (if applicable)

---

## Support

- **Documentation**: See README.md
- **Worker Guide**: WORKER_AGENTS.md
- **Examples**: WORKER_EXAMPLES.md
- **Issues**: https://github.com/jeccleston/clawcustom/issues
- **Discord**: https://discord.gg/MnCvHqpUGB

---

**Happy deploying! 🎉**
