# Deploy clawcustom to Coolify

Complete guide for deploying clawcustom (clawwork) on Coolify - a self-hosted Vercel/Netlify alternative.

## Prerequisites

- A Coolify instance installed on your server
- Docker installed on Coolify server
- An API key from an LLM provider (OpenRouter, Anthropic, DashScope, etc.)

## Quick Deploy (5 minutes)

### 1. Create New Project in Coolify

1. Open your Coolify dashboard
2. Click **"+ New"** → **"+ New Project"**
3. Name it `clawcustom` (or `clawwork`)
4. Click **Create**

### 2. Add New Service

1. In your project, click **"+ New"** → **"+ New Service"**
2. Choose **"Docker Compose"** or **"Dockerfile"** based deployment

#### Option A: Docker Compose (Recommended)

1. Select **"Docker Compose"**
2. In the **Compose file** field, paste the contents of `docker-compose.coolify.yml`
3. Click **Save**

#### Option B: Dockerfile

1. Select **"Public Git repository"**
2. Enter repository URL: `https://github.com/HKUDS/clawcustom.git`
3. Branch: `main`
4. Build Pack: **Dockerfile**
5. Dockerfile path: `Dockerfile`
6. Click **Save**

### 3. Configure Environment Variables

In Coolify's **Environment Variables** tab, add these **required** variables:

```bash
# Choose ONE provider:
OPENROUTER_API_KEY=sk-or-v1-xxx         # OpenRouter (recommended)
# OR
ANTHROPIC_API_KEY=sk-ant-xxx            # Anthropic direct
# OR
DASHSCOPE_API_KEY=xxx                   # Alibaba DashScope

# Model selection:
AI_MODEL=anthropic/claude-opus-4-5
AI_PROVIDER=auto
```

**Optional variables:**

```bash
# Web search capability:
BRAVE_SEARCH_API_KEY=xxx

# Chat channels:
TELEGRAM_ENABLED=true
TELEGRAM_BOT_TOKEN=xxx

# Resource limits:
CPU_LIMIT=1
MEMORY_LIMIT=1G
```

### 4. Configure Domain (Optional)

If you want to access clawcustom via a custom domain:

1. Go to **Domain** tab
2. Add your domain: `clawcustom.yourdomain.com`
3. Coolify will auto-configure reverse proxy and SSL

### 5. Deploy

1. Click **"Deploy"** button
2. Wait for build to complete (~2-3 minutes)
3. Check **Logs** tab for startup messages

## Post-Deployment Setup

### 1. Verify Deployment

```bash
# Check container status
docker ps | grep clawcustom

# View logs
docker logs -f <container-id>

# Or in Coolify: Click "Logs" tab
```

### 2. Initial Configuration

The first time clawcustom runs, it will create default config in the persistent volume.

**Option 1: Via CLI (if you have server access)**
```bash
docker exec -it <container-id> clawcustom onboard
```

**Option 2: Edit config directly**
```bash
# Access the volume
docker volume inspect clawcustom-data

# Edit config.json
docker exec -it <container-id> nano /root/.clawcustom/config.json
```

### 3. Enable Chat Channels

#### Telegram

1. Create bot via @BotFather in Telegram
2. Get bot token
3. Add to Coolify environment:
   ```bash
   TELEGRAM_ENABLED=true
   TELEGRAM_BOT_TOKEN=your-bot-token
   ```
4. Redeploy

#### Discord

1. Create app at https://discord.com/developers
2. Enable **MESSAGE CONTENT INTENT**
3. Get bot token
4. Add to Coolify:
   ```bash
   DISCORD_ENABLED=true
   DISCORD_BOT_TOKEN=your-bot-token
   ```
5. Redeploy

#### WhatsApp

WhatsApp requires QR code scanning:

```bash
# Execute in container
docker exec -it <container-id> clawcustom channels login

# Scan QR code with WhatsApp
# Settings → Linked Devices → Link a Device
```

### 4. Test the Agent

**Via Coolify Terminal:**
```bash
docker exec -it <container-id> clawcustom agent -m "Hello! What can you do?"
```

**Via Chat Channel:**
Send a message to your bot on Telegram/Discord/WhatsApp

## Coolify-Specific Configuration

### Resource Allocation

Recommended for production:

```yaml
CPU_LIMIT: 2           # 2 cores
CPU_RESERVATION: 0.5   # 0.5 cores guaranteed
MEMORY_LIMIT: 2G       # 2GB RAM
MEMORY_RESERVATION: 512M  # 512MB guaranteed
```

For testing/development:

```yaml
CPU_LIMIT: 1
CPU_RESERVATION: 0.25
MEMORY_LIMIT: 1G
MEMORY_RESERVATION: 256M
```

