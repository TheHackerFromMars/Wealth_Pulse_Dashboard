#!/bin/bash
# Complete deployment script for both backend and frontend
echo "🚀 Starting full deployment process..."

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "🔍 Checking prerequisites..."

if ! command_exists railway; then
    echo "❌ Railway CLI not found. Please install it first:"
    echo "   npm install -g @railway/cli"
    exit 1
fi

if ! command_exists vercel; then
    echo "❌ Vercel CLI not found. Please install it first:"
    echo "   npm install -g vercel"
    exit 1
fi

echo "✅ All CLI tools found!"

# Deploy Backend to Railway
echo ""
echo "📦 Step 1: Deploying backend to Railway..."
cd backend

if ! railway whoami &> /dev/null; then
    echo "🔐 Please login to Railway first:"
    railway login
fi

echo "🚀 Deploying backend..."
railway up

if [ $? -eq 0 ]; then
    echo "✅ Backend deployed successfully!"
    echo "📋 Please note your Railway URL from the dashboard"
else
    echo "❌ Backend deployment failed!"
    exit 1
fi

# Deploy Frontend to Vercel
echo ""
echo "📦 Step 2: Deploying frontend to Vercel..."
cd ../frontend

if ! vercel whoami &> /dev/null; then
    echo "🔐 Please login to Vercel first:"
    vercel login
fi

echo "🚀 Deploying frontend..."
vercel --prod

if [ $? -eq 0 ]; then
    echo "✅ Frontend deployed successfully!"
else
    echo "❌ Frontend deployment failed!"
    exit 1
fi

echo ""
echo "🎉 Deployment complete!"
echo ""
echo "📋 Post-deployment checklist:"
echo "   1. Copy your Railway backend URL from Railway dashboard"
echo "   2. Set VITE_API_URL in Vercel environment variables to your Railway URL"
echo "   3. Set CORS_ORIGINS in Railway environment variables to your Vercel URL"
echo "   4. Test your deployed application"
echo ""
echo "🔗 Access your dashboards:"
echo "   Railway: https://railway.app/dashboard"
echo "   Vercel: https://vercel.com/dashboard"
