// Types and API helpers for portfolio endpoints with automatic fallback to local mock data when Supabase is not configured.
export type Holding = {
  symbol: string;
  name: string;
  quantity: number;
  avgPrice: number;
  currentPrice: number;
  sector: string;
  marketCap: 'Large' | 'Mid' | 'Small';
  value: number;
  gainLoss: number;
  gainLossPercent: number;
};

export type Allocation = {
  bySector: Record<string, { value: number; percentage: number; count?: number }>;
  byMarketCap: Record<string, { value: number; percentage: number; count?: number }>;
};

export type Performance = {
  timeline: { date: string; portfolio: number; nifty50: number; gold: number }[];
  returns: {
    portfolio: { '1month': number; '3months': number; '1year': number };
    nifty50: { '1month': number; '3months': number; '1year': number };
    gold: { '1month': number; '3months': number; '1year': number };
  };
};

export type Summary = {
  totalValue: number;
  totalInvested: number;
  totalGainLoss: number;
  totalGainLossPercent: number;
  holdingsCount: number;
  topPerformer: { symbol: string; name: string; gainPercent: number };
  worstPerformer: { symbol: string; name: string; gainPercent: number };
  diversificationScore: number;
  riskLevel: string;
};

const base: string | undefined = (import.meta as any).env?.VITE_SUPABASE_URL;
const hasSupabase = typeof base === 'string' && base.length > 0;
const baseUrl = hasSupabase ? `${base}/functions/v1` : 'http://localhost:8000';

async function getJSON<T>(path: string): Promise<T> {
  const res = await fetch(`${baseUrl}${path}`);
  if (!res.ok) throw new Error(`API error ${res.status}`);
  return res.json();
}

// ---------- Local mock fallback (mirrors Edge Functions) ----------
const mockHoldingsBase = [
  { symbol: 'RELIANCE', name: 'Reliance Industries Ltd', quantity: 50, avgPrice: 2450, currentPrice: 2680.5, sector: 'Energy', marketCap: 'Large' as const },
  { symbol: 'INFY', name: 'Infosys Limited', quantity: 100, avgPrice: 1800, currentPrice: 2010.75, sector: 'Technology', marketCap: 'Large' as const },
  { symbol: 'TCS', name: 'Tata Consultancy Services', quantity: 75, avgPrice: 3200, currentPrice: 3450.25, sector: 'Technology', marketCap: 'Large' as const },
  { symbol: 'HDFCBANK', name: 'HDFC Bank Limited', quantity: 80, avgPrice: 1650, currentPrice: 1580.3, sector: 'Banking', marketCap: 'Large' as const },
  { symbol: 'ICICIBANK', name: 'ICICI Bank Limited', quantity: 60, avgPrice: 1100, currentPrice: 1235.8, sector: 'Banking', marketCap: 'Large' as const },
  { symbol: 'BHARTIARTL', name: 'Bharti Airtel Limited', quantity: 120, avgPrice: 850, currentPrice: 920.45, sector: 'Telecommunications', marketCap: 'Large' as const },
  { symbol: 'ITC', name: 'ITC Limited', quantity: 200, avgPrice: 420, currentPrice: 465.2, sector: 'Consumer Goods', marketCap: 'Large' as const },
  { symbol: 'BAJFINANCE', name: 'Bajaj Finance Limited', quantity: 25, avgPrice: 6800, currentPrice: 7150.6, sector: 'Financial Services', marketCap: 'Large' as const },
  { symbol: 'ASIANPAINT', name: 'Asian Paints Limited', quantity: 40, avgPrice: 3100, currentPrice: 2890.75, sector: 'Consumer Discretionary', marketCap: 'Large' as const },
  { symbol: 'MARUTI', name: 'Maruti Suzuki India', quantity: 30, avgPrice: 9500, currentPrice: 10250.3, sector: 'Automotive', marketCap: 'Large' as const },
  { symbol: 'WIPRO', name: 'Wipro Limited', quantity: 150, avgPrice: 450, currentPrice: 485.6, sector: 'Technology', marketCap: 'Large' as const },
  { symbol: 'TATAMOTORS', name: 'Tata Motors Limited', quantity: 100, avgPrice: 650, currentPrice: 720.85, sector: 'Automotive', marketCap: 'Large' as const },
  { symbol: 'TECHM', name: 'Tech Mahindra Limited', quantity: 80, avgPrice: 1200, currentPrice: 1145.25, sector: 'Technology', marketCap: 'Large' as const },
  { symbol: 'AXISBANK', name: 'Axis Bank Limited', quantity: 90, avgPrice: 980, currentPrice: 1055.4, sector: 'Banking', marketCap: 'Large' as const },
  { symbol: 'SUNPHARMA', name: 'Sun Pharmaceutical', quantity: 60, avgPrice: 1150, currentPrice: 1245.3, sector: 'Healthcare', marketCap: 'Large' as const },
];

