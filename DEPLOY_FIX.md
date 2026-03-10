# 🚨 IMPORTANT: Deployment Fix Applied

## ✅ Issue Resolved

**Problem:** CLI import errors in deployed container  
**Solution:** Fixed imports in `clawcustom/cli/commands.py`  
**Status:** ✅ Fixed and committed to repository  

---

## 🔧 What Was Fixed

### Import Errors Fixed

**Before (Broken):**
```python
from .schema import Config
from .helpers import sync_workspace_templates
```

**After (Fixed):**
```python
from clawcustom.config.schema import Config
from clawcustom.utils.helpers import sync_workspace_templates
```

### Files Modified

1. ✅ `clawcustom/cli/commands.py` - Fixed import statements
2. ✅ `.env.coolify` - Updated with DashScope defaults
3. ✅ `docker-compose.coolify.yml` - Updated environment variables
4. ✅ `coolify.json` - Updated manifest
5. ✅ All documentation updated

---

## 🚀 Deploy to Coolify NOW

### Step 1: Push to GitHub (CRITICAL)

```bash
# In your local repository
cd /path/to/clawcustom
git add .
git commit -m "fix: CLI imports and DashScope configuration"
git push origin master
```

**⚠️ IMPORTANT:** The fix MUST be pushed to GitHub for Coolify to use it!

### Step 2: Deploy on Coolify

**Option A: Fresh Deployment**
```
1. Coolify Dashboard → + New → + New Project
2. + New → + New Service → Public Git Repository
3. Repository: https://github.com/jeccleston/clawcustom
4. Branch: master (NOT main)
5. Build Pack: Docker Compose
6. Compose File: docker-compose.coolify.yml
7. Click Save
```

**Option B: Redeploy Existing**
```
1. Go to your existing clawcustom service
2. Settings → Advanced → Pull Latest Changes
3. Click Redeploy
```

### Step 3: Configure Environment Variables

**Required:**
```bash
# DashScope API Key
DASHSCOPE_API_KEY=sk-your-dashscope-key-here

# API Base URL (Coding Plan)
DASHSCOPE_API_BASE=https://coding-intl.dashscope.aliyuncs.com/v1

# Model
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

### Step 4: Deploy & Test

```
1. Click "Deploy"
2. Wait 2-3 minutes for build
3. Open Terminal tab
4. Run: clawcustom --help
5. Run: clawcustom agent -m "help"
```

**Expected Output:**
```
clawcustom - Personal AI Assistant

Usage: clawcustom [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show version
  --help     Show this message

Commands:
  agent     Chat with the agent
  gateway   Start gateway server
  onboard   Interactive onboarding
  status    Show system status
  help      Show help information
```

---

## ✅ Verification Checklist

After deployment, verify:

- [ ] Code pushed to GitHub (master branch)
- [ ] Coolify deployment completed
- [ ] Build succeeded (no import errors)
- [ ] Health check passed
- [ ] `clawcustom --help` works
- [ ] `clawcustom agent -m "help"` works
- [ ] DashScope API key configured
- [ ] Model qwen3.5-plus active

---

## 🐛 If You Still See Errors

### "ModuleNotFoundError: No module named 'clawcustom.cli.schema'"

**Cause:** Old code still deployed  
**Solution:** 
1. Verify code pushed to GitHub
2. Check Coolify pulled latest changes
3. Force redeploy: Settings → Advanced → Rebuild

### "ModuleNotFoundError: No module named 'prompt_toolkit'"

**Cause:** Missing dependency  
**Solution:** Already included in Dockerfile, just rebuild

### "ImportError: cannot import name 'Config'"

**Cause:** Wrong import path  
**Solution:** Already fixed in commands.py, just redeploy

---

## 📞 Support

If issues persist:

1. **Check logs** in Coolify (Logs tab)
2. **Verify imports** in clawcustom/cli/commands.py
3. **Join Discord**: https://discord.gg/MnCvHqpUGB
4. **Open issue**: https://github.com/jeccleston/clawcustom/issues

---

## 📚 Documentation

- **Quick Deploy**: [DEPLOY_NOW.md](DEPLOY_NOW.md)
- **DashScope Setup**: [DASHSCOPE_SETUP.md](DASHSCOPE_SETUP.md)
- **Full Guide**: [COOLIFY_QUICK_START.md](COOLIFY_QUICK_START.md)

---

## 🎉 Ready!

**The fix is applied. Just push to GitHub and redeploy on Coolify.**

**Next Steps:**
1. `git push origin master`
2. Redeploy on Coolify
3. Test with `clawcustom agent -m "help"`

---

**Happy coding! 🚀**

*Fixed: 2026-03-09*  
*Version: 2.0.0*
