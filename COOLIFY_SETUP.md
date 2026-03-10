# Coolify Deployment from GitHub - Complete Setup Guide

Deploy ClawCustom v2.0 from GitHub to Coolify in 10 minutes.

---

## 🎯 Quick Overview

**Repository:** https://github.com/jeccleston/clawcustom  
**Branch:** main  
**Deploy Time:** 5-10 minutes  
**Difficulty:** Easy  

---

## 📋 Pre-Deployment Checklist

### Repository Setup
- [x] Code pushed to GitHub
- [x] Branch: `main`
- [x] README.md updated
- [x] Dockerfile present
- [x] docker-compose.coolify.yml present
- [x] coolify.json present

### Your Setup
- [ ] Coolify instance running
- [ ] Docker installed on Coolify server
- [ ] LLM API key ready (OpenRouter/Anthropic/DashScope)

---

## 🚀 Deployment Steps

### Step 1: Create Project (2 min)

1. Open Coolify Dashboard
2. **"+ New"** → **"+ New Project"**
3. Name: `clawcustom`
4. Click **"Create"**

### Step 2: Add Service from GitHub (3 min)

1. **"+ New"** → **"+ New Service"**
2. Select **"Public Git Repository"**
3. Enter:
   - Repository URL: `https://github.com/jeccleston/clawcustom`
   - Branch: `main`
4. Build Pack: **Docker Compose**
5. Compose File: `docker-compose.coolify.yml`
6. Click **"Save"**

### Step 3: Configure Environment Variables (2 min)

Add these **required** variables:

```bash
# LLM Provider (choose one)
OPENROUTER_API_KEY=sk-or-v1-xxx
# OR
ANTHROPIC_API_KEY=sk-ant-xxx

# Model Configuration
AI_MODEL=anthropic/claude-opus-4-5
AI_PROVIDER=auto
AI_TEMPERATURE=0.1
AI_MAX_TOKENS=8192

# Security
RESTRICT_TO_WORKSPACE=true

# Resources
MEMORY_LIMIT=1G
CPU_LIMIT=1
```

### Step 4: Deploy (3 min)

1. Click **"Deploy"**
2. Wait for build (~2-3 minutes)
3. Health check should pass

**Success indicators:**
```
✓ Build completed
✓ Container started  
✓ Health check passed
```

### Step 5: Test (1 min)

**Terminal tab → Run:**
```bash
clawcustom agent -m "help"
```

**Expected output:**
```
# ClawCustom Help

Welcome! I'm here to help you with:

1. Specialized Workers - AI agents for coding, research, writing
2. Docker Environments - Instant dev sandboxes
3. Stock Analysis - Real-time market data
4. Document Processing - Work with PDF and Word
5. Multi-Platform Chat - Telegram, Discord, WhatsApp
```

---

## ⚙️ Configuration Reference

