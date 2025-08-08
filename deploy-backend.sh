#!/bin/bash
# Railway deployment script for backend
echo "🚀 Deploying backend to Railway..."

# Navigate to backend directory
cd backend

# Check if railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found. Please install it first:"
    echo "   npm install -g @railway/cli"
    exit 1
fi

# Check if user is logged in
if ! railway whoami &> /dev/null; then
    echo "🔐 Please login to Railway first:"
    railway login
fi

# Deploy to Railway
echo "📦 Deploying to Railway..."
railway up

echo "✅ Deployment complete!"
echo "📋 Don't forget to:"
echo "   1. Set CORS_ORIGINS environment variable in Railway dashboard"
echo "   2. Copy your Railway URL for frontend configuration"
