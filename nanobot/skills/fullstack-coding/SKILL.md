---
name: fullstack-coding
description: "Create isolated Docker-based development sandboxes for fullstack coding. Spin up ephemeral development environments with Node.js, Python, databases, and more using docker-compose templates."
metadata: {"nanobot":{"emoji":"🛠️","requires":{"bins":["docker","docker-compose"]},"install":[{"id":"docker","kind":"brew","formula":"docker","bins":["docker"],"label":"Install Docker (brew)"},{"id":"docker-compose","kind":"brew","formula":"docker-compose","bins":["docker-compose"],"label":"Install Docker Compose (brew)"}]}}
---

# Fullstack Coding Skill

Create isolated, ephemeral Docker-based development environments for fullstack coding projects. Each sandbox is a self-contained development environment that can be created, used, and destroyed without affecting the host system.

## Prerequisites

- Docker installed and running
- docker-compose installed

## Quick Start

### Create a new sandbox:

```bash
# Create a new project directory
mkdir -p ~/sandbox/my-project
cd ~/sandbox/my-project

# Copy a template
cp ~/nanobot/skills/fullstack-coding/templates/nodejs.yml docker-compose.yml

# Start the environment
docker-compose up -d
```

### Common Commands:

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Remove containers and volumes (clean slate)
docker-compose down -v

# Rebuild containers
docker-compose build --no-cache
docker-compose up -d

# Execute commands in a container
docker-compose exec app npm install
docker-compose exec api python manage.py migrate
```

## Available Templates

### Node.js (Express API)

File: `templates/nodejs.yml`

```yaml
services:
  app:
    image: node:20
    working_dir: /app
    volumes:
      - .:/app
    ports:
      - "3000:3000"
    command: sleep infinity
    environment:
      - NODE_ENV=development
```

Usage:
```bash
cp templates/nodejs.yml docker-compose.yml
docker-compose up -d
docker-compose exec app sh
# Then: npm init -y && npm install express
```

### Python (FastAPI)

File: `templates/python.yml`

```yaml
services:
  api:
    image: python:3.11
    working_dir: /app
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    command: sleep infinity
```

### Node.js + React (Fullstack)

File: `templates/fullstack.yml`

```yaml
services:
  frontend:
    image: node:20
    working_dir: /app
    volumes:
      - ./frontend:/app
    ports:
      - "3000:3000"
    command: sh -c "npm install && npm start"
  
  backend:
    image: node:20
    working_dir: /app
    volumes:
      - ./backend:/app
    ports:
      - "4000:4000"
    command: sleep infinity
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: dev
      POSTGRES_DB: app
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

### Node.js + MySQL

File: `templates/nodejs-mysql.yml`

```yaml
services:
  app:
    image: node:20
    working_dir: /app
    volumes:
      - .:/app
    ports:
      - "3000:3000"
    command: sleep infinity
    depends_on:
      - db
  
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: dev
      MYSQL_DATABASE: app
    ports:
      - "3306:3306"
    volumes:
      - mysqldata:/var/lib/mysql

volumes:
  mysqldata:
```

### Node.js + MongoDB

File: `templates/nodejs-mongo.yml`

```yaml
services:
  app:
    image: node:20
    working_dir: /app
    volumes:
      - .:/app
    ports:
      - "3000:3000"
    command: sleep infinity
    depends_on:
      - db
  
  db:
    image: mongo:7
    ports:
      - "27017:27017"
    volumes:
      - mongodata:/data/db

volumes:
  mongodata:
```

### Python + PostgreSQL

File: `templates/python-postgres.yml`

```yaml
services:
  api:
    image: python:3.11
    working_dir: /app
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    command: sleep infinity
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: dev
      POSTGRES_DB: app
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

### Redis Cache

File: `templates/redis.yml`

```yaml
services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --requirepass dev
    volumes:
      - redisdata:/data

volumes:
  redisdata:
```

## Working with Sandboxes

### Interactive Shell Access:

```bash
# Get shell in Node container
docker-compose exec app sh

# Get shell in Python container
docker-compose exec api sh

# Get shell as root
docker-compose exec --user root app sh
```

### Install Dependencies:

```bash
# Node.js
docker-compose exec app npm install lodash express

# Python
docker-compose exec api pip install fastapi uvicorn

# Python with requirements.txt
docker-compose exec api pip install -r requirements.txt
```

### Run Development Servers:

```bash
# Node/Express
docker-compose exec app node server.js

# Python/FastAPI
docker-compose exec api uvicorn main:app --host 0.0.0.0 --reload
```

### Access Services:

```bash
# From host, access:
# - Node app: http://localhost:3000
# - Python API: http://localhost:8000
# - PostgreSQL: localhost:5432 (user: postgres, pass: dev)
# - MySQL: localhost:3306 (user: root, pass: dev)
# - MongoDB: localhost:27017
# - Redis: localhost:6379
```

## Best Practices

### 1. Always Clean Up

```bash
# When done with a project
docker-compose down -v

# Remove the project directory
cd .. && rm -rf my-project
```

### 2. Use Named Containers

```bash
docker-compose --project-name my-project up -d
```

### 3. Share Files Between Host and Container

The `volumes: - .:/app` mount maps the current directory into the container. Edit files on your host and changes appear immediately in the container.

### 4. Persist Data

Always use named volumes for databases to prevent data loss:
```yaml
volumes:
  pgdata:
```

### 5. Check Logs

```bash
# All services
docker-compose logs

# Specific service
docker-compose logs -f app

# Last 100 lines
docker-compose logs --tail=100
```

## Example Workflow

```bash
# 1. Create project directory
mkdir ~/sandbox/todo-api
cd ~/sandbox/todo-api

# 2. Set up Python + PostgreSQL template
cp ~/nanobot/skills/fullstack-coding/templates/python-postgres.yml docker-compose.yml

# 3. Start the database
docker-compose up -d db

# 4. Create the API
docker-compose exec api sh -c "pip install fastapi uvicorn psycopg2-binary"

# 5. Create main.py with FastAPI code
cat > main.py << 'EOF'
from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/health")
def health_check():
    return {"database": "connected"}
EOF

# 6. Run the API
docker-compose exec api uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# 7. Test from host
curl http://localhost:8000/

# 8. Clean up when done
docker-compose down -v
cd .. && rm -rf todo-api
```
