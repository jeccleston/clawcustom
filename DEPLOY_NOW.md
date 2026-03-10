# 🚀 Deploy ClawCustom to Coolify - INSTANT START

**Repository:** https://github.com/jeccleston/clawcustom  
**Branch:** `master`  
**Deploy Time:** 5 minutes  
**AI Provider:** DashScope (Alibaba Cloud Qwen)  

---

## ⚡ Quick Deploy (Copy-Paste Ready)

### 1. Create Project
```
Coolify Dashboard → + New → + New Project
Name: clawcustom
```

### 2. Add Service from GitHub
```
+ New → + New Service → Public Git Repository

Repository URL: https://github.com/jeccleston/clawcustom
Branch: master  ← IMPORTANT: Use master, NOT main
Build Pack: Docker Compose
Compose File: docker-compose.coolify.yml
```

### 3. Environment Variables (Copy-Paste)

**Required:**
```bash
# DashScope API Key (Get from https://dashscope.console.aliyun.com)
DASHSCOPE_API_KEY=sk-your-dashscope-key-here

# API Base URL (Coding Plan endpoint)
DASHSCOPE_API_BASE=https://coding-intl.dashscope.aliyuncs.com/v1

# Model (Qwen)
AI_MODEL=qwen3.5-plus
AI_PROVIDER=dashscope
```

**Optional:**
```bash
AI_TEMPERATURE=0.1
AI_MAX_TOKENS=8192
RESTRICT_TO_WORKSPACE=true
MEMORY_LIMIT=1G
CPU_LIMIT=1
```

### 4. Deploy
```
Click "Deploy" → Wait 2-3 minutes
```

### 5. Test
```
Terminal tab → clawcustom agent -m "help"
```

**Expected Output:**
```
Hello! I'm ClawCustom, your AI assistant powered by Qwen (DashScope).

I can help you with:
1. 🤖 Specialized worker agents (coder, researcher, writer, etc.)
2. 🐳 Docker development environments
3. 📈 Stock market analysis
4. 📄 Document processing
5. 💬 Multi-platform chat

What would you like to do today?
```

---

## 🔑 Get DashScope API Key

### Quick Steps:

1. **Visit:** https://dashscope.console.aliyun.com
2. **Login/Register:** Alibaba Cloud account
3. **Navigate:** API-KEY Management (left sidebar)
4. **Create:** New API Key
5. **Copy:** Save the key securely

**API Key Format:** `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Detailed Guide:

See [DASHSCOPE_SETUP.md](DASHSCOPE_SETUP.md) for complete setup instructions.

---

## ✅ Success Checklist

- [ ] Repository: https://github.com/jeccleston/clawcustom
- [ ] Branch: **master** (NOT main)
- [ ] Compose file: docker-compose.coolify.yml
- [ ] DashScope API key obtained
- [ ] DASHSCOPE_API_KEY configured
- [ ] DASHSCOPE_API_BASE set to coding-intl endpoint
- [ ] AI_MODEL set to qwen3.5-plus
- [ ] Deploy completed
- [ ] Health check passed
- [ ] Test command works

---

## 🐛 Troubleshooting

### "Remote branch main not found"
**Solution:** Use branch **`master`** (not main)

### "No API key found"
**Solution:** Set `DASHSCOPE_API_KEY` from https://dashscope.console.aliyun.com

### "Model not found"
**Solution:** Verify model name is `qwen3.5-plus` (not qwen-3.5-plus)

### "Health check failed"
**Solution:** Wait 5 minutes, check API key is valid, verify DASHSCOPE_API_BASE

### "Connection timeout"
**Solution:** Check DASHSCOPE_API_BASE is `https://coding-intl.dashscope.aliyuncs.com/v1`

---

## 💡 Model Options

| Model | Best For | Cost |
|-------|----------|------|
| **qwen3.5-plus** ⭐ | Balanced performance/cost | ~¥0.02/1K |
| qwen-max | Complex coding tasks | ~¥0.04/1K |
| qwen-plus | General purpose | ~¥0.015/1K |
| qwen-turbo | Fast, simple queries | ~¥0.008/1K |

**Default:** qwen3.5-plus (recommended for most use cases)

---

## 📚 Full Guides

- **[DASHSCOPE_SETUP.md](DASHSCOPE_SETUP.md)** - Complete DashScope setup
- **[COOLIFY_QUICK_START.md](COOLIFY_QUICK_START.md)** - 5-minute quick start
- **[COOLIFY_SETUP.md](COOLIFY_SETUP.md)** - Detailed deployment guide
- **[README.md](README.md)** - Main documentation

---

## 💰 Cost Estimation

**qwen3.5-plus (typical usage):**
- Light use (10 conv/day): ~$2-5/month
- Moderate use (50 conv/day): ~$5-15/month
- Heavy use (200 conv/day): ~$15-40/month

**Much more cost-effective than:** Claude ($15-50/month) or GPT-4 ($20-60/month)

---

## 🆘 Support

- **DashScope Docs:** https://help.aliyun.com/zh/dashscope/
- **Discord:** https://discord.gg/MnCvHqpUGB
- **GitHub Issues:** https://github.com/jeccleston/clawcustom/issues

---

## 🎉 Next Steps After Deploy

1. **Run onboarding:**
   ```bash
   clawcustom onboard
   ```

2. **Test workers:**
   ```bash
   clawcustom agent -m "use coder to build a REST API"
   ```

3. **Create environment:**
   ```bash
   clawcustom agent -m "create python environment"
   ```

4. **Enable chat:**
   - Telegram: Add bot token, set TELEGRAM_ENABLED=true
   - Discord: Add bot token, set DISCORD_ENABLED=true

5. **Join community:**
   - Discord: https://discord.gg/MnCvHqpUGB

---

**Ready to deploy! Use branch `master` and DashScope API key** 🚀

*Powered by Alibaba Cloud Qwen (DashScope)*
