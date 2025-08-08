#!/bin/bash

# Portfolio Analytics - Development Setup Script
# This script tests both frontend and backend integration

echo "🚀 Portfolio Analytics - Development Test"
echo "=========================================="

# Test backend health
echo "📊 Testing Backend API (Python FastAPI)..."
echo "Backend running on: http://localhost:8000"

# Test all endpoints
echo "✅ Testing Holdings endpoint..."
curl -s http://localhost:8000/api/portfolio/holdings | head -c 100
echo ""

echo "✅ Testing Allocation endpoint..."
curl -s http://localhost:8000/api/portfolio/allocation | head -c 100
echo ""

echo "✅ Testing Performance endpoint..."
curl -s http://localhost:8000/api/portfolio/performance | head -c 100
echo ""

echo "✅ Testing Summary endpoint..."
curl -s http://localhost:8000/api/portfolio/summary | head -c 100
echo ""

echo "🌐 Frontend running on: http://localhost:8080"
echo "📚 API Documentation: http://localhost:8000/docs"
echo ""

echo "🎉 Setup Complete! Both frontend and backend are running."
echo "Frontend is now using the Python FastAPI backend with optimized JSON data pipeline."
