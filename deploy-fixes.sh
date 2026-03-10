#!/bin/bash
# Deploy ClawCustom Fixes to GitHub
# Run this script to push all fixes to GitHub for Coolify deployment

set -e

echo "🚀 Deploying ClawCustom Fixes to GitHub"
echo "========================================"
echo ""

# Check if we're in the right directory
if [ ! -f "clawcustom/cli/commands.py" ]; then
    echo "❌ Error: Please run this script from the clawcustom repository root"
    exit 1
fi

# Stage all changes
echo "📦 Staging changes..."
git add -A

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "✅ No changes to commit"
else
    # Commit changes
    echo "💾 Committing changes..."
    git commit -m "fix: CLI import errors and DashScope configuration"
fi

# Get current branch
BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "📍 Current branch: $BRANCH"

# Push to GitHub
echo "⬆️  Pushing to GitHub..."
git push origin $BRANCH

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "🎯 Next Steps:"
    echo "   1. Go to Coolify Dashboard"
    echo "   2. Select your clawcustom service"
    echo "   3. Click 'Redeploy' (or enable Auto Deploy)"
    echo "   4. Wait for build to complete (~3 minutes)"
    echo "   5. Test with: clawcustom agent -m 'help'"
    echo ""
    echo "📚 Documentation:"
    echo "   - DEPLOY_FIX.md"
    echo "   - DEPLOY_NOW.md"
    echo "   - DASHSCOPE_SETUP.md"
    echo ""
else
    echo ""
    echo "❌ Push failed. Please check:"
    echo "   - GitHub credentials"
    echo "   - Repository permissions"
    echo "   - Network connection"
    echo ""
    echo "Manual push command:"
    echo "   git push origin $BRANCH"
    echo ""
    exit 1
fi
