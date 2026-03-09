# Modular Agent System v2.0

Complete rewrite of ClawCustom with a modular, plugin-based architecture.

---

## 🎯 What's New

### ✨ Plugin System

Everything is now a plugin! Easy to add, remove, and customize.

- **BasePlugin** - Abstract base class all plugins inherit from
- **PluginRegistry** - Central management for all plugins
- **PluginLoader** - Dynamic discovery and loading
- **YAML Configuration** - Workers and tools defined in YAML

### 🤖 Worker Agents 2.0

Completely redesigned worker system with YAML definitions.

**7 Specialized Workers:**
- 🤖 Coder - Software development
- 📚 Researcher - Information gathering
- ✍️ Writer - Content creation
- 📊 Analyst - Data analysis
- 🔍 Reviewer - Code review
- 🏗️ Architect - System design
- 🛠️ DevOps - Infrastructure

**Easy to Add New Workers:**
```yaml
# nanobot/plugins/workers/your-worker/worker.yaml
name: your-worker
type: your_worker
description: What your worker does

system_prompt: |
  Your custom system prompt here...

tools:
  - read_file
  - write_file
  - exec

parameters:
  max_iterations: 25
  temperature: 0.1
  max_tokens: 6144
```

That's it! The system auto-discovers and registers.

### 🐳 Docker Environment Management

Full-stack development environments managed by agents.

**Pre-built Templates:**
- `python` - Python 3.11
- `nodejs` - Node.js 20
- `python-postgres` - Python + PostgreSQL
- `fullstack-react` - React + Node + PostgreSQL
- `fastapi` - FastAPI + PostgreSQL + Redis
- `nodejs-mongo` - Node.js + MongoDB
- `nextjs` - Next.js + PostgreSQL
- `ml-gpu` - TensorFlow + Jupyter + GPU

**Agent Workflow:**
```
User: "Build a REST API for user management"

Agent:
1. Analyzes requirements
2. Creates appropriate environment (python-postgres)
3. Installs dependencies
4. Implements the API
5. Writes tests
6. Documents
7. Shows result: http://localhost:8000
```

### 👤 User-Friendly Features

**Interactive Onboarding:**
- Guided setup process
- Choose your use case
- Select preferred channels
- Configure LLM provider
- API key setup

**Context-Aware Help:**
- `help` - General help
- `help workers` - Worker info
- `help environments` - Docker environments
- `help commands` - Command reference
- `help troubleshooting` - Fix common issues

**Natural Language Commands:**
```
"use coder to build an API" → Spawns coder worker
"create python environment" → Creates Python env
"show me AAPL stock price" → Gets stock info
```

---

## 🏗️ Architecture

```
┌────────────────────────────────────────────────────────────┐
│                      MAIN BOT                               │
├────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Core       │  │   Agent      │  │   Plugin     │     │
│  │   Engine     │  │   Manager    │  │   Loader     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│         │                 │                 │               │
│         ▼                 ▼                 ▼               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Modular Agent System                   │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │   │
│  │  │  Coder  │ │Research │ │  DevOps │ │ Analyst │   │   │
│  │  │  Agent  │ │  Agent  │ │  Agent  │ │  Agent  │   │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         Tool Registry (Dynamic from Plugins)        │   │
│  │  Files │ Shell │ Docker │ Stocks │ Docs │ Web │...  │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────┘
```

---

## 📁 New Directory Structure

