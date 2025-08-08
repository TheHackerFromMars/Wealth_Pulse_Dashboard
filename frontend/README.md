# Portfolio Analytics Dashboard - Frontend

A modern React TypeScript frontend for the Portfolio Analytics Dashboard.

## 🚀 Features

- **Portfolio Overview Cards** - Total value, gains/losses, holdings count, risk level
- **Asset Allocation Charts** - Interactive pie charts for sector and market cap distribution  
- **Holdings Table** - Sortable, searchable table with all portfolio positions
- **Performance Chart** - Timeline comparison vs Nifty 50 and Gold benchmarks
- **Top Performers** - Best and worst performing stocks with insights
- **Responsive Design** - Works seamlessly on desktop and mobile

## 🛠️ Technology Stack

- **React 18** with **TypeScript** for type safety
- **Vite** for fast development and building
- **Shadcn/ui** + **Tailwind CSS** for modern, responsive design
- **Recharts** for interactive data visualizations
- **TanStack Query** for efficient API state management
- **React Router** for navigation

## 🚦 Quick Start

### Prerequisites
- **Node.js 18+**

### Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will run on: **http://localhost:8080**

### Production Build

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── dashboard/           # Dashboard-specific components
│   │   │   ├── AllocationCharts.tsx
│   │   │   ├── HoldingsTable.tsx
│   │   │   ├── OverviewCards.tsx
│   │   │   ├── PerformanceChart.tsx
│   │   │   └── TopPerformers.tsx
│   │   ├── ui/                  # Reusable UI components (shadcn/ui)
│   │   └── SEO.tsx
│   ├── api/
│   │   └── portfolio.ts         # API client for backend integration
│   ├── pages/
│   │   ├── Index.tsx           # Main dashboard page
│   │   └── NotFound.tsx
│   ├── hooks/                   # Custom React hooks
│   ├── lib/
│   │   └── utils.ts            # Utility functions
│   ├── App.tsx                 # Main app component
│   ├── main.tsx                # App entry point
│   └── index.css               # Global styles
├── public/                      # Static assets
├── index.html                   # HTML template
├── vite.config.ts              # Vite configuration
├── tailwind.config.ts          # Tailwind CSS configuration
├── tsconfig.json               # TypeScript configuration
└── package.json                # Dependencies and scripts
```

## 🔌 Backend Integration

The frontend connects to the Python FastAPI backend running on port 8000.

### API Configuration

The API base URL is configured in `src/api/portfolio.ts`:

```typescript
const baseUrl = 'http://localhost:8000';
```

### API Endpoints Used

- `GET /api/portfolio/holdings` - Stock holdings data
- `GET /api/portfolio/allocation` - Sector and market cap allocation
- `GET /api/portfolio/performance` - Historical performance data
- `GET /api/portfolio/summary` - Portfolio summary metrics

## 🎨 UI Components

### Dashboard Components

- **OverviewCards** - Key portfolio metrics with color-coded gains/losses
- **AllocationCharts** - Interactive pie charts using Recharts
- **HoldingsTable** - Sortable table with search functionality
- **PerformanceChart** - Line chart showing portfolio vs benchmarks
- **TopPerformers** - Cards showing best and worst performing stocks

### Design System

- **Shadcn/ui** - Modern, accessible components
- **Tailwind CSS** - Utility-first CSS framework
- **Responsive** - Mobile-first design approach
- **Dark/Light Mode** - Theme support (can be extended)

## 🧪 Development

### Available Scripts

```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run preview  # Preview production build
npm run lint     # Run ESLint
```

### Code Quality

- **TypeScript** - Full type safety
- **ESLint** - Code linting
- **Prettier** - Code formatting (can be added)

### Hot Module Replacement

The development server supports HMR for instant updates during development.

## 🚀 Deployment

### Static Hosting

The frontend can be deployed to any static hosting service:

- **Vercel** - `vercel deploy`
- **Netlify** - Connect GitHub repository
- **GitHub Pages** - Static site hosting
- **AWS S3** - Static website hosting

### Environment Variables

For production deployment, set the backend API URL:

```bash
# .env.production
VITE_API_BASE_URL=https://your-backend-api.com
```

Update `src/api/portfolio.ts` to use the environment variable:

```typescript
const baseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';
```

## 📱 Responsive Design

The dashboard is fully responsive and works on:

- **Desktop** - Full dashboard with all components
- **Tablet** - Optimized layout for medium screens
- **Mobile** - Stacked layout for small screens

## ✨ Features

### Interactive Elements

- **Sortable Tables** - Click column headers to sort
- **Search Functionality** - Filter holdings by symbol, name, or sector
- **Hover Effects** - Chart tooltips and component hover states
- **Color Coding** - Green for gains, red for losses

### Loading States

- **Skeleton Loaders** - Smooth loading experience
- **Error Handling** - Graceful error messages
- **Loading Indicators** - Clear feedback during data fetching

## 🔧 Customization

### Adding New Components

1. Create component in `src/components/dashboard/`
2. Import and use in `src/pages/Index.tsx`
3. Add any new API calls to `src/api/portfolio.ts`

### Styling

- Use Tailwind classes for styling
- Extend theme in `tailwind.config.ts`
- Add custom components to `src/components/ui/`

---

**Portfolio Analytics Frontend** - Built with modern React for optimal performance and user experience.
