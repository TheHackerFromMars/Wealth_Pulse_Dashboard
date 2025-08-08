#!/usr/bin/env python3

"""
Portfolio Analytics Backend - Validation Script
Tests all API endpoints and validates data integrity
"""

import requests
import json
import sys
from typing import Dict, Any

BASE_URL = "http://localhost:8000"

def test_endpoint(endpoint: str, expected_fields: list) -> bool:
    """Test an API endpoint and validate response structure"""
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print(f"❌ {endpoint}: HTTP {response.status_code}")
            return False
        
        data = response.json()
        
        # Basic validation for different endpoint types
        if endpoint == "/api/portfolio/holdings":
            if not isinstance(data, list) or len(data) == 0:
                print(f"❌ {endpoint}: Expected non-empty list")
                return False
            # Check first holding structure
            holding = data[0]
            for field in expected_fields:
                if field not in holding:
                    print(f"❌ {endpoint}: Missing field '{field}'")
                    return False
        else:
            # For dict responses
            for field in expected_fields:
                if field not in data:
                    print(f"❌ {endpoint}: Missing field '{field}'")
                    return False
        
        print(f"✅ {endpoint}: OK ({len(json.dumps(data))} chars)")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ {endpoint}: Connection error - {e}")
        return False
    except json.JSONDecodeError:
        print(f"❌ {endpoint}: Invalid JSON response")
        return False
    except Exception as e:
        print(f"❌ {endpoint}: Unexpected error - {e}")
        return False

def main():
    print("🧪 Portfolio Analytics API Validation")
    print("=====================================")
    
    # Test server health
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code == 200:
            print("✅ Server health: OK")
        else:
            print(f"❌ Server health: HTTP {response.status_code}")
            sys.exit(1)
    except:
        print("❌ Server health: Cannot connect to backend")
        print("💡 Make sure backend is running: cd backend && python run.py")
        sys.exit(1)
    
    # Define test cases
    tests = [
        {
            "endpoint": "/api/portfolio/holdings",
            "fields": ["symbol", "name", "quantity", "avgPrice", "currentPrice", "sector", "marketCap", "value", "gainLoss", "gainLossPercent"]
        },
        {
            "endpoint": "/api/portfolio/allocation", 
            "fields": ["bySector", "byMarketCap"]
        },
        {
            "endpoint": "/api/portfolio/performance",
            "fields": ["timeline", "returns"]
        },
        {
            "endpoint": "/api/portfolio/summary",
            "fields": ["totalValue", "totalInvested", "totalGainLoss", "totalGainLossPercent", "holdingsCount", "topPerformer", "worstPerformer", "diversificationScore", "riskLevel"]
        }
    ]
    
    # Run tests
    all_passed = True
    for test in tests:
        passed = test_endpoint(test["endpoint"], test["fields"])
        all_passed &= passed
    
    print()
    if all_passed:
        print("🎉 All tests passed! Backend is working correctly.")
        print("🌐 Frontend should be able to connect successfully.")
    else:
        print("❌ Some tests failed. Check the backend implementation.")
        sys.exit(1)

if __name__ == "__main__":
    main()