```
clawcustom/
├── nanobot/
│   ├── plugins/                    # NEW: Plugin system
│   │   ├── __init__.py
│   │   ├── base.py                # BasePlugin class
│   │   ├── registry.py            # Plugin registry
│   │   ├── loader.py              # Dynamic loader
│   │   │
│   │   ├── workers/               # Worker plugins
│   │   │   ├── __init__.py
│   │   │   ├── coder/
│   │   │   │   ├── __init__.py
│   │   │   │   └── worker.yaml   # YAML definition
│   │   │   ├── researcher/
│   │   │   ├── writer/
│   │   │   ├── analyst/
│   │   │   ├── reviewer/
│   │   │   ├── architect/
│   │   │   └── devops/
│   │   │
│   │   └── docker/                # Docker plugin
│   │       ├── __init__.py
│   │       ├── tools.py
│   │       └── templates/         # Docker templates
│   │           ├── python.yml
│   │           ├── nodejs.yml
│   │           └── ...
│   │
│   ├── agent/
│   │   ├── loop.py               # Updated with plugin loading
│   │   ├── worker.py             # Worker agent manager
│   │   └── tools/
│   │       └── spawn_worker.py   # Worker spawning tool
│   │
│   └── cli/
│       ├── onboarding.py         # NEW: Interactive onboarding
│       └── help_system.py        # NEW: Help system
│
└── ...
```

---

## 🚀 Quick Start

### 1. Install

```bash
pip install -e .
```

### 2. Onboard (New!)

```bash
nanobot onboard
```

Follow the interactive setup:
- Set your name
- Choose use case
- Select chat channel
- Configure LLM provider

### 3. Use

```bash
# Get help
nanobot agent -m "help"

# Spawn a worker
nanobot agent -m "use coder to build a REST API with FastAPI"

# Create environment
nanobot agent -m "create python environment"

# List environments
nanobot agent -m "list environments"
```

---

## 💡 Usage Examples

### Workers

```bash
# Coder
"use coder to create a Python module for CSV parsing"
"use coder to fix the bug in auth.py"

# Researcher
"use researcher to analyze the AI assistant market"
"use researcher to find best practices for OAuth2"

# Writer
"use writer to create API documentation"
"use writer to draft a blog post about our product"

# Analyst
"use analyst to review Q4 sales data"
"use analyst to compare AAPL, GOOGL, MSFT"

# Reviewer
"use reviewer to audit the authentication module"
"use reviewer to check for security vulnerabilities"

# Architect
"use architect to design microservices architecture"
"use architect to plan database schema"

# DevOps
"use devops to create CI/CD pipeline"
"use devops to set up Docker Compose"
```

### Environments

```bash
# Create
"create python environment"
"create fullstack environment named my-app"

# List
"list environments"
"show all environments"

# Execute
"exec in my-app 'npm install'"
"exec in my-app 'python main.py'"

# Manage
"stop environment my-app"
"destroy environment my-app"
```

### Multi-Worker Workflow

```
User: "Build a complete e-commerce platform"

Agent spawns:
1. Researcher → Market research
2. Architect → System design
3. DevOps → Environment setup
4. Coder → Implementation
5. Reviewer → Code review
6. Writer → Documentation
```

---

## 🔧 Adding New Features

### Create a New Worker

**1. Create directory:**
```bash
mkdir -p nanobot/plugins/workers/qa-tester
```

**2. Create worker.yaml:**
```yaml
name: qa-tester
type: qa_tester
description: Quality assurance and testing specialist

system_prompt: |
  You are an expert QA engineer specializing in testing...
  
  Responsibilities:
  - Write comprehensive tests
  - Perform manual testing
  - Document bugs
  - Ensure quality standards

tools:
  - read_file
  - write_file
  - exec
  - web_search

parameters:
  max_iterations: 25
  temperature: 0.1
  max_tokens: 6144
```

**3. (Optional) Create skill.md:**
```markdown
# QA Tester Skill

Detailed instructions for the QA tester worker...
```

**Done!** The worker is auto-discovered and available.

### Create a New Plugin

**1. Create directory:**
```bash
mkdir -p nanobot/plugins/your-plugin
```

**2. Create __init__.py:**
```python
"""Your plugin description."""

from nanobot.plugins.base import BasePlugin
from nanobot.agent.tools.base import Tool
from typing import Any

class YourPluginPlugin(BasePlugin):
    name = "your-plugin"
    version = "1.0.0"
    description = "What your plugin does"
    
    async def on_load(self) -> None:
        """Initialize plugin."""
        pass
    
    def get_tools(self) -> list[Tool]:
        """Return tools provided by plugin."""
        return []
    
    def get_skills(self) -> list[str]:
        """Return skills provided by plugin."""
        return []
    
    def get_config_schema(self) -> dict[str, Any]:
        """Return configuration schema."""
        return {}
```

