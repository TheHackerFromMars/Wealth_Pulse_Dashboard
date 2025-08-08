# Portfolio Analytics Backend

A FastAPI-based backend service for the Portfolio Analytics Dashboard.

## Features

- **4 Core API Endpoints:**
  - `GET /api/portfolio/holdings` - Complete list of stock investments
  - `GET /api/portfolio/allocation` - Asset distribution by sectors and market cap
  - `GET /api/portfolio/performance` - Historical performance vs benchmarks
  - `GET /api/portfolio/summary` - Key portfolio metrics and insights

- **Data Source:** Reads from Excel file (`Sample Portfolio Dataset for Assignment.xlsx`)
- **Auto-calculated metrics:** Gain/loss, percentages, allocations
- **CORS enabled** for frontend integration
- **Type safety** with Pydantic models

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   python run.py
   ```

3. **API will be available at:**
   - Main API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── models.py        # Pydantic models
│   └── data_service.py  # Data processing logic
├── data/
│   └── Sample Portfolio Dataset for Assignment.xlsx
├── requirements.txt
├── run.py              # Server startup script
└── README.md
```

## API Endpoints

### GET /api/portfolio/holdings
Returns enriched holdings data with calculated gains/losses.

### GET /api/portfolio/allocation  
Returns sector and market cap allocation percentages.

### GET /api/portfolio/performance
Returns historical timeline and performance metrics.

### GET /api/portfolio/summary
Returns portfolio overview with top/worst performers.

## Development

- The server runs with auto-reload enabled for development
- Excel data is cached for performance
- Fallback data available if Excel reading fails
- Full error handling with proper HTTP status codes
