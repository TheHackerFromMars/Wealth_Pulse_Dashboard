# Deployment Guide

## Quick Start (All-in-One)

Deploy both backend and frontend with a single command:

```bash
./deploy-all.sh
```

This script will:
1. Deploy backend to Railway
2. Deploy frontend to Vercel
3. Provide post-deployment checklist

## Individual Deployments

## Backend Deployment (Railway)

### Prerequisites
1. Create a Railway account at [railway.app](https://railway.app)
2. Install Railway CLI: `npm install -g @railway/cli`

### Steps

#### Option 1: Using the deployment script (recommended)
```bash
./deploy-backend.sh
```

#### Option 2: Manual deployment
1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Login to Railway**
   ```bash
   railway login
   ```

3. **Initialize Railway project**
   ```bash
   railway init
   ```

4. **Deploy to Railway**
   ```bash
   railway up
   ```

5. **Set Environment Variables in Railway Dashboard**
   - `PORT`: Will be automatically set by Railway
   - `CORS_ORIGINS`: Set to your Vercel frontend URL (e.g., `https://your-app.vercel.app`)

6. **Get your Railway deployment URL**
   - Go to Railway dashboard
   - Copy your backend deployment URL (e.g., `https://your-app.railway.app`)

### Railway Configuration Files
- `backend/railway.toml` - Railway deployment configuration
- `backend/runtime.txt` - Python version specification
- `backend/requirements.txt` - Python dependencies
- `backend/data/portfolio_data.json` - Portfolio data from Excel import

## Frontend Deployment (Vercel)

### Prerequisites
1. Create a Vercel account at [vercel.com](https://vercel.com)
2. Install Vercel CLI: `npm install -g vercel`

### Steps

#### Option 1: Using the deployment script (recommended)
```bash
./deploy-frontend.sh
```

#### Option 2: Manual deployment
1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy to Vercel**
   ```bash
   vercel --prod
   ```

4. **Set Environment Variables in Vercel Dashboard**
   - Go to your Vercel project dashboard
   - Navigate to Settings > Environment Variables
   - Add: `VITE_API_URL` = `https://your-railway-backend-url.railway.app`

### Vercel Configuration Files
- `frontend/vercel.json` - Vercel deployment configuration
- `frontend/.env.example` - Environment variables template

## Environment Variables

### Backend (Railway)
```env
PORT=8000
CORS_ORIGINS=https://your-vercel-app.vercel.app
```

### Frontend (Vercel)
```env
VITE_API_URL=https://your-railway-backend.railway.app
```

## Post-Deployment Steps

1. **Update CORS Origins**
   - After deploying frontend to Vercel, get the Vercel URL
   - Update `CORS_ORIGINS` environment variable in Railway to include the Vercel URL

2. **Update Frontend API URL**
   - Set `VITE_API_URL` in Vercel environment variables to your Railway backend URL

3. **Test the Deployment**
   - Visit your Vercel frontend URL
   - Check if the dashboard loads and API calls work properly

## Troubleshooting

### Common Issues

1. **CORS Errors**
   - Ensure CORS_ORIGINS in Railway includes your Vercel domain
   - Check that the frontend is using the correct API URL

2. **Module Import Errors**
   - Check that all required packages are in requirements.txt
   - Verify the FastAPI app structure is correct

3. **Build Failures**
   - Check Railway logs for Python/dependency issues
   - Check Vercel logs for npm/build issues

### Logs
- **Railway**: `railway logs`
- **Vercel**: Check the Vercel dashboard under Functions tab

## Custom Domains (Optional)

### Railway
1. Go to Railway project settings
2. Add custom domain under "Domains"

### Vercel
1. Go to Vercel project settings
2. Add custom domain under "Domains"

## Continuous Deployment

Both Railway and Vercel support automatic deployments from Git repositories:

1. **Connect GitHub Repository**
   - Railway: Connect repo in project settings
   - Vercel: Connect repo during project creation or in settings

2. **Automatic Deployments**
   - Push to main branch triggers automatic deployment
   - Separate staging environments can be set up for development branches
