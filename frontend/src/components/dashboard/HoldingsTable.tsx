import { useMemo, useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { PortfolioAPI, Holding } from "@/api/portfolio";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";

export default function HoldingsTable() {
  const { data, isLoading, error } = useQuery<Holding[]>({ queryKey: ["holdings"], queryFn: PortfolioAPI.holdings });
  const [q, setQ] = useState("");
  const [sortKey, setSortKey] = useState<keyof Holding | 'value' | 'gainLoss' | 'gainLossPercent'>("symbol");
  const [desc, setDesc] = useState(false);

  const filtered = useMemo(() => {
    const rows = (data || []).filter(h => [h.symbol, h.name, h.sector].some(s => s.toLowerCase().includes(q.toLowerCase())));
    const sorted = [...rows].sort((a,b) => {
      const av = a[sortKey as keyof Holding] as any; const bv = b[sortKey as keyof Holding] as any;
      if (typeof av === 'number' && typeof bv === 'number') return desc ? bv - av : av - bv;
      return desc ? String(bv).localeCompare(String(av)) : String(av).localeCompare(String(bv));
    });
    return sorted;
  }, [data, q, sortKey, desc]);

  if (isLoading) return <div className="h-80 bg-muted/50 rounded-lg animate-pulse"/>;
  if (error) return <div className="text-negative">Failed to load holdings.</div>;

  const header = (key: typeof sortKey, label: string) => (
    <TableHead onClick={() => { if (sortKey === key) setDesc(!desc); else { setSortKey(key); setDesc(false);} }} className="cursor-pointer select-none">
      {label} {sortKey === key ? (desc ? '↓' : '↑') : ''}
    </TableHead>
  );

  return (
    <Card className="shadow-sm">
      <CardHeader>
        <CardTitle>Holdings</CardTitle>
        <Input placeholder="Search by symbol, name or sector" value={q} onChange={(e)=>setQ(e.target.value)} />
      </CardHeader>
      <CardContent>
        <div className="overflow-x-auto">
          <Table>
            <TableHeader>
              <TableRow>
                {header('symbol','Symbol')}
                {header('name','Company')}
                {header('quantity','Qty')}
                {header('avgPrice','Avg Price')}
                {header('currentPrice','Current Price')}
                {header('sector','Sector')}
                {header('marketCap','M.Cap')}
                {header('value','Value')}
                {header('gainLoss','Gain/Loss')}
                {header('gainLossPercent','Gain/Loss %')}
              </TableRow>
            </TableHeader>
            <TableBody>
              {filtered.map(h => (
                <TableRow key={h.symbol}>
                  <TableCell>{h.symbol}</TableCell>
                  <TableCell>{h.name}</TableCell>
                  <TableCell>{h.quantity}</TableCell>
                  <TableCell>₹{h.avgPrice.toLocaleString()}</TableCell>
                  <TableCell>₹{h.currentPrice.toLocaleString()}</TableCell>
                  <TableCell>{h.sector}</TableCell>
                  <TableCell>{h.marketCap}</TableCell>
                  <TableCell>₹{h.value.toLocaleString()}</TableCell>
                  <TableCell className={h.gainLoss>=0?"text-positive":"text-negative"}>₹{h.gainLoss.toLocaleString()}</TableCell>
                  <TableCell className={h.gainLossPercent>=0?"text-positive":"text-negative"}>{h.gainLossPercent.toFixed(2)}%</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </CardContent>
    </Card>
  );
}
