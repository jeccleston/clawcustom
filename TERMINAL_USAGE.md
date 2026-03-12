# Using ClawCustom Terminal in Coolify

Complete guide for using the interactive terminal in Coolify with ClawCustom.

---

## 🎯 Overview

Once deployed on Coolify, you can access a full terminal to interact with ClawCustom directly.

---

## 📱 Accessing the Terminal

### In Coolify Dashboard:

1. **Select your clawcustom service**
2. **Click "Terminal" tab**
3. **Click "Connect"** or **"+"** to open terminal

You now have a shell inside the ClawCustom container!

---

## 🚀 Basic Commands

### Show Help
```bash
clawcustom --help
```

### Show Status
```bash
clawcustom status
```

### Interactive Chat
```bash
clawcustom agent
```

### Single Message
```bash
clawcustom agent -m "Hello! What can you do?"
```

### Start Gateway
```bash
clawcustom gateway
```

### Onboarding (First Time)
```bash
clawcustom onboard
```

### Show Version
```bash
clawcustom --version
```

---

## ⚙️ Configuration in Terminal

### View Config
```bash
cat /root/.clawcustom/config.json
```

### Edit Config
```bash
# Using nano editor
nano /root/.clawcustom/config.json

# Using vi/vim
vi /root/.clawcustom/config.json
```

### Create Config Manually
```bash
mkdir -p /root/.clawcustom
cat > /root/.clawcustom/config.json << 'EOF'
{
  "providers": {
    "dashscope": {
      "apiKey": "sk-your-api-key-here",
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
  },
  "tools": {
    "restrictToWorkspace": true
  }
}
EOF
```

### Check Workspace
```bash
ls -la /root/.clawcustom/workspace
```

---

## 💬 Chat Commands

### Interactive Mode
```bash
clawcustom agent
```

Then type your messages:
```
> Hello! What can you do?
> use coder to build a REST API
> create python environment
> help
> exit
```

### Exit Interactive Mode
- Type: `exit` or `quit`
- Or press: `Ctrl+D` or `Ctrl+C`

---

## 🛠️ Advanced Terminal Usage

### Check Environment Variables
```bash
env | grep CLAWCUSTOM
```

### View Logs
```bash
# Current container logs
docker logs $(hostname)

# Follow logs
docker logs -f $(hostname)
```

### Check Running Processes
```bash
ps aux
```

### Check Disk Usage
```bash
df -h
```

### Check Memory
```bash
free -h
```

### Test DashScope Connection
```bash
# Simple test
clawcustom agent -m "Hello, are you working?"

# Test with specific model
CLAWCUSTOM__AGENTS__DEFAULTS__MODEL=qwen-max clawcustom agent -m "Test"
```

---

## 🐛 Troubleshooting in Terminal

### Config Not Found
```bash
# Check if config exists
ls -la /root/.clawcustom/

# Create if missing
clawcustom onboard
```

### Import Errors
```bash
# Reinstall package
pip install -e /app --force-reinstall
```

### Permission Issues
```bash
# Fix permissions
chmod -R 755 /root/.clawcustom
chown -R root:root /root/.clawcustom
```

### Check Python Path
```bash
which python
python --version
which clawcustom
```

### Test Imports
```bash
python -c "from clawcustom.cli.commands import app; print('✓ Imports work')"
```

---

## 📦 Package Management

### Check Installed Version
```bash
clawcustom --version
```

### Check Installed Packages
```bash
pip list | grep -i claw
```

### Reinstall ClawCustom
```bash
pip install -e /app --force-reinstall --no-deps
```

---

## 🔄 Service Management

### Check If Gateway Running
```bash
ps aux | grep gateway
```

### Start Gateway
```bash
clawcustom gateway
```

### Run in Background
```bash
nohup clawcustom gateway > /tmp/gateway.log 2>&1 &
```

### Check Gateway Logs
```bash
tail -f /tmp/gateway.log
```

---

## 🧪 Testing Commands

### Test All Commands
```bash
# Help
clawcustom --help

# Status
clawcustom status

# Single message
clawcustom agent -m "Test message"

# Help system
clawcustom help

# Show version
clawcustom --version
```

### Test Workers
```bash
# Coder
clawcustom agent -m "use coder to write hello world"

# Researcher
clawcustom agent -m "use researcher to find AI news"

# Writer
clawcustom agent -m "use writer to draft email"
```

### Test Docker Environments
```bash
# Create
clawcustom agent -m "create python environment"

# List
clawcustom agent -m "list environments"
```

---

## 🔧 Environment Variables

### Set Temporarily
```bash
export CLAWCUSTOM__AGENTS__DEFAULTS__MODEL=qwen-max
clawcustom agent -m "Test with qwen-max"
```

### View Current Settings
```bash
env | grep CLAWCUSTOM | sort
```

### Set for Session
```bash
# In terminal
export DASHSCOPE_API_KEY=sk-your-key
export AI_MODEL=qwen3.5-plus
export AI_PROVIDER=dashscope
```

---

## 📝 Tips for Coolify Terminal

1. **Terminal Session Timeout**
   - Coolify terminal may timeout after inactivity
   - Reconnect by clicking "Connect" again

2. **Copy/Paste**
   - Use Ctrl+Shift+C / Ctrl+Shift+V
   - Or right-click → Copy/Paste

3. **Multiple Terminals**
   - Click "+" to open multiple terminal sessions
   - Useful for running gateway in one, chatting in another

4. **Scrollback**
   - Use Shift+PageUp / Shift+PageDown
   - Or mouse wheel

5. **Clear Screen**
   ```bash
   clear
   # Or press Ctrl+L
   ```

---

## 🎯 Common Workflows

### Quick Question
```bash
clawcustom agent -m "What is the weather today?"
```

### Interactive Session
```bash
clawcustom agent
> Hello!
> Can you help me write code?
> exit
```

### Check Status Then Chat
```bash
clawcustom status
clawcustom agent -m "Show me your capabilities"
```

### Run Gateway and Monitor
```bash
# Terminal 1
clawcustom gateway

# Terminal 2 (new session)
clawcustom agent -m "Hello via gateway"
```

---

## ✅ Verification Checklist

After deploying and accessing terminal:

- [ ] Terminal connects successfully
- [ ] `clawcustom --help` works
- [ ] `clawcustom status` shows info
- [ ] `clawcustom agent -m "test"` responds
- [ ] Config directory exists
- [ ] Environment variables set
- [ ] DashScope API configured
- [ ] Can create/edit files
- [ ] No import errors

---

## 🆘 If Terminal Doesn't Work

### "command not found: clawcustom"
```bash
# Check installation
which clawcustom

# Reinstall if needed
pip install -e /app
```

### "Permission denied"
```bash
# Fix permissions
chmod +x /usr/local/bin/clawcustom
```

### "Connection refused"
```bash
# Check if container is running
docker ps

# Restart container from Coolify UI
```

### Terminal Closes Immediately
- Check container logs in Coolify
- Ensure health check passes
- Verify environment variables

---

## 📚 Additional Resources

- **Main Docs**: [README.md](README.md)
- **Deploy Guide**: [DEPLOY_NOW.md](DEPLOY_NOW.md)
- **DashScope Setup**: [DASHSCOPE_SETUP.md](DASHSCOPE_SETUP.md)
- **Coolify Guide**: [COOLIFY_QUICK_START.md](COOLIFY_QUICK_START.md)

---

**Happy terminal usage! 🚀**

*ClawCustom v2.0.0*
