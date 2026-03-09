# Renamed from nanobot to clawcustom

## Summary

All references to "nanobot" have been changed to "clawcustom" throughout the codebase.

---

## Changes Made

### 1. Directory Structure
- ✅ Renamed `nanobot/` directory to `clawcustom/`

### 2. Python Package
- ✅ Updated all imports from `nanobot.*` to `clawcustom.*`
- ✅ Changed package name in `__init__.py` files
- ✅ Updated function names (e.g., `_parse_nanobot_metadata` → `_parse_clawcustom_metadata`)
- ✅ Updated class names (e.g., `NanobotDingTalkHandler` → `ClawcustomDingTalkHandler`)

### 3. Configuration
- ✅ Updated `pyproject.toml`:
  - Package name: `nanobot-ai` → `clawcustom`
  - Version: `0.1.4.post3` → `2.0.0` (major rewrite)
  - Entry point: `nanobot` → `clawcustom`
  - Description updated for v2.0 features
  
- ✅ Updated environment variable prefix:
  - `NANOBOT_` → `CLAWCUSTOM_`
  - Example: `CLAWCUSTOM__PROVIDERS__OPENROUTER__API_KEY`

### 4. Docker Configuration
- ✅ Updated `Dockerfile`:
  - Package installation paths
  - Config directory: `/root/.nanobot` → `/root/.clawcustom`
  - Entry point: `["nanobot"]` → `["clawcustom"]`

- ✅ Updated `docker-compose.yml`:
  - Service names: `nanobot-gateway` → `clawcustom-gateway`
  - Volume paths: `~/.nanobot` → `~/.clawcustom`
  - Container names

- ✅ Updated `docker-compose.coolify.yml`:
  - All nanobot references → clawcustom

### 5. Documentation
- ✅ Updated all Markdown files:
  - README.md
  - MODULAR_SYSTEM.md
  - COOLIFY_DEPLOY.md
  - WORKER_AGENTS.md
  - All other documentation

- ✅ Updated comments and docstrings in code

### 6. CLI Commands

**Old:**
```bash
nanobot onboard
nanobot agent
nanobot gateway
nanobot status
```

**New:**
```bash
clawcustom onboard
clawcustom agent
clawcustom gateway
clawcustom status
```

### 7. Default Config Paths

**Old:** `~/.nanobot/`
**New:** `~/.clawcustom/`

Files:
- `~/.clawcustom/config.json`
- `~/.clawcustom/workspace/`
- `~/.clawcustom/sessions/`

---

## Migration Guide

### For Existing Users

1. **Uninstall old version:**
   ```bash
   pip uninstall nanobot-ai
   ```

2. **Install new version:**
   ```bash
   pip install -e .
   ```

3. **Migrate config (optional):**
   ```bash
   # Backup old config
   cp -r ~/.nanobot ~/.nanobot.backup
   
   # Copy to new location (or let it create fresh)
   cp -r ~/.nanobot ~/.clawcustom
   ```

4. **Update environment variables:**
   ```bash
   # Old
   export NANOBOT__PROVIDERS__OPENROUTER__API_KEY=xxx
   
   # New
   export CLAWCUSTOM__PROVIDERS__OPENROUTER__API_KEY=xxx
   ```

5. **Update Docker commands:**
   ```bash
   # Old
   docker run -v ~/.nanobot:/root/.nanobot nanobot gateway
   
   # New
   docker run -v ~/.clawcustom:/root/.clawcustom clawcustom gateway
   ```

---

## Breaking Changes

### API Changes

| Old | New |
|-----|-----|
| `from nanobot.agent import ...` | `from clawcustom.agent import ...` |
| `NanobotDingTalkHandler` | `ClawcustomDingTalkHandler` |
| `env_prefix="NANOBOT_"` | `env_prefix="CLAWCUSTOM_"` |

### Config Changes

All environment variables now use `CLAWCUSTOM_` prefix instead of `NANOBOT_`.

### Path Changes

Default config directory changed from `~/.nanobot/` to `~/.clawcustom/`.

---

## What's New in v2.0

Besides the rename, ClawCustom v2.0 includes:

- ✨ **Plugin System** - Modular architecture
- 🤖 **Worker Agents 2.0** - YAML-based worker definitions
- 🐳 **Docker Environments** - Full-stack development sandboxes
- 👤 **Onboarding** - Interactive setup wizard
- 📚 **Help System** - Context-aware assistance

---

## Verification

To verify the rename was successful:

```bash
# Check package name
python -c "import clawcustom; print(clawcustom.__name__)"

# Check CLI
clawcustom --version

# Check no nanobot references remain
grep -r "nanobot" clawcustom/ --include="*.py"
# Should return empty or only historical references
```

---

## Testing Checklist

- [ ] `clawcustom onboard` works
- [ ] `clawcustom agent -m "help"` works
- [ ] `clawcustom gateway` starts
- [ ] `clawcustom status` shows info
- [ ] Worker spawning works
- [ ] Docker environments work
- [ ] Plugins load correctly
- [ ] Config is read from `~/.clawcustom/`

---

**Rename completed successfully! 🎉**

All nanobot references have been changed to clawcustom.
