# Worker Agent Examples

Practical examples of using specialized worker agents.

## Table of Contents

- [Single Worker Examples](#single-worker-examples)
- [Multi-Worker Workflows](#multi-worker-workflows)
- [Real-World Scenarios](#real-world-scenarios)

---

## Single Worker Examples

### Coder Worker

**Task: Create a new feature**

```python
spawn_worker(
    task="""
    Create a Python module for email validation and sending.
    
    Requirements:
    - Validate email format using regex
    - Send emails via SMTP
    - Support HTML and plain text
    - Handle attachments
    - Include error handling and logging
    
    Files to create:
    - nanobot/utils/email_service.py
    - tests/test_email_service.py
    
    Follow existing code style in the project.
    """,
    worker_type="coder",
    label="Email Service Module"
)
```

**Task: Fix a bug**

```python
spawn_worker(
    task="""
    Fix the race condition in the database connection pool.
    
    Issue: Multiple threads sometimes get the same connection.
    Location: nanobot/db/pool.py
    
    Requirements:
    - Add proper locking
    - Ensure thread-safe connection acquisition
    - Add tests to verify the fix
    - Don't break existing functionality
    """,
    worker_type="coder",
    label="DB Pool Race Condition Fix"
)
```

### Researcher Worker

**Task: Market research**

```python
spawn_worker(
    task="""
    Research the competitive landscape for AI coding assistants.
    
    Focus areas:
    - Top 5 competitors (GitHub Copilot, Cursor, Codeium, etc.)
    - Pricing models
    - Key features and differentiators
    - Target audience
    - Recent funding or acquisitions
    
    Output:
    - Summary table comparing features and pricing
    - SWOT analysis for each competitor
    - Market trends and opportunities
    
    Include links to all sources.
    """,
    worker_type="researcher",
    label="AI Coding Assistant Market Research"
)
```

**Task: Technology research**

```python
spawn_worker(
    task="""
    Research best practices for implementing rate limiting in FastAPI.
    
    Topics to cover:
    - Different rate limiting algorithms (token bucket, sliding window, etc.)
    - Redis-based distributed rate limiting
    - FastAPI middleware vs dependency injection
    - Existing libraries (slowapi, fastapi-limiter, etc.)
    - Performance implications
    
    Provide code examples and recommend the best approach for a high-traffic API.
    """,
    worker_type="researcher",
    label="Rate Limiting Best Practices"
)
```

### Writer Worker

**Task: API documentation**

```python
spawn_worker(
    task="""
    Write API documentation for the user authentication endpoints.
    
    Endpoints to document:
    - POST /api/v1/auth/register
    - POST /api/v1/auth/login
    - POST /api/v1/auth/logout
    - POST /api/v1/auth/refresh
    - POST /api/v1/auth/password/reset
    
    For each endpoint include:
    - Description
    - Request format (headers, body)
    - Response format (success and error cases)
    - Example requests and responses
    - Authentication requirements
    
    Use Markdown format. Match the style of existing docs in docs/api/.
    """,
    worker_type="writer",
    label="Auth API Documentation"
)
```

**Task: Blog post**

```python
spawn_worker(
    task="""
    Write a technical blog post about building scalable AI assistants.
    
    Topics to cover:
    - Architecture overview
    - Handling concurrent requests
    - Caching strategies
    - Database optimization
    - Monitoring and alerting
    
    Target audience: Software engineers building AI applications.
    Tone: Technical but accessible.
    Length: 1500-2000 words.
    
    Include code examples and diagrams where helpful.
    """,
    worker_type="writer",
    label="Scalable AI Assistants Blog Post"
)
```

### Analyst Worker

**Task: Sales analysis**

```python
spawn_worker(
    task="""
    Analyze Q4 2025 sales data from data/sales_q4_2025.csv.
    
    Analysis required:
    - Total revenue and growth vs Q3
    - Top 10 products by revenue
    - Sales trends by month and week
    - Customer segmentation (new vs returning)
    - Regional performance
    
    Output:
    - Executive summary with key findings
    - Detailed metrics and charts
    - Recommendations for Q1 2026
    
    Use Python for analysis. Create visualizations with matplotlib.
    """,
    worker_type="analyst",
    label="Q4 2025 Sales Analysis"
)
```

**Task: Stock portfolio review**

```python
spawn_worker(
    task="""
    Review and analyze the stock portfolio performance.
    
    Holdings:
    - AAPL: 50 shares
    - GOOGL: 20 shares
    - MSFT: 30 shares
    - NVDA: 15 shares
    
    Analysis needed:
    - Current portfolio value
    - YTD return percentage
    - Allocation by sector
    - Risk assessment (beta, volatility)
    - Comparison with S&P 500
    
    Provide rebalancing recommendations based on current market conditions.
    """,
    worker_type="analyst",
    label="Stock Portfolio Review"
)
```

### Reviewer Worker

**Task: Security audit**

```python
spawn_worker(
    task="""
    Conduct a security audit of the authentication module.
    
    Files to review:
    - nanobot/auth/login.py
    - nanobot/auth/jwt.py
    - nanobot/auth/oauth.py
    
    Check for:
    - SQL injection vulnerabilities
    - XSS and CSRF protection
    - Password hashing and storage
    - JWT token security
    - Session management
    - Input validation
    
    Output:
    - List of vulnerabilities by severity (critical, high, medium, low)
    - Specific code locations
    - Remediation recommendations
    - Priority order for fixes
    """,
    worker_type="reviewer",
    label="Auth Security Audit"
)
```

**Task: Code quality review**

```python
spawn_worker(
    task="""
    Review the codebase for code quality and best practices.
    
    Focus areas:
    - Code duplication
    - Function complexity (too long, too many parameters)
    - Missing type hints
    - Inconsistent naming conventions
    - Missing docstrings
    - Error handling gaps
    
    Review all files in nanobot/agent/ directory.
    
    Provide a report with:
    - Issues categorized by type
    - Specific file and line numbers
    - Suggested improvements
    - Estimated effort to fix
    """,
    worker_type="reviewer",
    label="Code Quality Review"
)
```

### Architect Worker

**Task: System design**

```python
spawn_worker(
    task="""
    Design a microservices architecture for a real-time collaboration platform.
    
    Requirements:
    - Support 100,000 concurrent users
    - Real-time document editing
    - Video/audio calls
    - Chat messaging
    - File sharing
    
    Deliverables:
    - Service breakdown and responsibilities
    - Data flow diagrams
    - API gateway design
    - Database strategy (SQL vs NoSQL per service)
    - Caching strategy
    - Message queue design
    - Scaling strategy
    
    Consider trade-offs and provide rationale for key decisions.
    """,
    worker_type="architect",
    label="Real-time Collaboration Platform Architecture"
)
```

**Task: Database design**

```python
spawn_worker(
    task="""
    Design a database schema for a multi-tenant SaaS application.
    
    Requirements:
    - Tenant isolation (data segregation)
    - User management with roles
    - Subscription and billing
    - Audit logging
    - Multi-currency support
    
    Deliverables:
    - ER diagram
    - Table definitions with columns and types
    - Index strategy
    - Migration plan from single-tenant
    - Sharding strategy for scale
    
    Use PostgreSQL. Include SQL for core tables.
    """,
    worker_type="architect",
    label="Multi-tenant SaaS Database Design"
)
```

### DevOps Worker

**Task: CI/CD pipeline**

```python
spawn_worker(
    task="""
    Create a CI/CD pipeline for deploying to Kubernetes.
    
    Requirements:
    - Build Docker images on PR merge
    - Run tests before deployment
    - Deploy to staging automatically
    - Production deployment with approval
    - Rollback capability
    - Slack notifications
    
    Tools: GitHub Actions, Docker, Kubernetes, Helm
    
    Deliverables:
    - GitHub Actions workflow files
    - Helm charts for deployment
    - Environment configuration
    - Deployment documentation
    """,
    worker_type="devops",
    label="Kubernetes CI/CD Pipeline"
)
```

**Task: Infrastructure setup**

```python
spawn_worker(
    task="""
    Set up Docker Compose for local development environment.
    
    Services needed:
    - Web application (Python/FastAPI)
    - Frontend (Node.js/React)
    - PostgreSQL database
    - Redis cache
    - Nginx reverse proxy
    
    Requirements:
    - Hot reload for development
    - Persistent data volumes
    - Environment variable management
    - Health checks
    - Logging configuration
    
    Deliverables:
    - docker-compose.yml
    - Dockerfile for each service
    - .env.example file
    - Setup instructions
    """,
    worker_type="devops",
    label="Local Development Environment"
)
```

---

## Multi-Worker Workflows

### New Feature Development

```python
# Phase 1: Research
spawn_worker(
    task="Research best practices for implementing search functionality in web applications. Compare ElasticSearch, Algolia, and PostgreSQL full-text search.",
    worker_type="researcher",
    label="Search Technology Research"
)

# Phase 2: Architecture
spawn_worker(
    task="Design search architecture for the e-commerce platform. Support product search, filtering, faceting, and autocomplete. Handle 10K products and 1M searches/day.",
    worker_type="architect",
    label="Search Architecture Design"
)

# Phase 3: Implementation
spawn_worker(
    task="Implement the search service based on the architecture document. Include API endpoints, search indexing, and query optimization.",
    worker_type="coder",
    label="Search Service Implementation"
)

# Phase 4: Testing & Review
spawn_worker(
    task="Review the search service implementation for performance, security, and code quality. Test with large datasets.",
    worker_type="reviewer",
    label="Search Service Review"
)

# Phase 5: Documentation
spawn_worker(
    task="Write documentation for the search API including usage examples, query syntax, and performance tuning guide.",
    worker_type="writer",
    label="Search API Documentation"
)
```

### Product Launch

```python
# Market Research
spawn_worker(
    task="Analyze the target market for our new AI assistant product. Identify customer segments, pain points, and willingness to pay.",
    worker_type="analyst",
    label="Market Analysis"
)

# Competitive Research
spawn_worker(
    task="Research direct and indirect competitors. Analyze their features, pricing, positioning, and customer reviews.",
    worker_type="researcher",
    label="Competitive Analysis"
)

# Go-to-Market Strategy
spawn_worker(
    task="Based on research findings, design a go-to-market strategy including positioning, pricing, and launch plan.",
    worker_type="architect",
    label="GTM Strategy"
)

# Marketing Content
spawn_worker(
    task="Write launch announcement blog post, product landing page copy, and email campaign for early access users.",
    worker_type="writer",
    label="Launch Content"
)

# Technical Setup
spawn_worker(
    task="Set up analytics, A/B testing, and monitoring for the launch. Create dashboards for tracking KPIs.",
    worker_type="devops",
    label="Launch Infrastructure"
)
```

### Security Hardening

```python
# Security Audit
spawn_worker(
    task="Comprehensive security audit of the entire codebase. Focus on OWASP Top 10 vulnerabilities.",
    worker_type="reviewer",
    label="Security Audit"
)

# Threat Modeling
spawn_worker(
    task="Create threat model for the application. Identify assets, attack vectors, and mitigation strategies.",
    worker_type="architect",
    label="Threat Modeling"
)

# Security Fixes
spawn_worker(
    task="Implement security fixes for all high and critical vulnerabilities found in the audit.",
    worker_type="coder",
    label="Security Fixes"
)

# Security Documentation
spawn_worker(
    task="Write security best practices guide for the development team. Include secure coding standards and review checklist.",
    worker_type="writer",
    label="Security Documentation"
)

# Security Monitoring
spawn_worker(
    task="Set up security monitoring, intrusion detection, and alerting. Configure log analysis for security events.",
    worker_type="devops",
    label="Security Monitoring"
)
```

---

## Real-World Scenarios

### Scenario 1: Startup MVP

You're building an MVP for a new SaaS product:

```python
# 1. Market validation
spawn_worker(
    task="Research the problem space and validate market need for [your idea]. Find evidence of people actively seeking solutions.",
    worker_type="researcher",
    label="Market Validation"
)

# 2. Technical architecture
spawn_worker(
    task="Design minimal architecture for MVP. Focus on speed to market but allow for scaling. Recommend tech stack.",
    worker_type="architect",
    label="MVP Architecture"
)

# 3. Core features
spawn_worker(
    task="Implement core features: user authentication, dashboard, main value proposition feature. Use the recommended stack.",
    worker_type="coder",
    label="MVP Development"
)

# 4. Deploy infrastructure
spawn_worker(
    task="Set up production deployment on cloud provider. Include database, backups, monitoring, and SSL.",
    worker_type="devops",
    label="Production Setup"
)

# 5. Launch materials
spawn_worker(
    task="Write landing page, documentation, and launch announcement. Create onboarding guide for early users.",
    worker_type="writer",
    label="Launch Materials"
)
```

### Scenario 2: Enterprise Migration

Migrating from monolith to microservices:

```python
# 1. Current state analysis
spawn_worker(
    task="Analyze the existing monolithic codebase. Document dependencies, data flows, and pain points.",
    worker_type="analyst",
    label="Current State Analysis"
)

# 2. Target architecture
spawn_worker(
    task="Design microservices architecture. Define service boundaries, communication patterns, and data migration strategy.",
    worker_type="architect",
    label="Target Architecture"
)

# 3. Migration plan
spawn_worker(
    task="Create detailed migration plan with phases, timeline, risk mitigation, and rollback procedures.",
    worker_type="architect",
    label="Migration Plan"
)

# 4. Implement services
spawn_worker(
    task="Implement first microservice (user service) following the architecture. Include API, database, tests.",
    worker_type="coder",
    label="User Service Implementation"
)

# 5. Setup infrastructure
spawn_worker(
    task="Set up Kubernetes cluster, service mesh, CI/CD, and monitoring for microservices.",
    worker_type="devops",
    label="K8s Infrastructure"
)
```

---

## Tips for Better Results

### 1. Be Specific

❌ Bad: "Build a login system"

✅ Good: "Implement JWT-based authentication with email/password login, password reset via email, token refresh, and session management. Store passwords with bcrypt. Use the existing user model."

### 2. Provide Context

❌ Bad: "Fix the bug"

✅ Good: "Fix the NullReferenceException in CheckoutService.cs line 142. Issue occurs when cart is empty. Add null check and return appropriate error response."

### 3. Define Success

❌ Bad: "Write tests"

✅ Good: "Write unit tests achieving 90% code coverage for the payment module. Include tests for success, failure, edge cases, and error handling. Use pytest."

### 4. Include Constraints

❌ Bad: "Make it faster"

✅ Good: "Optimize database queries to reduce page load time to under 200ms for 10K concurrent users. Use connection pooling and query caching."

### 5. Chain Workers

Complex tasks work best with multiple specialized workers:
- Research → Design → Implement → Review → Document

---

For more information, see [WORKER_AGENTS.md](WORKER_AGENTS.md).
