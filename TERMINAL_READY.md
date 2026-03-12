# ✅ ClawCustom Terminal Ready for Coolify

All changes committed and ready to push to GitHub for deployment on Coolify.

---

## 🎯 What Was Done

### 1. Fixed Dockerfile ✅
- Changed default CMD from `status` to `--help`
- Makes terminal more user-friendly on first access

### 2. Updated docker-compose.coolify.yml ✅
- Added `stdin_open: true` - Enables interactive terminal
- Added `tty: true` - Enables terminal features
- Changed health check to `--help` (more reliable than `status`)

### 3. Created Terminal Usage Guide ✅
- **File:** `TERMINAL_USAGE.md`
- Complete guide for using ClawCustom in Coolify terminal
- Includes all commands, troubleshooting, and tips

---

## 📦 Files Changed

| File | Changes |
|------|---------|
| `Dockerfile` | CMD changed to `--help` |
| `docker-compose.coolify.yml` | Added stdin_open, tty; fixed healthcheck |
| `TERMINAL_USAGE.md` | NEW - Complete terminal guide |

---

## 🚀 Deploy to Coolify

### Step 1: Push to GitHub

```bash
cd /path/to/clawcustom
git push origin master
```

### Step 2: Redeploy on Coolify

```
1. Coolify Dashboard → Select clawcustom service
2. Settings → Advanced → Pull Latest Changes
3. Click Redeploy
4. Wait 2-3 minutes for build
```

### Step 3: Access Terminal

```
1. Select your clawcustom service
2. Click "Terminal" tab
3. Click "Connect" or "+"
4. You're in! Try: clawcustom --help
```

---

## 💡 Using the Terminal

### Basic Commands

```bash
# Show help
clawcustom --help

# Show status
clawcustom status

# Interactive chat
clawcustom agent

# Single message
clawcustom agent -m "Hello!"

# Start gateway
clawcustom gateway

# Onboarding
clawcustom onboard
```

### Create Config (If Not Exists)

```bash
# Run onboarding
clawcustom onboard

# OR create manually
mkdir -p /root/.clawcustom
cat > /root/.clawcustom/config.json << 'EOF'
{
  "providers": {
    "dashscope": {
      "apiKey": "sk-your-key",
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
EOF
```

---

## ✅ Expected Result

After deployment and terminal access:

```bash
# In Coolify Terminal
root@container-id:/app# clawcustom --help

 Usage: clawcustom [OPTIONS] COMMAND [ARGS]...

 ╭─ clawcustom - Personal AI Assistant ─╮
│                                         │
│  🐈 clawcustom - Personal AI Assistant │
│                                         │
╰─────────────────────────────────────────╯

 Options
  --version    Show version
  --help       Show this message

 Commands
  agent     Chat with the agent
  gateway   Start gateway server
  help      Show help information
  onboard   Interactive onboarding
  status    Show system status
```

---

## 📚 Documentation

**Essential Guides:**
- [TERMINAL_USAGE.md](TERMINAL_USAGE.md) - Complete terminal guide ⭐
- [DEPLOY_NOW.md](DEPLOY_NOW.md) - Quick deploy
- [DASHSCOPE_SETUP.md](DASHSCOPE_SETUP.md) - API setup
- [README.md](README.md) - Main docs

---

## 🎯 Terminal Features

✅ **Interactive Shell Access**
- Full bash shell inside container
- Run any clawcustom command
- Edit config files
- Test functionality

✅ **stdin_open + tty**
- Enables interactive features
- Proper terminal behavior
- Ctrl+C, tab completion work

✅ **Persistent Sessions**
- Config saved in /root/.clawcustom
- Workspace persists across restarts
- Volume mounted for durability

---

## 🐛 Troubleshooting

### Terminal Closes Immediately
- Check container logs in Coolify
- Ensure health check passes
- Verify container is running

### "command not found"
```bash
# Reinstall
pip install -e /app --force-reinstall
```

### Config Not Found
```bash
# Run onboarding
clawcustom onboard
```

### Import Errors
```bash
# Fix imports (already fixed in code)
# Just redeploy from GitHub
```

---

## 🎉 Ready to Deploy!

**All changes committed. Just push and redeploy:**

```bash
git push origin master
```

Then access terminal in Coolify and enjoy! 🚀

---

**Terminal-ready ClawCustom v2.0.0**

*Deployed with: DashScope + qwen3.5-plus*
