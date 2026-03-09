# Worker Agent System

Specialized AI agents optimized for specific task domains.

## Overview

The worker agent system allows you to spawn specialized agents with domain-specific expertise, optimized tools, and tailored system prompts. Each worker type is fine-tuned for its specialty.

## Worker Types

| Type | Specialty | Best For |
|------|-----------|----------|
| **coder** | Software development | Building features, bug fixes, refactoring, tests |
| **researcher** | Information gathering | Market research, competitive analysis, fact-finding |
| **writer** | Content creation | Documentation, articles, emails, guides |
| **analyst** | Data analysis | Financial analysis, metrics, trends, insights |
| **reviewer** | Code review | QA, security audit, best practices |
| **architect** | System design | Architecture, APIs, databases, patterns |
| **devops** | Infrastructure | Docker, CI/CD, deployment, monitoring |

## Usage

### Basic Example

```python
# Via CLI
nanobot agent -m "Spawn a coder worker to build a REST API for user management"

# The agent will use spawn_worker tool:
spawn_worker(
    task="Build a REST API with FastAPI for user management including CRUD operations, authentication, and validation",
    worker_type="coder",
    label="User Management API"
)
```

### Worker Tool Parameters

```json
{
  "task": "Detailed description of what needs to be done",
  "worker_type": "coder|researcher|writer|analyst|reviewer|architect|devops",
  "label": "Short descriptive name for tracking"
}
```

## Worker Specifications

### Coder

**Specialty:** Software development, debugging, testing

**Tools:**
- File operations (read, write, edit, list)
- Shell execution
- Web search (documentation)
- Web fetch (API docs, examples)

**Configuration:**
- Max iterations: 30
- Temperature: 0.1 (focused, deterministic)
- Max tokens: 8192

**Example Tasks:**
- "Create a Python module to parse and validate CSV files"
- "Implement JWT authentication middleware for Express.js"
- "Fix the race condition in the database connection pool"
- "Write unit tests for the payment processing service"

### Researcher

**Specialty:** Information gathering, analysis, synthesis

**Tools:**
- Web search (extensive)
- Web fetch (deep content extraction)
- File operations (reports)

**Configuration:**
- Max iterations: 25
- Temperature: 0.2 (slightly creative)
- Max tokens: 6144

**Example Tasks:**
- "Research top 5 competitors in the AI assistant market"
- "Find best practices for implementing OAuth2 in microservices"
- "Gather information on GDPR compliance requirements for chatbots"
- "Compare pricing and features of major cloud providers"

### Writer

**Specialty:** Content creation, documentation, communication

**Tools:**
- File operations
- Web fetch (reference material)

**Configuration:**
- Max iterations: 20
- Temperature: 0.3 (more creative)
- Max tokens: 6144

**Example Tasks:**
- "Write API documentation for the user authentication endpoints"
- "Create a user guide for the new feature release"
- "Draft an email announcing the product update to customers"
- "Write a blog post about our technical architecture"

### Analyst

**Specialty:** Data analysis, financial modeling, insights

**Tools:**
- File operations (data files)
- Shell execution (data processing)
- Stock analysis tools
- Web search (market data)

**Configuration:**
- Max iterations: 25
- Temperature: 0.1 (focused)
- Max tokens: 6144

**Example Tasks:**
- "Analyze Q4 sales data and identify trends and opportunities"
- "Review the stock portfolio performance and suggest rebalancing"
- "Calculate customer lifetime value from the provided dataset"
- "Create a financial model for the new product launch"

### Reviewer

**Specialty:** Code review, security, quality assurance

**Tools:**
- File operations (read-only focus)
- Web search (security best practices)
- Shell execution (linting, testing)

**Configuration:**
- Max iterations: 20
- Temperature: 0.1 (critical, focused)
- Max tokens: 6144

**Example Tasks:**
- "Review the authentication module for security vulnerabilities"
- "Audit the codebase for potential performance bottlenecks"
- "Check if the API follows REST best practices"
- "Review error handling and logging across the application"

### Architect

**Specialty:** System design, patterns, scalability

**Tools:**
- File operations
- Web search (patterns, best practices)
- Web fetch (reference architectures)

**Configuration:**
- Max iterations: 25
- Temperature: 0.2 (balanced)
- Max tokens: 8192

**Example Tasks:**
- "Design a microservices architecture for an e-commerce platform"
- "Create a database schema for a multi-tenant SaaS application"
- "Plan the API design for a real-time collaboration tool"
- "Design a caching strategy for high-traffic endpoints"

### DevOps

**Specialty:** Infrastructure, automation, deployment

**Tools:**
- Shell execution (Docker, kubectl, etc.)
- File operations (config files)
- Web search (latest practices)

**Configuration:**
- Max iterations: 25
- Temperature: 0.1 (precise)
- Max tokens: 6144

**Example Tasks:**
- "Create a CI/CD pipeline for deploying to Kubernetes"
- "Set up Docker Compose for local development environment"
- "Configure monitoring and alerting for the production cluster"
- "Implement infrastructure as code using Terraform"

## Multi-Worker Workflows

Complex projects can use multiple specialized workers in sequence:

### Example: New Feature Development

```
1. researcher → Market research and requirements gathering
   spawn_worker(task="Research user needs for project management features", 
                worker_type="researcher", label="PM Research")

2. architect → System design
   spawn_worker(task="Design architecture for project management module",
                worker_type="architect", label="PM Architecture")

3. coder → Implementation
   spawn_worker(task="Implement project management API endpoints",
                worker_type="coder", label="PM API Development")

4. reviewer → Quality check
   spawn_worker(task="Code review of project management module",
                worker_type="reviewer", label="PM Code Review")

5. writer → Documentation
   spawn_worker(task="Write API documentation for PM module",
                worker_type="writer", label="PM Documentation")
```

