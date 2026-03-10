# DashScope Setup Guide for ClawCustom

Complete guide for configuring Alibaba Cloud DashScope (Qwen models) with ClawCustom.

---

## 🎯 Overview

**ClawCustom** is optimized for **Alibaba Cloud DashScope** Qwen models, providing excellent performance for coding tasks with competitive pricing.

**Recommended Model:** `qwen3.5-plus` - Best balance of performance and cost

---

## 📋 Prerequisites

- Alibaba Cloud account (https://www.aliyun.com)
- DashScope access enabled
- API key generated

---

## 🔑 Step 1: Get DashScope API Key

### 1.1 Create/Login to Alibaba Cloud

1. Visit: https://www.aliyun.com
2. Click **"Sign In"** or **"Free Account"**
3. Complete registration/verification

### 1.2 Access DashScope Console

1. Go to: https://dashscope.console.aliyun.com
2. If prompted, enable DashScope service
3. Navigate to **"API-KEY Management"** in left sidebar

### 1.3 Create API Key

1. Click **"Create New API Key"**
2. Copy the generated key immediately
3. Store it securely (you can't view it again)

**Your API key looks like:** `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

## ⚙️ Step 2: Configure ClawCustom

### For Coolify Deployment

In Coolify's **Environment Variables** tab, add:

```bash
# Required: DashScope API Key
DASHSCOPE_API_KEY=sk-your-actual-key-here

# API Base URL (Coding Plan endpoint)
DASHSCOPE_API_BASE=https://coding-intl.dashscope.aliyuncs.com/v1

# Model Configuration
AI_MODEL=qwen3.5-plus
AI_PROVIDER=dashscope
```

### For Local Deployment

Edit `~/.clawcustom/config.json`:

```json
{
  "providers": {
    "dashscope": {
      "apiKey": "sk-your-actual-key-here",
      "apiBase": "https://coding-intl.dashscope.aliyuncs.com/v1"
    }
  },
  "agents": {
    "defaults": {
      "model": "qwen3.5-plus",
      "provider": "dashscope",
      "temperature": 0.1,
      "max_tokens": 8192
    }
  }
}
```

Or use environment variables:

```bash
export CLAWCUSTOM__PROVIDERS__DASHSCOPE__API_KEY=sk-your-key
export CLAWCUSTOM__PROVIDERS__DASHSCOPE__API_BASE=https://coding-intl.dashscope.aliyuncs.com/v1
export CLAWCUSTOM__AGENTS__DEFAULTS__MODEL=qwen3.5-plus
export CLAWCUSTOM__AGENTS__DEFAULTS__PROVIDER=dashscope
```

---

## 🤖 Step 3: Choose Your Qwen Model

### Available Models

| Model | Context | Best For | Price (¥/1K tokens) |
|-------|---------|----------|---------------------|
| **qwen3.5-plus** ⭐ | 256K | **Balanced performance/cost** | ~¥0.02 |
| qwen-max | 256K | Complex reasoning, coding | ~¥0.04 |
| qwen-plus | 256K | General purpose | ~¥0.015 |
| qwen-turbo | 256K | Simple tasks, speed | ~¥0.008 |
| qwen-2.5-72b-instruct | 128K | Open-source preference | ~¥0.012 |

### Recommendations

**For Coding Tasks:**
- `qwen3.5-plus` - Best overall for coding (recommended)
- `qwen-max` - Most powerful for complex architectures

**For General Chat:**
- `qwen-plus` - Good balance
- `qwen-turbo` - Fast responses, lower cost

**For Chinese Language:**
- All Qwen models excel at Chinese
- `qwen3.5-plus` recommended for bilingual use

---

## 🧪 Step 4: Test Configuration

### Quick Test

```bash
# Deploy and access terminal
docker exec -it <container> clawcustom agent -m "你好！请用中文介绍你自己"

# Expected response in Chinese
```

### Full Test

```bash
# Test coding capability
clawcustom agent -m "use coder to create a Python function that sorts a list"

# Test reasoning
clawcustom agent -m "Explain quantum computing in simple terms"

# Test Chinese language
clawcustom agent -m "写一篇关于人工智能的短文"
```

---

## 💰 Pricing Information

### DashScope Pricing (Approximate)

**qwen3.5-plus:**
- Input: ¥0.02 / 1K tokens
- Output: ¥0.06 / 1K tokens
- **~$0.003 USD / 1K tokens**

**qwen-max:**
- Input: ¥0.04 / 1K tokens
- Output: ¥0.12 / 1K tokens
- **~$0.006 USD / 1K tokens**

**qwen-turbo:**
- Input: ¥0.008 / 1K tokens
- Output: ¥0.024 / 1K tokens
- **~$0.001 USD / 1K tokens**

### Cost Estimation

**Typical usage (100 conversations/day):**
- qwen3.5-plus: ~$5-15/month
- qwen-max: ~$10-30/month
- qwen-turbo: ~$2-5/month

**For comparison:**
- Claude-3.5-Sonnet (via OpenRouter): ~$15-40/month
- GPT-4o: ~$20-50/month

---

## 🔧 Step 5: Advanced Configuration

### Using Coding Plan Endpoint

The coding-intl endpoint is optimized for coding tasks:

```bash
# Environment variable
DASHSCOPE_API_BASE=https://coding-intl.dashscope.aliyuncs.com/v1

# Or in config.json
{
  "providers": {
    "dashscope": {
      "apiBase": "https://coding-intl.dashscope.aliyuncs.com/v1"
    }
  }
}
```

### Switching Models

**Via Environment Variable:**
```bash
# Quick switch to qwen-max for complex tasks
export AI_MODEL=qwen-max

# Switch back
export AI_MODEL=qwen3.5-plus
```

**Via Config File:**
```json
{
  "agents": {
    "defaults": {
      "model": "qwen-max"
    }
  }
}
```

### Alternative Providers

You can keep other providers as backup:

```bash
# Primary: DashScope
DASHSCOPE_API_KEY=sk-dashscope-key
AI_MODEL=qwen3.5-plus
AI_PROVIDER=dashscope

# Backup: OpenRouter (optional)
OPENROUTER_API_KEY=sk-or-key

# Backup: Anthropic (optional)
ANTHROPIC_API_KEY=sk-ant-key
```

The system will use DashScope by default, but you can switch providers in config if needed.

---

## 🐛 Troubleshooting

### "Invalid API Key" Error

**Solutions:**
1. Verify API key is copied correctly (no extra spaces)
2. Check API key is activated in DashScope console
3. Ensure account has sufficient balance
4. Try regenerating the API key

### "Model Not Found" Error

**Solutions:**
1. Verify model name: `qwen3.5-plus` (not `qwen-3.5-plus`)
2. Check model is available in your region
3. Ensure model is enabled for your account
4. Try alternative: `qwen-max` or `qwen-plus`

### "API Base URL" Error

**Solutions:**
1. Verify URL: `https://coding-intl.dashscope.aliyuncs.com/v1`
2. Check for typos (https, not http)
3. Ensure no trailing slashes
4. Try standard endpoint: `https://dashscope.aliyuncs.com/api/v1`

### Slow Response Times

**Solutions:**
1. Switch to `qwen-turbo` for faster responses
2. Reduce `AI_MAX_TOKENS` to limit response length
3. Check network connection to Alibaba Cloud
4. Use CDN or closer region if available

### Rate Limit Errors

**Solutions:**
1. Check your quota in DashScope console
2. Increase quota if needed
3. Implement request batching
4. Add retry logic with exponential backoff

---

## 📊 Performance Benchmarks

### Qwen Model Performance (Approximate)

| Model | Speed (tokens/s) | Coding Score | Reasoning Score |
|-------|-----------------|--------------|-----------------|
| qwen-max | ~50 | 95/100 | 95/100 |
| qwen3.5-plus | ~80 | 90/100 | 88/100 |
| qwen-plus | ~100 | 85/100 | 82/100 |
| qwen-turbo | ~150 | 75/100 | 70/100 |

### Comparison with Other Providers

| Provider/Model | Coding | Chinese | Cost |
|---------------|--------|---------|------|
| **Qwen3.5-Plus** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $ |
| Claude-3.5-Sonnet | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | $$$ |
| GPT-4o | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | $$$ |
| DeepSeek-V3 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $ |

**Best Value:** qwen3.5-plus for coding + Chinese tasks

---

## 🔒 Security Best Practices

### API Key Security

1. **Never commit API keys to Git**
   ```bash
   # Add to .gitignore
   echo ".env" >> .gitignore
   echo "*.key" >> .gitignore
   ```

2. **Use environment variables**
   ```bash
   # Better than config files
   export DASHSCOPE_API_KEY=xxx
   ```

3. **Rotate keys regularly**
   - Regenerate API key every 90 days
   - Delete unused keys immediately

4. **Use separate keys for environments**
   - Development key
   - Staging key
   - Production key

### Access Control

1. **Enable API key restrictions**
   - IP whitelist in DashScope console
   - Referer restrictions
   - Usage quotas

2. **Monitor usage**
   - Set up billing alerts
   - Monitor API calls in console
   - Review logs regularly

---

## 📚 Resources

### Official Documentation

- **DashScope Console:** https://dashscope.console.aliyun.com
- **API Docs:** https://help.aliyun.com/zh/dashscope/
- **Pricing:** https://www.aliyun.com/price/product
- **Models:** https://help.aliyun.com/zh/dashscope/models

### Community

- **Discord:** https://discord.gg/MnCvHqpUGB
- **GitHub:** https://github.com/jeccleston/clawcustom
- **Issues:** https://github.com/jeccleston/clawcustom/issues

### Tutorials

- **Getting Started:** https://help.aliyun.com/zh/dashscope/quick-start
- **Best Practices:** https://help.aliyun.com/zh/dashscope/best-practices
- **FAQ:** https://help.aliyun.com/zh/dashscope/faq

---

## ✅ Setup Checklist

- [ ] Alibaba Cloud account created
- [ ] DashScope service enabled
- [ ] API key generated and copied
- [ ] Environment variables configured
- [ ] Model selected (qwen3.5-plus recommended)
- [ ] API base URL set (coding-intl endpoint)
- [ ] Test query successful
- [ ] Monitoring/alerts configured
- [ ] Security best practices implemented

---

## 🎉 Next Steps

1. **Test with workers:**
   ```bash
   clawcustom agent -m "use coder to build a REST API"
   ```

2. **Create Docker environment:**
   ```bash
   clawcustom agent -m "create python environment"
   ```

3. **Enable chat channels:**
   - Telegram, Discord, or WhatsApp

4. **Join community:**
   - Discord: https://discord.gg/MnCvHqpUGB

---

**Happy coding with Qwen! 🚀**

*Last Updated: 2026-03-09*  
*Version: 2.0.0*