### Persistent Storage

Coolify automatically creates the `clawcustom-data` volume. This persists:

- `~/.clawcustom/config.json` - Your configuration
- `~/.clawcustom/workspace/` - Agent workspace
- `~/.clawcustom/workspace/MEMORY.md` - Long-term memory
- `~/.clawcustom/workspace/HEARTBEAT.md` - Periodic tasks
- `~/.clawcustom/sessions/` - Chat sessions

### Auto-Restart Policy

Set in Coolify service settings:
- **Restart Policy**: `unless-stopped`
- **Health Check**: Enabled (already configured)

### Multiple Instances

Deploy multiple clawcustom instances for different purposes:

1. Create separate services in Coolify
2. Use different ports: `18791`, `18792`, etc.
3. Use separate volumes: `clawcustom-bot1-data`, `clawcustom-bot2-data`
4. Configure different channels/models per instance

## Troubleshooting

### Container Won't Start

**Check logs:**
```bash
docker logs <container-id>
```

**Common issues:**

1. **Missing API key**: Check environment variables
2. **Invalid model name**: Verify `AI_MODEL` format
3. **Port conflict**: Change `GATEWAY_PORT`

### Can't Access Chat Channels

1. **Verify tokens**: Check channel tokens in Coolify env vars
2. **Check permissions**: Ensure bot has required permissions
3. **Review logs**: Look for authentication errors

### Memory Issues

If container is killed for OOM:

1. Increase `MEMORY_LIMIT` in Coolify
2. Reduce `AI_MAX_TOKENS`
3. Lower model complexity

### Configuration Not Persisting

Ensure volume is properly mounted:

```bash
docker volume inspect clawcustom-data
```

If volume is missing, recreate:
```bash
docker volume create clawcustom-data
```

## Advanced Configuration

### Custom Config File

1. Create `config.json` locally
2. Mount it in Coolify:
   ```yaml
   volumes:
     - ./config.json:/root/.clawcustom/config.json:ro
   ```
3. Or use Coolify's "File Mounts" feature

### MCP Servers

Add Model Context Protocol servers for extended capabilities:

```json
{
  "tools": {
    "mcpServers": {
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/app/data"]
      }
    }
  }
}
```

### Multiple LLM Providers

Configure fallback providers:

```bash
# Primary
OPENROUTER_API_KEY=sk-or-v1-xxx

# Fallback
ANTHROPIC_API_KEY=sk-ant-xxx

# Model will auto-detect available provider
AI_PROVIDER=auto
```

## Security Best Practices

1. **Restrict workspace access:**
   ```bash
   RESTRICT_TO_WORKSPACE=true
   ```

2. **Use allowlists for channels:**
   ```json
   {
     "channels": {
       "telegram": {
         "allowFrom": ["your-user-id"]
       }
     }
   }
   ```

3. **Rotate API keys regularly**

4. **Use HTTPS for all webhooks**

5. **Keep Coolify and clawcustom updated**

## Monitoring

### Coolify Built-in Monitoring

- **Metrics tab**: CPU, memory, network usage
- **Logs tab**: Real-time container logs
- **Notifications**: Set up alerts for failures

### Custom Health Checks

Add to docker-compose:

```yaml
healthcheck:
  test: ["CMD", "clawcustom", "status"]
  interval: 60s
  timeout: 10s
  retries: 3
```

## Updates and Maintenance

### Update clawcustom

**Docker Compose:**
```bash
docker-compose pull
docker-compose up -d
```

**In Coolify:**
1. Click **"Redeploy"** button
2. Or enable **"Auto Deploy"** for git-based deployments

### Backup Configuration

```bash
# Backup config and data
docker run --rm -v clawcustom-data:/data -v $(pwd):/backup alpine tar czf /backup/clawcustom-backup.tar.gz /data

# Restore
docker run --rm -v clawcustom-data:/data -v $(pwd):/backup alpine tar xzf /backup/clawcustom-backup.tar.gz -C /data
```

## Support

- **Documentation**: https://github.com/HKUDS/clawcustom
- **Discord**: https://discord.gg/MnCvHqpUGB
- **Issues**: https://github.com/HKUDS/clawcustom/issues

## Cost Estimation

**Monthly costs** (excluding Coolify server):

| Provider | Model | Estimated Cost* |
|----------|-------|-----------------|
| OpenRouter | Claude-3.5-Sonnet | $5-20 |
| Anthropic | Claude-Opus | $10-50 |
| DashScope | Qwen-Max | $2-10 |
| DeepSeek | DeepSeek-Chat | $1-5 |

*Based on moderate personal usage. Actual costs vary by usage.

---

**Happy deploying! 🚀**
