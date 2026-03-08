#!/bin/bash
# Coolify Deployment Verification Script for nanobot
# Run this after deploying to verify everything is working

set -e

echo "🐈 nanobot Coolify Deployment Verification"
echo "=========================================="
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check functions
check_pass() {
    echo -e "${GREEN}✓${NC} $1"
}

check_fail() {
    echo -e "${RED}✗${NC} $1"
}

check_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# 1. Check if running in Docker
echo "1. Checking container environment..."
if [ -f /.dockerenv ]; then
    check_pass "Running inside Docker container"
else
    check_warn "Not running in Docker (this is OK for local testing)"
fi

# 2. Check nanobot installation
echo ""
echo "2. Checking nanobot installation..."
if command -v nanobot &> /dev/null; then
    check_pass "nanobot is installed"
    nanobot --version
else
    check_fail "nanobot is not installed"
    echo "   Run: pip install -e ."
    exit 1
fi

# 3. Check configuration
echo ""
echo "3. Checking configuration..."
if [ -f ~/.nanobot/config.json ]; then
    check_pass "Configuration file exists"
    
    # Check for API keys
    if grep -q "apiKey" ~/.nanobot/config.json 2>/dev/null; then
        check_pass "API key configured"
    else
        check_warn "No API key found in config"
    fi
else
    check_warn "No config file found (run 'nanobot onboard' to create)"
fi

# 4. Check environment variables (Coolify)
echo ""
echo "4. Checking Coolify environment variables..."

if [ -n "$OPENROUTER_API_KEY" ] || [ -n "$ANTHROPIC_API_KEY" ] || [ -n "$DASHSCOPE_API_KEY" ]; then
    check_pass "LLM provider API key is set"
else
    check_warn "No LLM API key found in environment variables"
    echo "   Set one of: OPENROUTER_API_KEY, ANTHROPIC_API_KEY, or DASHSCOPE_API_KEY"
fi

if [ -n "$AI_MODEL" ]; then
    check_pass "AI_MODEL is set: $AI_MODEL"
else
    check_warn "AI_MODEL not set (will use default)"
fi

if [ -n "$RESTRICT_TO_WORKSPACE" ] && [ "$RESTRICT_TO_WORKSPACE" = "true" ]; then
    check_pass "Workspace restriction enabled (security)"
fi

# 5. Check workspace
echo ""
echo "5. Checking workspace..."
if [ -d ~/.nanobot/workspace ]; then
    check_pass "Workspace directory exists"
    
    if [ -f ~/.nanobot/workspace/MEMORY.md ]; then
        check_pass "Memory file exists"
    fi
    
    if [ -f ~/.nanobot/workspace/HEARTBEAT.md ]; then
        check_pass "Heartbeat file exists"
    fi
else
    check_warn "Workspace not found (will be created on first run)"
fi

# 6. Run status check
echo ""
echo "6. Running nanobot status..."
if nanobot status &> /dev/null; then
    check_pass "nanobot status check passed"
    nanobot status
else
    check_warn "Status check failed (may need API key)"
fi

# 7. Check available tools
echo ""
echo "7. Checking available tools..."
TOOLS=("stock_analysis" "market_overview" "compare_stocks")
for tool in "${TOOLS[@]}"; do
    if grep -r "$tool" nanobot/agent/tools/ &> /dev/null; then
        check_pass "Tool '$tool' available"
    else
        check_warn "Tool '$tool' not found"
    fi
done

# 8. Check skills
echo ""
echo "8. Checking skills..."
SKILLS=("docx" "pdf" "fullstack-coding" "stock-insight")
for skill in "${SKILLS[@]}"; do
    if [ -d "nanobot/skills/$skill" ]; then
        check_pass "Skill '$skill' installed"
    else
        check_warn "Skill '$skill' not found"
    fi
done

# Summary
echo ""
echo "=========================================="
echo "Verification Complete!"
echo ""

if command -v nanobot &> /dev/null; then
    check_pass "nanobot is ready to use"
    echo ""
    echo "Next steps:"
    echo "  1. Ensure API key is configured"
    echo "  2. Run: nanobot agent -m 'Hello!'"
    echo "  3. Configure chat channels if needed"
else
    check_fail "nanobot is not properly installed"
    echo ""
    echo "Please run: pip install -e ."
fi

echo ""
