# Portfolio Analytics Dashboard

A full-stack portfolio analytics application with a **React TypeScript frontend** and **Python FastAPI backend**.

## 🚀 Features

### Frontend (React + TypeScript)
- **Portfolio Overview Cards** - Total value, gains/losses, holdings count, risk level
- **Asset Allocation Charts** - Interactive pie charts for sector and market cap distribution  
- **Holdings Table** - Sortable, searchable table with all portfolio positions
- **Performance Chart** - Timeline comparison vs Nifty 50 and Gold benchmarks
- **Top Performers** - Best and worst performing stocks with insights

### Backend (Python FastAPI)
- **4 REST API Endpoints** matching the assignment requirements exactly
- **Excel Data Integration** - Reads portfolio data from provided Excel file
- **Real-time Calculations** - Gain/loss, percentages, allocations computed on-the-fly
- **Type Safety** - Pydantic models for request/response validation
- **Auto-generated API Docs** - Interactive Swagger UI at `/docs`

## 📊 API Endpoints

| Endpoint | Description | Returns |
|----------|-------------|---------|
| `GET /api/portfolio/holdings` | Complete holdings with calculations | List of enriched stock positions |
| `GET /api/portfolio/allocation` | Sector & market cap distribution | Percentage breakdowns with counts |
| `GET /api/portfolio/performance` | Historical timeline vs benchmarks | Performance data with returns |
| `GET /api/portfolio/summary` | Key portfolio metrics | Overview with top/worst performers |

## 🛠️ Technology Stack

### Frontend
- **React 18** with **TypeScript** for type safety
- **Vite** for fast development and building
- **Shadcn/ui** + **Tailwind CSS** for modern, responsive design
- **Recharts** for interactive data visualizations
- **TanStack Query** for efficient API state management
- **React Router** for navigation

### Backend  
- **Python 3.12** with **FastAPI** for high-performance APIs
- **JSON-based data pipeline** for optimal performance (Excel → JSON → API)
- **Automatic data import** from Excel with timestamped backups
- **In-memory caching** for sub-millisecond API responses
- **Pydantic** for data validation and serialization
- **Uvicorn** as ASGI server with auto-reload

## 🚦 Quick Start

### Prerequisites
- **Node.js 18+** (for frontend)
- **Python 3.12+** (for backend)

### 1. Setup & Run Backend (Python FastAPI)

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies (virtual environment already configured)
pip install -r requirements.txt

# Import Excel data to JSON (first time or after Excel updates)
python import_data.py

# Start the API server
python run.py
```

Backend will run on: **http://localhost:8000**
- API Documentation: **http://localhost:8000/docs**
- Alternative docs: **http://localhost:8000/redoc**

### 2. Setup & Run Frontend (React)

```bash
# Navigate to frontend directory
cd frontend

# Install frontend dependencies
npm install

# Start the development server  
npm run dev
```

Frontend will run on: **http://localhost:8080**

### 3. Test Integration

```bash
# Run the integration test script
chmod +x test-integration.sh
./test-integration.sh
```

### 4. Update Data (When Excel File Changes)

```bash
# Complete data update workflow
cd backend
./update_data.sh
```

This will:
1. Import latest Excel data to JSON
2. Reload API server cache
3. Validate all endpoints

## 📁 Project Structure

```
wealth-pulse-dash/
├── frontend/                    # React TypeScript Frontend
│   ├── src/
│   │   ├── components/dashboard/    # Dashboard components
│   │   ├── api/portfolio.ts         # API client
│   │   ├── pages/Index.tsx          # Main dashboard page
│   │   └── ...
│   ├── package.json
│   └── vite.config.ts
├── backend/                     # Python FastAPI Backend
│   ├── app/
│   │   ├── main.py                  # FastAPI application
│   │   ├── models.py                # Pydantic models
│   │   ├── data_service.py          # JSON processing logic
│   │   └── __init__.py
│   ├── data/
│   │   ├── portfolio_data.json      # Generated JSON cache
│   │   ├── Sample Portfolio Dataset for Assignment.xlsx
│   │   └── backups/                 # Timestamped backups
│   ├── requirements.txt
│   ├── run.py                       # Server startup
│   └── README.md
└── start-dev.sh                     # Development startup script
```

## 📈 Data Source

The application reads portfolio data from **`Sample Portfolio Dataset for Assignment.xlsx`** with the following sheets:

- **Holdings** - Stock positions with quantities, prices, sectors
- **Historical_Performance** - Timeline data for performance charts  
- **Summary** - Portfolio overview metrics
- **Sector_Allocation** - Sector distribution data
- **Market_Cap** - Market cap allocation data
- **Top_Performers** - Best/worst performing stocks

## 🔧 Development

### Frontend Development
```bash
cd frontend
npm run dev     # Start with hot reload
npm run build   # Production build
npm run preview # Preview production build
```

### Backend Development
```bash
python run.py   # Start with auto-reload
# API will automatically restart when code changes
```

### Adding New Features
1. **Backend**: Add new endpoints in `backend/app/main.py`, models in `backend/app/models.py`
2. **Frontend**: Add API calls in `frontend/src/api/portfolio.ts`, components in `frontend/src/components/`

## 🌟 Key Features Implemented

### ✅ Backend Requirements Met
- [x] All 4 required API endpoints implemented exactly as specified
- [x] Data calculations (gain/loss, percentages) working correctly
- [x] Error handling with proper HTTP status codes
- [x] CORS enabled for frontend integration
- [x] Clean, documented code structure

### ✅ Frontend Requirements Met  
- [x] Portfolio overview cards with color-coded gains/losses
- [x] Interactive asset allocation visualizations
- [x] Sortable, searchable holdings table
- [x] Performance comparison charts with hover effects
- [x] Top performers section with insights
- [x] Responsive design for mobile/desktop
- [x] Loading states and error handling

## 🚀 Deployment Ready

The application is architected for easy deployment:

- **Backend**: Can be deployed to any platform supporting Python (Heroku, Railway, DigitalOcean, etc.)
- **Frontend**: Can be deployed to static hosting (Vercel, Netlify, GitHub Pages, etc.)
- **Environment Variables**: Backend URL configurable via frontend environment

## 🧪 Testing

- Integration test script validates all API endpoints
- Frontend automatically handles API failures gracefully
- Type safety ensures data consistency between frontend/backend

---

**Portfolio Analytics Dashboard** - Built with modern web technologies for optimal performance and user experience.
- Edit files directly within the Codespace and commit and push your changes once you're done.

## What technologies are used for this project?

This project is built with:

- Vite
- TypeScript
- React
- shadcn-ui
- Tailwind CSS

## How can I deploy this project?

Simply open [Lovable](https://lovable.dev/projects/1c9d5a15-1bf9-442b-8c61-93c37081db95) and click on Share -> Publish.

## Can I connect a custom domain to my Lovable project?

Yes, you can!

To connect a domain, navigate to Project > Settings > Domains and click Connect Domain.

Read more here: [Setting up a custom domain](https://docs.lovable.dev/tips-tricks/custom-domain#step-by-step-guide)
