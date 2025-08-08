#!/bin/bash

# Portfolio Analytics Dashboard - Development Startup Script
# Starts both frontend and backend servers concurrently

echo "🚀 Starting Portfolio Analytics Dashboard..."
echo "==========================================="

# Function to cleanup processes on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down servers..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Start backend server
echo "📊 Starting Backend (Python FastAPI) on port 8000..."
cd backend
"../.venv/bin/python" run.py &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to start
sleep 3

# Start frontend server
echo "🌐 Starting Frontend (React) on port 8080..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

# Wait a moment for frontend to start
sleep 3

echo ""
echo "✅ Both servers are running!"
echo "🌐 Frontend: http://localhost:8080"
echo "📊 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for user interrupt
wait
