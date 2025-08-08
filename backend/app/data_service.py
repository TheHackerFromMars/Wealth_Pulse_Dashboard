import json
import os
from typing import List, Dict, Any
from .models import Holding, Allocation, AllocationItem, Performance, TimelinePoint, Returns, Summary, TopPerformer

class PortfolioDataService:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), '..', 'data')
        self.json_file = os.path.join(self.data_path, 'portfolio_data.json')
        self._portfolio_data = None
        
    def _load_portfolio_data(self) -> Dict[str, Any]:
        """Load portfolio data from JSON file"""
        if self._portfolio_data is None:
            try:
                if not os.path.exists(self.json_file):
                    raise FileNotFoundError(f"Portfolio data file not found: {self.json_file}")
                
                with open(self.json_file, 'r', encoding='utf-8') as f:
                    self._portfolio_data = json.load(f)
                
                print(f"📊 Loaded portfolio data from JSON (imported: {self._portfolio_data['metadata']['imported_at']})")
                
            except Exception as e:
                print(f"Error loading JSON data, using fallback: {e}")
                self._portfolio_data = self._get_fallback_data()
        
        return self._portfolio_data
    
    def _get_fallback_data(self) -> Dict[str, Any]:
        """Fallback data structure when JSON file is not available"""
        return {
            'metadata': {
                'imported_at': '2024-01-01T00:00:00',
                'source_file': 'fallback_data',
                'version': '1.0'
            },
            'holdings': [
                {"symbol": "RELIANCE", "name": "Reliance Industries Ltd", "quantity": 50, "avgPrice": 2450, "currentPrice": 2680.5, "sector": "Energy", "marketCap": "Large", "exchange": "NSE", "value": 134025.0, "invested": 122500.0, "gainLoss": 11525.0, "gainLossPercent": 9.41},
                {"symbol": "INFY", "name": "Infosys Limited", "quantity": 100, "avgPrice": 1800, "currentPrice": 2010.75, "sector": "Technology", "marketCap": "Large", "exchange": "NSE", "value": 201075.0, "invested": 180000.0, "gainLoss": 21075.0, "gainLossPercent": 11.71},
                {"symbol": "TCS", "name": "Tata Consultancy Services", "quantity": 75, "avgPrice": 3200, "currentPrice": 3450.25, "sector": "Technology", "marketCap": "Large", "exchange": "NSE", "value": 258768.75, "invested": 240000.0, "gainLoss": 18768.75, "gainLossPercent": 7.82},
                {"symbol": "HDFCBANK", "name": "HDFC Bank Limited", "quantity": 80, "avgPrice": 1650, "currentPrice": 1580.3, "sector": "Banking", "marketCap": "Large", "exchange": "NSE", "value": 126424.0, "invested": 132000.0, "gainLoss": -5576.0, "gainLossPercent": -4.22},
                {"symbol": "ICICIBANK", "name": "ICICI Bank Limited", "quantity": 60, "avgPrice": 1100, "currentPrice": 1235.8, "sector": "Banking", "marketCap": "Large", "exchange": "NSE", "value": 74148.0, "invested": 66000.0, "gainLoss": 8148.0, "gainLossPercent": 12.35},
            ],
            'historical_performance': [
                {"date": "2024-01-01", "portfolio": 1500000, "nifty50": 21000, "gold": 62000},
                {"date": "2024-02-01", "portfolio": 1520000, "nifty50": 21300, "gold": 61800},
                {"date": "2024-03-01", "portfolio": 1540000, "nifty50": 22100, "gold": 64500},
                {"date": "2024-04-01", "portfolio": 1580000, "nifty50": 22800, "gold": 66200},
                {"date": "2024-05-01", "portfolio": 1620000, "nifty50": 23200, "gold": 68000},
                {"date": "2024-06-01", "portfolio": 1650000, "nifty50": 23500, "gold": 68500},
                {"date": "2024-07-01", "portfolio": 1680000, "nifty50": 24100, "gold": 69800},
                {"date": "2024-08-01", "portfolio": 1720000, "nifty50": 24800, "gold": 70200},
                {"date": "2024-09-01", "portfolio": 1750000, "nifty50": 25200, "gold": 71500},
                {"date": "2024-10-01", "portfolio": 1780000, "nifty50": 25600, "gold": 72800},
                {"date": "2024-11-01", "portfolio": 1820000, "nifty50": 26100, "gold": 74000},
                {"date": "2024-12-01", "portfolio": 1850000, "nifty50": 26500, "gold": 75200},
            ],
            'sector_allocation': [],
            'market_cap_allocation': [],
            'summary_metrics': {}
        }
    
    def get_holdings(self) -> List[Holding]:
        """Get enriched holdings with calculated values"""
        portfolio_data = self._load_portfolio_data()
        holdings_data = portfolio_data.get('holdings', [])
        
        enriched_holdings = []
        for holding_dict in holdings_data:
            # The JSON already has calculated values, just create Holding objects
            enriched_holding = Holding(
                symbol=holding_dict['symbol'],
                name=holding_dict['name'],
                quantity=holding_dict['quantity'],
                avgPrice=holding_dict['avgPrice'],
                currentPrice=holding_dict['currentPrice'],
                sector=holding_dict['sector'],
                marketCap=holding_dict['marketCap'],
                value=holding_dict.get('value', holding_dict['quantity'] * holding_dict['currentPrice']),
                gainLoss=holding_dict.get('gainLoss', 0),
                gainLossPercent=holding_dict.get('gainLossPercent', 0)
            )
            enriched_holdings.append(enriched_holding)
        
        return enriched_holdings
    
    def get_allocation(self) -> Allocation:
        """Calculate portfolio allocation by sector and market cap"""
        portfolio_data = self._load_portfolio_data()
        
        # Try to use pre-calculated allocation data from JSON
        sector_data = portfolio_data.get('sector_allocation', [])
        market_cap_data = portfolio_data.get('market_cap_allocation', [])
        
        # If pre-calculated data exists, use it
        if sector_data and market_cap_data:
            by_sector_items = {}
            for sector_item in sector_data:
                by_sector_items[sector_item['sector']] = AllocationItem(
                    value=round(sector_item['value'], 2),
                    percentage=round(sector_item['percentage'], 2),
                    count=sector_item.get('holdingsCount', 0)
                )
            
            by_market_cap_items = {}
            for cap_item in market_cap_data:
                by_market_cap_items[cap_item['marketCap']] = AllocationItem(
                    value=round(cap_item['value'], 2),
                    percentage=round(cap_item['percentage'], 2),
                    count=cap_item.get('holdingsCount', 0)
                )
        else:
            # Calculate from holdings if pre-calculated data not available
            holdings = self.get_holdings()
            total_value = sum(h.value for h in holdings)
            
            # Calculate by sector
            by_sector = {}
            for holding in holdings:
                if holding.sector not in by_sector:
                    by_sector[holding.sector] = {"value": 0, "count": 0}
                by_sector[holding.sector]["value"] += holding.value
                by_sector[holding.sector]["count"] += 1
            
            # Calculate by market cap
            by_market_cap = {}
            for holding in holdings:
                if holding.marketCap not in by_market_cap:
                    by_market_cap[holding.marketCap] = {"value": 0, "count": 0}
                by_market_cap[holding.marketCap]["value"] += holding.value
                by_market_cap[holding.marketCap]["count"] += 1
            
            # Convert to allocation items with percentages
            by_sector_items = {}
            for sector, data in by_sector.items():
                percentage = round((data["value"] / total_value) * 100, 2) if total_value > 0 else 0
                by_sector_items[sector] = AllocationItem(
                    value=round(data["value"], 2),
                    percentage=percentage,
                    count=data["count"]
                )
            
            by_market_cap_items = {}
            for cap, data in by_market_cap.items():
                percentage = round((data["value"] / total_value) * 100, 2) if total_value > 0 else 0
                by_market_cap_items[cap] = AllocationItem(
                    value=round(data["value"], 2),
                    percentage=percentage,
                    count=data["count"]
                )
        
        return Allocation(
            bySector=by_sector_items,
            byMarketCap=by_market_cap_items
        )
    
    def get_performance(self) -> Performance:
        """Get performance data with timeline and returns"""
        portfolio_data = self._load_portfolio_data()
        performance_data = portfolio_data.get('historical_performance', [])
        
        # Create timeline from JSON data
        timeline = []
        for perf_point in performance_data:
            timeline.append(TimelinePoint(
                date=perf_point['date'],
                portfolio=float(perf_point['portfolio']),
                nifty50=float(perf_point['nifty50']),
                gold=float(perf_point['gold'])
            ))
        
        def calculate_returns(series: List[float]) -> Returns:
            if len(series) < 2:
                return Returns(oneMonth=0, threeMonths=0, oneYear=0)
                
            last = series[-1]
            one_month = round(((last - series[-2]) / series[-2]) * 100, 2) if len(series) >= 2 and series[-2] != 0 else 0
            three_months = round(((last - series[-4]) / series[-4]) * 100, 2) if len(series) >= 4 and series[-4] != 0 else 0
            one_year = round(((last - series[0]) / series[0]) * 100, 2) if len(series) >= 1 and series[0] != 0 else 0
            
            return Returns(
                oneMonth=one_month,
                threeMonths=three_months,
                oneYear=one_year
            )
        
        portfolio_series = [t.portfolio for t in timeline]
        nifty_series = [t.nifty50 for t in timeline]
        gold_series = [t.gold for t in timeline]
        
        returns = {
            "portfolio": calculate_returns(portfolio_series),
            "nifty50": calculate_returns(nifty_series),
            "gold": calculate_returns(gold_series)
        }
        
        return Performance(timeline=timeline, returns=returns)
    
    def get_summary(self) -> Summary:
        """Get portfolio summary with key metrics"""
        holdings = self.get_holdings()
        
        total_invested = sum(h.quantity * h.avgPrice for h in holdings)
        total_value = sum(h.value for h in holdings)
        total_gain_loss = total_value - total_invested
        total_gain_loss_percent = round((total_gain_loss / total_invested) * 100, 2) if total_invested > 0 else 0
        
        # Find top and worst performers
        sorted_holdings = sorted(holdings, key=lambda h: h.gainLossPercent, reverse=True)
        top_performer = sorted_holdings[0]
        worst_performer = sorted_holdings[-1]
        
        # Calculate diversification score
        unique_sectors = len(set(h.sector for h in holdings))
        diversification_score = min(10.0, round((unique_sectors / 8) * 10, 1))
        
        # Determine risk level
        risk_level = "Moderate" if total_gain_loss_percent > 15 else "Low"
        
        return Summary(
            totalValue=round(total_value, 2),
            totalInvested=round(total_invested, 2),
            totalGainLoss=round(total_gain_loss, 2),
            totalGainLossPercent=total_gain_loss_percent,
            holdingsCount=len(holdings),
            topPerformer=TopPerformer(
                symbol=top_performer.symbol,
                name=top_performer.name,
                gainPercent=top_performer.gainLossPercent
            ),
            worstPerformer=TopPerformer(
                symbol=worst_performer.symbol,
                name=worst_performer.name,
                gainPercent=worst_performer.gainLossPercent
            ),
            diversificationScore=diversification_score,
            riskLevel=risk_level
        )
    
    def reload_data(self) -> None:
        """Force reload data from JSON file (useful after data import)"""
        self._portfolio_data = None
        print("🔄 Portfolio data cache cleared, will reload on next request")

# Create a singleton instance
portfolio_service = PortfolioDataService()
