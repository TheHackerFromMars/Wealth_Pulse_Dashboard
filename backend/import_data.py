#!/usr/bin/env python3

"""
Data Import Script
Converts Excel data to JSON format for faster API access
Run this script whenever the Excel file is updated
"""

import pandas as pd
import json
import os
from datetime import datetime
from typing import Dict, Any, List

class DataImporter:
    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.excel_file = os.path.join(self.data_dir, 'Sample Portfolio Dataset for Assignment.xlsx')
        self.json_file = os.path.join(self.data_dir, 'portfolio_data.json')
        self.backup_dir = os.path.join(self.data_dir, 'backups')
        
        # Ensure directories exist
        os.makedirs(self.backup_dir, exist_ok=True)
    
    def load_excel_data(self) -> Dict[str, Any]:
        """Load and process all Excel sheets"""
        if not os.path.exists(self.excel_file):
            raise FileNotFoundError(f"Excel file not found: {self.excel_file}")
        
        print(f"📊 Loading Excel file: {self.excel_file}")
        excel_data = pd.read_excel(self.excel_file, sheet_name=None)
        
        processed_data = {
            'metadata': {
                'imported_at': datetime.now().isoformat(),
                'source_file': 'Sample Portfolio Dataset for Assignment.xlsx',
                'version': '1.0'
            },
            'holdings': self._process_holdings(excel_data),
            'historical_performance': self._process_performance(excel_data),
            'sector_allocation': self._process_sector_allocation(excel_data),
            'market_cap_allocation': self._process_market_cap_allocation(excel_data),
            'summary_metrics': self._process_summary(excel_data)
        }
        
        return processed_data
    
    def _process_holdings(self, excel_data: Dict[str, pd.DataFrame]) -> List[Dict[str, Any]]:
        """Process Holdings sheet"""
        if 'Holdings' not in excel_data:
            print("⚠️  Holdings sheet not found, using fallback data")
            return self._get_fallback_holdings()
        
        holdings_df = excel_data['Holdings']
        holdings_data = []
        
        print(f"📈 Processing {len(holdings_df)} holdings...")
        
        for _, row in holdings_df.iterrows():
            # Clean up market cap field
            market_cap = row['Market Cap'].replace(' Cap', '') if pd.notna(row['Market Cap']) else 'Large'
            
            holding = {
                'symbol': str(row['Symbol']).strip(),
                'name': str(row['Company Name']).strip(),
                'quantity': int(row['Quantity']) if pd.notna(row['Quantity']) else 0,
                'avgPrice': float(row['Avg Price ₹']) if pd.notna(row['Avg Price ₹']) else 0.0,
                'currentPrice': float(row['Current Price (₹)']) if pd.notna(row['Current Price (₹)']) else 0.0,
                'sector': str(row['Sector']).strip() if pd.notna(row['Sector']) else 'Unknown',
                'marketCap': market_cap.strip(),
                'exchange': str(row.get('Exchange', 'NSE')).strip() if pd.notna(row.get('Exchange')) else 'NSE'
            }
            
            # Calculate derived values
            holding['value'] = round(holding['quantity'] * holding['currentPrice'], 2)
            holding['invested'] = round(holding['quantity'] * holding['avgPrice'], 2)
            holding['gainLoss'] = round(holding['value'] - holding['invested'], 2)
            holding['gainLossPercent'] = round((holding['gainLoss'] / holding['invested']) * 100, 2) if holding['invested'] > 0 else 0
            
            holdings_data.append(holding)
        
        return holdings_data
    
    def _process_performance(self, excel_data: Dict[str, pd.DataFrame]) -> List[Dict[str, Any]]:
        """Process Historical_Performance sheet"""
        if 'Historical_Performance' not in excel_data:
            print("⚠️  Historical_Performance sheet not found, using fallback data")
            return self._get_fallback_performance()
        
        perf_df = excel_data['Historical_Performance']
        performance_data = []
        
        print(f"📊 Processing {len(perf_df)} performance records...")
        
        for _, row in perf_df.iterrows():
            date_str = row['Date'].strftime('%Y-%m-%d') if pd.notna(row['Date']) else '2024-01-01'
            
            performance_point = {
                'date': date_str,
                'portfolio': float(row['Portfolio Value (₹)']) if pd.notna(row['Portfolio Value (₹)']) else 0,
                'nifty50': float(row['Nifty 50']) if pd.notna(row['Nifty 50']) else 0,
                'gold': float(row['Gold (₹/10g)']) if pd.notna(row['Gold (₹/10g)']) else 0
            }
            
            # Add return percentages if available
            if 'Portfolio Return %' in row:
                performance_point['portfolioReturn'] = float(row['Portfolio Return %']) if pd.notna(row['Portfolio Return %']) else 0
            if 'Nifty 50 Return %' in row:
                performance_point['niftyReturn'] = float(row['Nifty 50 Return %']) if pd.notna(row['Nifty 50 Return %']) else 0
            if 'Gold Return %' in row:
                performance_point['goldReturn'] = float(row['Gold Return %']) if pd.notna(row['Gold Return %']) else 0
            
            performance_data.append(performance_point)
        
        return performance_data
    
    def _process_sector_allocation(self, excel_data: Dict[str, pd.DataFrame]) -> List[Dict[str, Any]]:
        """Process Sector_Allocation sheet"""
        if 'Sector_Allocation' not in excel_data:
            return []
        
        sector_df = excel_data['Sector_Allocation']
        sector_data = []
        
        for _, row in sector_df.iterrows():
            sector_item = {
                'sector': str(row['Sector']).strip(),
                'value': float(row['Value (₹)']) if pd.notna(row['Value (₹)']) else 0,
                'percentage': float(row['Percentage']) * 100 if pd.notna(row['Percentage']) else 0,  # Convert to percentage
                'holdingsCount': int(row['Holdings Count']) if pd.notna(row['Holdings Count']) else 0
            }
            sector_data.append(sector_item)
        
        return sector_data
    
    def _process_market_cap_allocation(self, excel_data: Dict[str, pd.DataFrame]) -> List[Dict[str, Any]]:
        """Process Market_Cap sheet"""
        if 'Market_Cap' not in excel_data:
            return []
        
        cap_df = excel_data['Market_Cap']
        cap_data = []
        
        for _, row in cap_df.iterrows():
            # Clean up market cap name
            market_cap = str(row['Market Cap']).replace(' Cap', '') if pd.notna(row['Market Cap']) else 'Large'
            
            cap_item = {
                'marketCap': market_cap.strip(),
                'value': float(str(row['Value (₹)']).replace(',', '')) if pd.notna(row['Value (₹)']) else 0,
                'percentage': float(row['Percentage']) * 100 if pd.notna(row['Percentage']) else 0,  # Convert to percentage
                'holdingsCount': int(row['Holdings Count']) if pd.notna(row['Holdings Count']) else 0
            }
            cap_data.append(cap_item)
        
        return cap_data
    
    def _process_summary(self, excel_data: Dict[str, pd.DataFrame]) -> Dict[str, Any]:
        """Process Summary sheet"""
        if 'Summary' not in excel_data:
            return {}
        
        summary_df = excel_data['Summary']
        summary_data = {}
        
        # Convert Summary sheet (Metric, Value pairs) to dict
        for _, row in summary_df.iterrows():
            metric = str(row['Metric']).strip()
            value = row['Value']
            
            # Clean up value (remove commas, convert to float if numeric)
            if pd.notna(value):
                value_str = str(value).replace(',', '').replace('₹', '').strip()
                try:
                    value_clean = float(value_str)
                except:
                    value_clean = value_str
            else:
                value_clean = 0
            
            summary_data[metric] = value_clean
        
        return summary_data
    
    def _get_fallback_holdings(self) -> List[Dict[str, Any]]:
        """Fallback holdings data"""
        return [
            {"symbol": "RELIANCE", "name": "Reliance Industries Ltd", "quantity": 50, "avgPrice": 2450, "currentPrice": 2680.5, "sector": "Energy", "marketCap": "Large", "exchange": "NSE"},
            {"symbol": "INFY", "name": "Infosys Limited", "quantity": 100, "avgPrice": 1800, "currentPrice": 2010.75, "sector": "Technology", "marketCap": "Large", "exchange": "NSE"},
            {"symbol": "TCS", "name": "Tata Consultancy Services", "quantity": 75, "avgPrice": 3200, "currentPrice": 3450.25, "sector": "Technology", "marketCap": "Large", "exchange": "NSE"},
            {"symbol": "HDFCBANK", "name": "HDFC Bank Limited", "quantity": 80, "avgPrice": 1650, "currentPrice": 1580.3, "sector": "Banking", "marketCap": "Large", "exchange": "NSE"},
            {"symbol": "ICICIBANK", "name": "ICICI Bank Limited", "quantity": 60, "avgPrice": 1100, "currentPrice": 1235.8, "sector": "Banking", "marketCap": "Large", "exchange": "NSE"},
        ]
    
    def _get_fallback_performance(self) -> List[Dict[str, Any]]:
        """Fallback performance data"""
        return [
            {"date": "2024-01-01", "portfolio": 1500000, "nifty50": 21000, "gold": 62000},
            {"date": "2024-02-01", "portfolio": 1520000, "nifty50": 21300, "gold": 61800},
            {"date": "2024-03-01", "portfolio": 1540000, "nifty50": 22100, "gold": 64500},
        ]
    
    def save_json(self, data: Dict[str, Any]) -> None:
        """Save processed data to JSON file"""
        # Create backup of existing JSON file
        if os.path.exists(self.json_file):
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = os.path.join(self.backup_dir, f'portfolio_data_backup_{timestamp}.json')
            os.rename(self.json_file, backup_file)
            print(f"💾 Backed up existing data to: {backup_file}")
        
        # Save new data
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved processed data to: {self.json_file}")
        print(f"📁 File size: {os.path.getsize(self.json_file) / 1024:.1f} KB")
    
    def import_data(self) -> Dict[str, Any]:
        """Main import process"""
        print("🚀 Starting data import process...")
        
        try:
            # Load and process Excel data
            processed_data = self.load_excel_data()
            
            # Save to JSON
            self.save_json(processed_data)
            
            # Print summary
            self._print_summary(processed_data)
            
            print("🎉 Data import completed successfully!")
            return processed_data
            
        except Exception as e:
            print(f"❌ Error during import: {e}")
            raise
    
    def _print_summary(self, data: Dict[str, Any]) -> None:
        """Print import summary"""
        print("\n📊 Import Summary:")
        print("=" * 40)
        print(f"Holdings: {len(data['holdings'])} stocks")
        print(f"Performance Records: {len(data['historical_performance'])} data points")
        print(f"Sectors: {len(data['sector_allocation'])} sectors")
        print(f"Market Caps: {len(data['market_cap_allocation'])} categories")
        print(f"Imported at: {data['metadata']['imported_at']}")

def main():
    """Command line interface"""
    importer = DataImporter()
    importer.import_data()

if __name__ == "__main__":
    main()
