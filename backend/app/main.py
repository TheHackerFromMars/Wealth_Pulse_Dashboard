from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn
import os

from .models import Holding, Allocation, Performance, Summary
from .data_service import portfolio_service

# Create FastAPI app
app = FastAPI(
    title="Portfolio Analytics API",
    description="Backend API for portfolio analytics dashboard",
    version="1.0.0"
)

# Configure CORS origins
allowed_origins = os.getenv("CORS_ORIGINS", "*").split(",")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Portfolio Analytics API is running"}

@app.get("/api/portfolio/holdings", response_model=List[Holding])
async def get_holdings():
    """Get complete list of user's stock investments"""
    try:
        return portfolio_service.get_holdings()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to compute holdings: {str(e)}")

@app.get("/api/portfolio/allocation", response_model=Allocation)
async def get_allocation():
    """Get asset distribution by sectors and market cap"""
    try:
        return portfolio_service.get_allocation()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to compute allocation: {str(e)}")

@app.get("/api/portfolio/performance", response_model=Performance)
async def get_performance():
    """Get historical performance vs benchmarks"""
    try:
        return portfolio_service.get_performance()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to compute performance: {str(e)}")

@app.get("/api/portfolio/summary", response_model=Summary)
async def get_summary():
    """Get key portfolio metrics and insights"""
    try:
        return portfolio_service.get_summary()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to compute summary: {str(e)}")

@app.post("/api/portfolio/reload")
async def reload_data():
    """Reload portfolio data from JSON file (useful after data import)"""
    try:
        portfolio_service.reload_data()
        return {"message": "Portfolio data reloaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to reload data: {str(e)}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
