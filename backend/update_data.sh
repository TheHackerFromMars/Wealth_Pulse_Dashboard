#!/bin/bash

# Portfolio Data Update Workflow
# 1. Import Excel data to JSON
# 2. Reload data in API server
# 3. Validate all endpoints

echo "🔄 Portfolio Data Update Workflow"
echo "================================="

echo "📊 Step 1: Converting Excel to JSON..."
"/Users/samit.manna/Documents/Passion Projects/wealth-pulse-dash/.venv/bin/python" import_data.py

echo ""
echo "🔄 Step 2: Reloading data in API server..."
curl -X POST http://localhost:8000/api/portfolio/reload

echo ""
echo ""
echo "🧪 Step 3: Validating all endpoints..."
"/Users/samit.manna/Documents/Passion Projects/wealth-pulse-dash/.venv/bin/python" validate.py

echo ""
echo "✅ Data update workflow completed!"
echo "📊 API server is now using the latest data from Excel file."