## Best Practices

### 1. Choose the Right Worker

Match worker type to primary task:
- Building features → `coder`
- Gathering information → `researcher`
- Writing content → `writer`
- Analyzing data → `analyst`
- Reviewing code → `reviewer`
- Designing systems → `architect`
- Setting up infra → `devops`

### 2. Write Clear Tasks

Be specific:
- ✅ "Create a FastAPI endpoint for user login with email/password validation"
- ❌ "Build login"

Include context:
- ✅ "Using the existing user model in models/user.py, create..."
- ❌ "Make user login"

Define output:
- ✅ "Return JSON with user info and JWT token"
- ❌ "Make it work"

### 3. Use Descriptive Labels

Good labels help track progress:
- ✅ "Payment Integration", "Security Audit", "API Docs"
- ❌ "Task 1", "Fix stuff", "Thing"

### 4. Monitor and Guide

- Check worker progress via notifications
- Review intermediate results
- Provide clarification if needed
- Chain workers for complex tasks

### 5. Handle Errors

If a worker fails:
1. Review the error message
2. Check if task description was clear
3. Consider breaking into smaller tasks
4. Try different worker type if mismatched

## Advanced Usage

### Custom Worker Configuration

Modify worker behavior by understanding their system prompts:

```python
# Coder focuses on:
- Clean, tested code
- Error handling
- Following conventions

# Researcher focuses on:
- Multiple sources
- Cross-referencing
- Clear citations

# Writer focuses on:
- Audience-appropriate tone
- Clear structure
- Grammar accuracy
```

### Tool Access

Each worker has only relevant tools:

| Worker | Key Tools |
|--------|-----------|
| coder | exec, files, web |
| researcher | web_search, web_fetch |
| writer | files, web_fetch |
| analyst | files, exec, stocks |
| reviewer | read, exec, web |
| architect | files, web |
| devops | exec, files, web |

### Iteration Limits

Workers have max iterations to prevent runaway tasks:
- coder: 30 (complex implementations)
- researcher: 25 (thorough research)
- writer: 20 (focused writing)
- analyst: 25 (deep analysis)
- reviewer: 20 (thorough review)
- architect: 25 (comprehensive design)
- devops: 25 (complete setup)

## Limitations

1. **Independent Execution** - Workers run independently with no shared state
2. **No Worker Spawning** - Workers cannot spawn other workers
3. **Iteration Limits** - Prevents infinite loops but may need task breakdown
4. **Tool Restrictions** - Limited to assigned tools per worker type

## Performance Tips

### For Coders
- Provide file paths upfront
- Specify coding conventions
- Mention testing requirements
- Include error handling expectations

### For Researchers
- Specify time range
- List preferred sources
- Define output format
- Request citations

### For Writers
- Define target audience
- Specify tone (formal, casual)
- Provide style guides
- Include length requirements

### For Analysts
- Provide data sources
- Specify metrics to track
- Define success criteria
- Request visualizations

### For Reviewers
- List focus areas
- Specify security concerns
- Mention performance goals
- Include compliance needs

### For Architects
- State scale requirements
- List constraints
- Define integration points
- Mention budget/timeline

### For DevOps
- Specify target environment
- List required tools
- Define SLA requirements
- Mention security policies

## Monitoring

Check running workers:

```python
# In agent context, workers report:
# - Start notification
# - Progress updates (via tool calls)
# - Completion notification

# Track via labels:
# "worker-coder-auth-module"
# "worker-researcher-market-analysis"
```

## Troubleshooting

### Worker Takes Too Long
- Break task into smaller pieces
- Reduce scope
- Provide more specific instructions

### Worker Produces Poor Results
- Check if worker type matches task
- Provide more context
- Include examples of expected output

### Worker Fails to Start
- Verify task description is clear
- Check if required tools are available
- Ensure workspace is accessible

### Worker Gets Stuck
- Review tool call history
- Check for circular dependencies
- Provide guidance on next steps

## Examples

### Full Project Workflow

```python
# E-commerce Platform Development

# Phase 1: Research
spawn_worker(
    task="Research e-commerce best practices for checkout flow optimization",
    worker_type="researcher",
    label="Checkout Research"
)

# Phase 2: Architecture
spawn_worker(
    task="Design microservices architecture for e-commerce platform with 100K daily users",
    worker_type="architect",
    label="Platform Architecture"
)

# Phase 3: Implementation
spawn_worker(
    task="Implement product catalog API with search and filtering",
    worker_type="coder",
    label="Catalog API"
)

# Phase 4: DevOps
spawn_worker(
    task="Create Docker Compose setup for local development with all services",
    worker_type="devops",
    label="Dev Environment"
)

# Phase 5: Review
spawn_worker(
    task="Security review of payment processing implementation",
    worker_type="reviewer",
    label="Payment Security Audit"
)

# Phase 6: Documentation
spawn_worker(
    task="Write API documentation for all e-commerce endpoints",
    worker_type="writer",
    label="API Documentation"
)
```

## Integration

The worker system integrates with:
- **Subagent System** - General purpose background tasks
- **Skills System** - Worker skill provides usage guide
- **Tool Registry** - spawn_worker tool available to main agent
- **Message Bus** - Results announced to main agent

---

For more information, see the worker skill at `nanobot/skills/worker/SKILL.md`.