### Environment Variables Table

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENROUTER_API_KEY` | OpenRouter API key | ✅ | - |
| `ANTHROPIC_API_KEY` | Anthropic API key | ✅ | - |
| `DASHSCOPE_API_KEY` | DashScope API key | ❌ | - |
| `AI_MODEL` | Model name | ❌ | `anthropic/claude-opus-4-5` |
| `AI_PROVIDER` | Provider name | ❌ | `auto` |
| `AI_TEMPERATURE` | Temperature 0.0-1.0 | ❌ | `0.1` |
| `AI_MAX_TOKENS` | Max response tokens | ❌ | `8192` |
| `BRAVE_SEARCH_API_KEY` | Web search key | ❌ | - |
| `TELEGRAM_ENABLED` | Enable Telegram | ❌ | `false` |
| `TELEGRAM_BOT_TOKEN` | Telegram token | ❌ | - |
| `DISCORD_ENABLED` | Enable Discord | ❌ | `false` |
| `DISCORD_BOT_TOKEN` | Discord token | ❌ | - |
| `WHATSAPP_ENABLED` | Enable WhatsApp | ❌ | `false` |
| `RESTRICT_TO_WORKSPACE` | Security restriction | ❌ | `true` |
| `MEMORY_LIMIT` | Memory limit | ❌ | `1G` |
| `CPU_LIMIT` | CPU cores limit | ❌ | `1` |

### Resource Presets

**Development:**
```yaml
CPU_LIMIT: 1
MEMORY_LIMIT: 512M
```

**Production:**
```yaml
CPU_LIMIT: 2
MEMORY_LIMIT: 2G
```

**Heavy Usage:**
```yaml
CPU_LIMIT: 4
MEMORY_LIMIT: 4G
```

---

## 🐛 Troubleshooting

### Build Fails

**Error:** `dockerfile not found`

**Solution:**
- Verify repository URL is correct
- Check branch name matches
- Ensure Dockerfile exists at root

### Container Won't Start

**Error:** `No API key found`

**Solution:**
```bash
# Set in Environment Variables
OPENROUTER_API_KEY=sk-or-v1-xxx
# OR
ANTHROPIC_API_KEY=sk-ant-xxx
```

### Health Check Fails

**Error:** `Health check failed`

**Solutions:**
1. Wait 5 minutes (first startup is slow)
2. Check logs for errors
3. Verify API key is valid
4. Increase start_period to 60s

### Out of Memory

**Error:** `Killed` or `OOM`

**Solution:**
```bash
MEMORY_LIMIT=2G
```

### Port Conflict

**Error:** `Port already in use`

**Solution:**
```bash
GATEWAY_PORT=18791
```

---

## 🔄 Updates

### Enable Auto-Deploy

1. Settings → Advanced
2. Toggle **"Auto Deploy"** ON
3. Now git pushes trigger automatic deployment

### Manual Update

1. Settings → Advanced
2. Click **"Pull Latest Changes"**
3. Click **"Redeploy"**

---

## 💾 Backup

### Create Backup

```bash
docker run --rm \
  -v clawcustom-data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/clawcustom-$(date +%Y%m%d).tar.gz /data
```

### Restore Backup

```bash
# Stop container
docker compose down

# Restore
docker run --rm \
  -v clawcustom-data:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/clawcustom-20260308.tar.gz -C /data

# Start
docker compose up -d
```

---

## 📊 Monitoring

### View Logs

**Coolify UI:**
- Logs tab → Real-time streaming

**Terminal:**
```bash
docker logs -f <container-id>
```

### Check Status

```bash
docker exec -it <container> clawcustom status
```

### Resource Usage

**Coolify UI:**
- Metrics tab → CPU/Memory/Network

**Terminal:**
```bash
docker stats <container-id>
```

---

## 📞 Support

- **Discord:** https://discord.gg/MnCvHqpUGB
- **GitHub Issues:** https://github.com/jeccleston/clawcustom/issues
- **Documentation:** README.md, COOLIFY_QUICK_START.md

---

## ✅ Deployment Complete Checklist

- [ ] Project created in Coolify
- [ ] Service added from GitHub
- [ ] Environment variables configured
- [ ] Deploy successful
- [ ] Health check passed
- [ ] Tested with `clawcustom agent -m "help"`
- [ ] (Optional) Chat channels enabled
- [ ] (Optional) Auto-deploy enabled
- [ ] (Optional) Backups configured

---

## 🎉 Next Steps

1. **Run onboarding:**
   ```bash
   clawcustom onboard
   ```

2. **Test workers:**
   ```bash
   clawcustom agent -m "use coder to build API"
   ```

3. **Create environment:**
   ```bash
   clawcustom agent -m "create python environment"
   ```

4. **Enable chat:**
   - Telegram: Add bot token, set TELEGRAM_ENABLED=true
   - Discord: Add bot token, set DISCORD_ENABLED=true
   - WhatsApp: Run `clawcustom channels login`

5. **Join community:**
   - Discord: https://discord.gg/MnCvHqpUGB

---

**Ready to deploy! 🚀**

For detailed guide, see [COOLIFY_QUICK_START.md](COOLIFY_QUICK_START.md)
