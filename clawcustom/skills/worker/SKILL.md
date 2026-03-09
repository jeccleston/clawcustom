---
name: worker
description: "Spawn specialized worker agents for specific task domains. Each worker has expertise in coding, research, writing, analysis, or review tasks."
metadata: {"nanobot":{"emoji":"👷","requires":{"bins":[]},"always":false}}
---

# Worker Agent Skill

Spawn specialized worker agents optimized for specific task domains. Each worker type has tailored system prompts, tools, and expertise.

## Worker Types

| Worker | Specialty | Use Case |
|--------|-----------|----------|
| `coder` | Software development | Build features, fix bugs, write tests |
| `researcher` | Information gathering | Market research, competitive analysis |
| `writer` | Content creation | Documentation, articles, emails |
| `analyst` | Data analysis | Financial analysis, metrics, insights |
| `reviewer` | Code review | QA, security audit, best practices |
| `architect` | System design | Architecture, APIs, databases |
| `devops` | Infrastructure | Docker, CI/CD, deployment |

## Usage

### Spawn a Worker

```python
# Via spawn tool
spawn(
    task="Build a REST API with FastAPI for user management",
    worker_type="coder",
    label="User API Development"
)
```

### Worker Configuration

Each worker type has:

1. **Specialized System Prompt** - Domain-specific instructions
2. **Tool Access** - Only relevant tools for the task
3. **Iteration Limits** - Adjusted for task complexity
4. **Model Settings** - Optimized temperature and tokens

## Worker Specifications

### Coder

**Specialty:** Software development, debugging, refactoring

**Tools:**
- File operations (read, write, edit, list)
- Shell execution
- Web search (for documentation)
- Web fetch (for API docs)

**System Prompt Focus:**
- Write clean, tested, production-ready code
- Follow existing code conventions
- Include error handling and logging
- Add comments for complex logic
- Prefer simplicity over cleverness

**Example:**
```
spawn(
    task="Create a Python module to parse CSV files and validate data",
    worker_type="coder",
    label="CSV Parser Module"
)
```

### Researcher

**Specialty:** Information gathering, market analysis, competitive research

**Tools:**
- Web search (extensive)
- Web fetch (deep content extraction)
- File operations (for reports)

**System Prompt Focus:**
- Gather comprehensive, verified information
- Cross-reference multiple sources
- Organize findings logically
- Cite sources clearly
- Distinguish facts from opinions

**Example:**
```
spawn(
    task="Research the top 5 competitors in the AI assistant market and summarize their features, pricing, and positioning",
    worker_type="researcher",
    label="Competitive Analysis"
)
```

### Writer

**Specialty:** Content creation, documentation, communication

**Tools:**
- File operations
- Web fetch (for reference material)

**System Prompt Focus:**
- Clear, concise writing
- Appropriate tone for audience
- Proper structure and formatting
- Grammar and spelling accuracy
- Engaging and informative

**Example:**
```
spawn(
    task="Write API documentation for the user authentication endpoints",
    worker_type="writer",
    label="Auth API Docs"
)
```

### Analyst

**Specialty:** Data analysis, financial modeling, insights

**Tools:**
- File operations (data files)
- Shell execution (for data processing)
- Stock analysis tools
- Web search (for market data)

**System Prompt Focus:**
- Data-driven conclusions
- Clear visualizations where helpful
- Identify trends and patterns
- Quantify findings
- Highlight risks and opportunities

**Example:**
```
spawn(
    task="Analyze Q4 sales data and identify trends, top performers, and areas for improvement",
    worker_type="analyst",
    label="Q4 Sales Analysis"
)
```

### Reviewer

**Specialty:** Code review, security audit, quality assurance

**Tools:**
- File operations (read-only)
- Web search (for security best practices)
- Shell execution (for linting, testing)

**System Prompt Focus:**
- Identify bugs and vulnerabilities
- Check coding standards compliance
- Suggest improvements
- Flag security concerns
- Verify test coverage

**Example:**
```
spawn(
    task="Review the authentication module for security vulnerabilities and suggest improvements",
    worker_type="reviewer",
    label="Auth Security Review"
)
```

### Architect

**Specialty:** System design, API design, database schema

**Tools:**
- File operations
- Web search (for patterns and best practices)
- Web fetch (for reference architectures)

**System Prompt Focus:**
- Scalable, maintainable designs
- Clear component boundaries
- Well-defined interfaces
- Consider trade-offs
- Document decisions

**Example:**
```
spawn(
    task="Design a microservices architecture for an e-commerce platform with 1M daily users",
    worker_type="architect",
    label="E-commerce Architecture"
)
```

### DevOps

**Specialty:** Infrastructure, CI/CD, deployment, monitoring

**Tools:**
- Shell execution (Docker, kubectl, etc.)
- File operations (config files)
- Web search (for latest practices)

**System Prompt Focus:**
- Infrastructure as code
- Automated pipelines
- Security best practices
- Monitoring and alerting
- Disaster recovery

**Example:**
```
spawn(
    task="Create a CI/CD pipeline for deploying the app to Kubernetes with zero downtime",
    worker_type="devops",
    label="K8s CI/CD Pipeline"
)
```

## Best Practices

### 1. Choose the Right Worker

Match the worker type to the primary task:
- Building features → `coder`
- Gathering info → `researcher`
- Writing docs → `writer`
- Analyzing data → `analyst`
- Reviewing code → `reviewer`

### 2. Provide Clear Tasks

Be specific about:
- What needs to be done
- Expected output format
- Any constraints or requirements
- Success criteria

### 3. Set Appropriate Labels

Use descriptive labels for tracking:
- Good: "Payment Integration", "Security Audit"
- Bad: "Task 1", "Fix stuff"

### 4. Monitor Progress

Check worker output via:
- Progress notifications
- Final results
- Intermediate file changes

### 5. Chain Workers

Complex tasks may need multiple workers:

```
1. researcher → Gather requirements
2. architect → Design solution
3. coder → Implement
4. reviewer → Quality check
5. writer → Documentation
```

## Example Workflow

```python
# Multi-worker project

# Step 1: Research
spawn(
    task="Research best practices for implementing OAuth2 authentication",
    worker_type="researcher",
    label="OAuth2 Research"
)

# Step 2: Design
spawn(
    task="Design OAuth2 authentication flow with security considerations",
    worker_type="architect",
    label="OAuth2 Architecture"
)

# Step 3: Implement
spawn(
    task="Implement OAuth2 authentication based on the architecture doc",
    worker_type="coder",
    label="OAuth2 Implementation"
)

# Step 4: Review
spawn(
    task="Security review of OAuth2 implementation",
    worker_type="reviewer",
    label="OAuth2 Security Review"
)

# Step 5: Document
spawn(
    task="Write user guide for OAuth2 authentication",
    worker_type="writer",
    label="OAuth2 Documentation"
)
```

## Limitations

- Workers run independently - no shared state between them
- Each worker has iteration limits (prevents runaway tasks)
- Workers can't spawn other workers (only main agent can)
- Complex tasks may need human guidance

## Error Handling

If a worker fails:

1. Review the error message
2. Check if task was clear enough
3. Consider breaking into smaller tasks
4. Try a different worker type if mismatched

## Performance Tips

- **Coder:** Provide file paths and conventions upfront
- **Researcher:** Specify time range and source preferences
- **Writer:** Define audience and tone
- **Analyst:** Include data sources and metrics
- **Reviewer:** List specific concerns to focus on
- **Architect:** State scale requirements and constraints
- **DevOps:** Specify target environment and tools
