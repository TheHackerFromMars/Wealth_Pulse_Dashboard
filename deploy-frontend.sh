#!/bin/bash
# Vercel deployment script for frontend
echo "🚀 Deploying frontend to Vercel..."

# Navigate to frontend directory
cd frontend

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found. Please install it first:"
    echo "   npm install -g vercel"
    exit 1
fi

# Check if user is logged in
if ! vercel whoami &> /dev/null; then
    echo "🔐 Please login to Vercel first:"
    vercel login
fi

# Deploy to Vercel
echo "📦 Deploying to Vercel..."
vercel --prod

echo "✅ Deployment complete!"
echo "📋 Don't forget to:"
echo "   1. Set VITE_API_URL environment variable in Vercel dashboard"
echo "   2. Update CORS_ORIGINS in Railway with your Vercel URL"
