from pydantic import BaseModel
from typing import Dict, List, Literal
from datetime import datetime

class Holding(BaseModel):
    symbol: str
    name: str
    quantity: int
    avgPrice: float
    currentPrice: float
    sector: str
    marketCap: Literal["Large", "Mid", "Small"]
    value: float
    gainLoss: float
    gainLossPercent: float

class AllocationItem(BaseModel):
    value: float
    percentage: float
    count: int = 0

class Allocation(BaseModel):
    bySector: Dict[str, AllocationItem]
    byMarketCap: Dict[str, AllocationItem]

class TimelinePoint(BaseModel):
    date: str
    portfolio: float
    nifty50: float
    gold: float

class Returns(BaseModel):
    oneMonth: float = 0.0  # Using oneMonth instead of 1month as field name
    threeMonths: float = 0.0
    oneYear: float = 0.0
    
    class Config:
        # Map the JSON field names to Python field names
        alias_generator = lambda field_name: {
            'oneMonth': '1month',
            'threeMonths': '3months', 
            'oneYear': '1year'
        }.get(field_name, field_name)
        populate_by_name = True

class Performance(BaseModel):
    timeline: List[TimelinePoint]
    returns: Dict[str, Returns]

class TopPerformer(BaseModel):
    symbol: str
    name: str
    gainPercent: float

class Summary(BaseModel):
    totalValue: float
    totalInvested: float
    totalGainLoss: float
    totalGainLossPercent: float
    holdingsCount: int
    topPerformer: TopPerformer
    worstPerformer: TopPerformer
    diversificationScore: float
    riskLevel: str
