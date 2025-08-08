import { useQuery } from "@tanstack/react-query";
import { PortfolioAPI, Performance } from "@/api/portfolio";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, Legend } from "recharts";

export default function PerformanceChart(){
  const { data, isLoading, error } = useQuery<Performance>({ queryKey: ["performance"], queryFn: PortfolioAPI.performance });

  if (isLoading) return <div className="h-80 bg-muted/50 rounded-lg animate-pulse"/>;
  if (error || !data) return <div className="text-negative">Failed to load performance.</div>;

  const chartData = data.timeline.map(t => ({ date: t.date.slice(0,7), Portfolio: t.portfolio, Nifty50: t.nifty50, Gold: t.gold }));

  return (
    <Card className="shadow-sm">
      <CardHeader>
        <CardTitle>Performance vs Benchmarks</CardTitle>
        <div className="text-sm text-muted-foreground">1M {data.returns.portfolio['1month']}% | 3M {data.returns.portfolio['3months']}% | 1Y {data.returns.portfolio['1year']}%</div>
      </CardHeader>
      <CardContent className="h-80">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={chartData} margin={{ left: 8, right: 8, bottom: 8 }}>
            <XAxis dataKey="date"/>
            <YAxis/>
            <Tooltip formatter={(v:any)=> typeof v==='number'? v.toLocaleString(): v }/>
            <Legend/>
            <Line type="monotone" dataKey="Portfolio" stroke="hsl(var(--primary))" strokeWidth={2} dot={false}/>
            <Line type="monotone" dataKey="Nifty50" stroke="hsl(var(--accent))" strokeWidth={2} dot={false}/>
            <Line type="monotone" dataKey="Gold" stroke="hsl(var(--muted-foreground))" strokeWidth={2} dot={false}/>
          </LineChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}