**Done!** Enable in config.

---

## ⚙️ Configuration

### Enable/Disable Plugins

```yaml
# ~/.nanobot/config.yaml

plugins:
  enabled:
    - workers
    - docker
    - stock
  
  settings:
    workers:
      default_worker: coder
      max_concurrent: 5
    
    docker:
      auto_cleanup: true
      max_environments: 5
```

### Worker Configuration

```yaml
plugins:
  settings:
    workers:
      coder:
        max_iterations: 30
        temperature: 0.1
      
      researcher:
        max_iterations: 25
        temperature: 0.2
```

---

## 📊 Plugin System Details

### Lifecycle Hooks

```python
class MyPlugin(BasePlugin):
    async def on_load(self) -> None:
        """Called when plugin is loaded."""
        pass
    
    async def on_unload(self) -> None:
        """Called when plugin is unloaded."""
        pass
    
    async def on_enable(self) -> None:
        """Called when plugin is enabled."""
        self.enabled = True
    
    async def on_disable(self) -> None:
        """Called when plugin is disabled."""
        self.enabled = False
```

### Required Methods

```python
def get_tools(self) -> list[Tool]:
    """Return list of tools."""
    return []

def get_skills(self) -> list[str]:
    """Return list of skills."""
    return []

def get_config_schema(self) -> dict:
    """Return JSON schema for config."""
    return {}
```

---

## 🎓 Advanced Features

### Environment-Aware Agents

Workers can now create and manage their own environments:

```python
# Worker automatically creates environment
class CoderWorker(WorkerAgent):
    async def execute_task(self, task: str) -> str:
        # 1. Analyze task requirements
        # 2. Create environment if needed
        env = await self.docker.create_environment(
            template="python-postgres",
            name="task-env"
        )
        
        # 3. Work in environment
        await self.docker.execute_in_environment(
            env.id,
            "pip install fastapi"
        )
        
        # 4. Implement feature
        # ...
        
        # 5. Return result
        return result
```

### Plugin Discovery

Plugins are auto-discovered:

```python
# Plugin loader scans nanobot/plugins/
# Any directory with __init__.py is a plugin
# Plugin class must inherit from BasePlugin
```

---

## 📝 Migration Guide

### From Old Worker System

**Old way:**
```python
# Hardcoded in worker.py
WORKER_CONFIGS = {
    WorkerType.CODER: WorkerConfig(...)
}
```

**New way:**
```yaml
# nanobot/plugins/workers/coder/worker.yaml
name: coder
type: coder
system_prompt: |
  ...
```

### Benefits

- ✅ Easy to add workers (just YAML)
- ✅ No code changes needed
- ✅ Auto-discovery
- ✅ Configurable per-worker
- ✅ Version controlled

---

## 🤝 Contributing

### Adding Plugins

1. Create plugin in `nanobot/plugins/`
2. Inherit from `BasePlugin`
3. Implement required methods
4. Test locally
5. Submit PR

### Best Practices

- **Single Responsibility** - Each plugin does one thing well
- **Clear Interfaces** - Well-defined tool APIs
- **Documentation** - Include README for complex plugins
- **Testing** - Unit tests for plugins
- **Versioning** - Semantic versioning for plugins

---

## 📖 Documentation

- **PLUGIN_SYSTEM.md** - Plugin development guide
- **WORKER_AGENTS.md** - Worker system details
- **DOCKER_ENVIRONMENTS.md** - Environment management
- **ONBOARDING.md** - Setup guide
- **HELP_SYSTEM.md** - Help topics

---

## ✅ What's Implemented

- [x] Plugin system foundation
- [x] Worker plugins with YAML
- [x] Docker environment plugin
- [x] Interactive onboarding
- [x] Context-aware help system
- [x] Agent integration
- [x] 8 Docker templates
- [x] 7 specialized workers
- [x] Documentation

---

**ClawCustom v2.0 - Modular, Extensible, User-Friendly**

Built with ❤️ for the community!
