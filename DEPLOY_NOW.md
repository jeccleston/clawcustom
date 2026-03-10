# 🚀 Deploy ClawCustom to Coolify - INSTANT START

**Repository:** https://github.com/jeccleston/clawcustom  
**Branch:** `master`  
**Deploy Time:** 5 minutes  

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
Branch: master
Build Pack: Docker Compose
Compose File: docker-compose.coolify.yml
```

### 3. Environment Variables (Copy-Paste)
```bash
OPENROUTER_API_KEY=sk-or-v1-your-key-here
AI_MODEL=anthropic/claude-opus-4-5
AI_PROVIDER=auto
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

---

## ✅ Success Checklist

- [ ] Repository: https://github.com/jeccleston/clawcustom
- [ ] Branch: **master** (NOT main)
- [ ] Compose file: docker-compose.coolify.yml
- [ ] API key set (OPENROUTER_API_KEY or ANTHROPIC_API_KEY)
- [ ] Deploy completed
- [ ] Health check passed
- [ ] Test command works

---

## 🐛 Common Issues

### "Remote branch main not found"
**Solution:** Use branch **`master`** (not main)

### "No API key found"
**Solution:** Set `OPENROUTER_API_KEY` or `ANTHROPIC_API_KEY`

### "Health check failed"
**Solution:** Wait 5 minutes, check API key is valid

---

## 📚 Full Guides

- **Quick Start:** [COOLIFY_QUICK_START.md](COOLIFY_QUICK_START.md)
- **Setup Guide:** [COOLIFY_SETUP.md](COOLIFY_SETUP.md)
- **Deployment:** [COOLIFY_DEPLOY.md](COOLIFY_DEPLOY.md)
- **Ready Check:** [COOLIFY_READY.md](COOLIFY_READY.md)

---

## 🆘 Support

- Discord: https://discord.gg/MnCvHqpUGB
- Issues: https://github.com/jeccleston/clawcustom/issues

---

**Ready to deploy! Use branch `master`** 🚀
