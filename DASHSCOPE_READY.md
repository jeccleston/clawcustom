# ✅ DashScope Configuration Complete!

Your ClawCustom repository is now fully configured for **Alibaba Cloud DashScope** with the **qwen3.5-plus** model.

---

## 🎯 Configuration Summary

**AI Provider:** DashScope (Alibaba Cloud)  
**Model:** qwen3.5-plus  
**API Endpoint:** https://coding-intl.dashscope.aliyuncs.com/v1  
**Repository:** https://github.com/jeccleston/clawcustom  
**Branch:** master  

---

## 📦 Files Updated

### ✅ Configuration Files

| File | Status | Changes |
|------|--------|---------|
| `.env.coolify` | ✅ Updated | DashScope as primary provider |
| `docker-compose.coolify.yml` | ✅ Updated | DashScope defaults, coding-intl endpoint |
| `coolify.json` | ✅ Updated | DashScope required, qwen3.5-plus default |
| `DEPLOY_NOW.md` | ✅ Updated | DashScope quick deploy guide |
| `DASHSCOPE_SETUP.md` | ✅ NEW | Complete DashScope setup guide |
| `README.md` | ✅ Updated | DashScope as primary provider |

---

## 🚀 Deploy Now

### Quick Start (5 minutes)

**1. Get API Key:**
- Visit: https://dashscope.console.aliyun.com
- Create API key
- Copy key

**2. Deploy on Coolify:**
```
Coolify Dashboard → + New → + New Service
Repository: https://github.com/jeccleston/clawcustom
Branch: master
Compose: docker-compose.coolify.yml
```

**3. Environment Variables:**
```bash
DASHSCOPE_API_KEY=sk-your-key-here
DASHSCOPE_API_BASE=https://coding-intl.dashscope.aliyuncs.com/v1
AI_MODEL=qwen3.5-plus
AI_PROVIDER=dashscope
```

**4. Deploy & Test:**
```
Click Deploy → Wait 2-3 min
Terminal → clawcustom agent -m "help"
```

---

## 🤖 Model: qwen3.5-plus

**Why qwen3.5-plus?**
- ✅ Best balance of performance and cost
- ✅ Excellent for coding tasks
- ✅ Superior Chinese/English bilingual support
- ✅ 256K context window
- ✅ ~¥0.02/1K tokens (very cost-effective)

**Alternative Models:**
- `qwen-max` - Most powerful (higher cost)
- `qwen-plus` - Balanced (good general purpose)
- `qwen-turbo` - Fastest (lowest cost)

---

## 💰 Cost Estimation

**qwen3.5-plus Pricing:**
- Input: ~¥0.02 / 1K tokens
- Output: ~¥0.06 / 1K tokens
- **~$0.003 USD / 1K tokens**

**Monthly Estimates:**
- Light use (10 conversations/day): $2-5
- Moderate use (50 conversations/day): $5-15
- Heavy use (200 conversations/day): $15-40

**Comparison:**
- Claude-3.5-Sonnet: $15-40/month
- GPT-4o: $20-60/month
- **Qwen3.5-Plus: $5-15/month** ⭐

---

## 📚 Documentation

| Guide | Purpose |
|-------|---------|
| **[DASHSCOPE_SETUP.md](DASHSCOPE_SETUP.md)** | Complete DashScope setup |
| **[DEPLOY_NOW.md](DEPLOY_NOW.md)** | Quick deploy guide |
| **[COOLIFY_QUICK_START.md](COOLIFY_QUICK_START.md)** | 5-minute setup |
| **[README.md](README.md)** | Main documentation |

---

## 🧪 Test Your Deployment

```bash
# Test English
clawcustom agent -m "Write a Python function to sort a list"

# Test Chinese
clawcustom agent -m "用 Python 写一个排序函数"

# Test coding
clawcustom agent -m "use coder to build a REST API with FastAPI"

# Test reasoning
clawcustom agent -m "Explain quantum entanglement"
```

---

## 🔧 Configuration Examples

### Environment Variables (Coolify)
```bash
# Required
DASHSCOPE_API_KEY=sk-xxxxxxxx
DASHSCOPE_API_BASE=https://coding-intl.dashscope.aliyuncs.com/v1

# Model
AI_MODEL=qwen3.5-plus
AI_PROVIDER=dashscope
AI_TEMPERATURE=0.1
AI_MAX_TOKENS=8192
```

### Config File (~/.clawcustom/config.json)
```json
{
  "providers": {
    "dashscope": {
      "apiKey": "sk-xxxxxxxx",
      "apiBase": "https://coding-intl.dashscope.aliyuncs.com/v1"
    }
  },
  "agents": {
    "defaults": {
      "model": "qwen3.5-plus",
      "provider": "dashscope"
    }
  }
}
```

---

## 🐛 Troubleshooting

### "Invalid API Key"
- Verify key copied correctly (no spaces)
- Check key activated in DashScope console
- Ensure account has balance

### "Model Not Found"
- Use exact name: `qwen3.5-plus` (not qwen-3.5-plus)
- Verify model available in your region

### "Connection Timeout"
- Check API base URL is correct
- Verify https (not http)
- No trailing slash in URL

### "Rate Limit Exceeded"
- Check quota in DashScope console
- Increase quota if needed
- Implement request batching

---

## ✅ Deployment Checklist

- [ ] DashScope account created
- [ ] API key generated from console
- [ ] DASHSCOPE_API_KEY configured
- [ ] DASHSCOPE_API_BASE set to coding-intl endpoint
- [ ] AI_MODEL set to qwen3.5-plus
- [ ] Repository branch: master (NOT main)
- [ ] Deploy successful
- [ ] Health check passed
- [ ] Test queries work
- [ ] Monitoring configured

---

## 🎉 Ready to Deploy!

Everything is configured for DashScope with qwen3.5-plus.

**Start here:** [DEPLOY_NOW.md](DEPLOY_NOW.md)

**Need help?** [DASHSCOPE_SETUP.md](DASHSCOPE_SETUP.md)

---

**Happy coding with Qwen! 🚀**

*Powered by Alibaba Cloud DashScope*