function enrichHoldings(): Holding[] {
  return mockHoldingsBase.map(h => {
    const value = +(h.quantity * h.currentPrice).toFixed(2);
    const invested = +(h.quantity * h.avgPrice).toFixed(2);
    const gainLoss = +(value - invested).toFixed(2);
    const gainLossPercent = invested ? +(((value - invested) / invested) * 100).toFixed(2) : 0;
    return { ...h, value, gainLoss, gainLossPercent };
  });
}

function mockAllocation(): Allocation {
  const hs = enrichHoldings();
  const total = hs.reduce((a, b) => a + b.value, 0);
  const bySector: Allocation['bySector'] = {};
  const byMarketCap: Allocation['byMarketCap'] = {};
  hs.forEach(h => {
    bySector[h.sector] ||= { value: 0, percentage: 0 };
    bySector[h.sector].value += h.value;
    byMarketCap[h.marketCap] ||= { value: 0, percentage: 0 };
    byMarketCap[h.marketCap].value += h.value;
  });
  for (const k in bySector) bySector[k].percentage = +((bySector[k].value / total) * 100).toFixed(2);
  for (const k in byMarketCap) byMarketCap[k].percentage = +((byMarketCap[k].value / total) * 100).toFixed(2);
  return { bySector, byMarketCap };
}

const mockTimeline = [
  { date: '2024-01-01', portfolio: 1500000, nifty50: 21000, gold: 62000 },
  { date: '2024-02-01', portfolio: 1520000, nifty50: 21300, gold: 61800 },
  { date: '2024-03-01', portfolio: 1540000, nifty50: 22100, gold: 64500 },
  { date: '2024-04-01', portfolio: 1580000, nifty50: 22800, gold: 66200 },
  { date: '2024-05-01', portfolio: 1620000, nifty50: 23200, gold: 68000 },
  { date: '2024-06-01', portfolio: 1650000, nifty50: 23500, gold: 68500 },
  { date: '2024-07-01', portfolio: 1680000, nifty50: 24100, gold: 69800 },
  { date: '2024-08-01', portfolio: 1720000, nifty50: 24800, gold: 70200 },
  { date: '2024-09-01', portfolio: 1750000, nifty50: 25200, gold: 71500 },
  { date: '2024-10-01', portfolio: 1780000, nifty50: 25600, gold: 72800 },
  { date: '2024-11-01', portfolio: 1820000, nifty50: 26100, gold: 74000 },
  { date: '2024-12-01', portfolio: 1850000, nifty50: 26500, gold: 75200 },
];

function pct(series: number[]) {
  const last = series.at(-1)!;
  const m1 = series.at(-2)!;
  const m3 = series.at(-4)!;
  const first = series[0];
  return {
    '1month': +(((last - m1) / m1) * 100).toFixed(2),
    '3months': +(((last - m3) / m3) * 100).toFixed(2),
    '1year': +(((last - first) / first) * 100).toFixed(2),
  };
}

function mockPerformance(): Performance {
  const portfolioSeries = mockTimeline.map(t => t.portfolio);
  const niftySeries = mockTimeline.map(t => t.nifty50);
  const goldSeries = mockTimeline.map(t => t.gold);
  return { timeline: mockTimeline, returns: { portfolio: pct(portfolioSeries), nifty50: pct(niftySeries), gold: pct(goldSeries) } };
}

function mockSummary(): Summary {
  const hs = enrichHoldings();
  const totalInvested = hs.reduce((a, b) => a + b.quantity * b.avgPrice, 0);
  const totalValue = hs.reduce((a, b) => a + b.value, 0);
  const totalGainLoss = totalValue - totalInvested;
  const totalGainLossPercent = totalInvested ? (totalGainLoss / totalInvested) * 100 : 0;
  const sorted = [...hs].sort((a, b) => b.gainLossPercent - a.gainLossPercent);
  const top = sorted[0];
  const worst = sorted[sorted.length - 1];
  const sectorCount = new Set(hs.map(h => h.sector)).size;
  const diversificationScore = Math.min(10, +(sectorCount / 8 * 10).toFixed(1));
  const riskLevel = totalGainLossPercent > 15 ? 'Moderate' : 'Low';
  return {
    totalValue: +totalValue.toFixed(2),
    totalInvested: +totalInvested.toFixed(2),
    totalGainLoss: +totalGainLoss.toFixed(2),
    totalGainLossPercent: +totalGainLossPercent.toFixed(2),
    holdingsCount: hs.length,
    topPerformer: { symbol: top.symbol, name: top.name, gainPercent: +top.gainLossPercent.toFixed(2) },
    worstPerformer: { symbol: worst.symbol, name: worst.name, gainPercent: +worst.gainLossPercent.toFixed(2) },
    diversificationScore,
    riskLevel,
  };
}

// ---------- Public API ----------
export const PortfolioAPI = {
  holdings: () => getJSON<Holding[]>(`/api/portfolio/holdings`),
  allocation: () => getJSON<Allocation>(`/api/portfolio/allocation`),
  performance: () => getJSON<Performance>(`/api/portfolio/performance`),
  summary: () => getJSON<Summary>(`/api/portfolio/summary`),
};
