import { useQuery } from "@tanstack/react-query";
import { PortfolioAPI, Allocation } from "@/api/portfolio";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from "recharts";

const COLORS = ["hsl(var(--primary))", "hsl(var(--accent))", "hsl(var(--muted-foreground))", "hsl(var(--secondary))", "hsl(var(--ring))"];

export default function AllocationCharts() {
  const { data, isLoading, error } = useQuery<Allocation>({ queryKey: ["allocation"], queryFn: PortfolioAPI.allocation });

  if (isLoading) return <div className="grid md:grid-cols-2 gap-4"><div className="h-80 bg-muted/50 rounded-lg animate-pulse"/><div className="h-80 bg-muted/50 rounded-lg animate-pulse"/></div>;
  if (error || !data) return <div className="text-negative">Failed to load allocation.</div>;

  const sectorData = Object.entries(data.bySector).map(([name, v]) => ({ name, value: Math.round(v.value), percentage: v.percentage }));
  const capData = Object.entries(data.byMarketCap).map(([name, v]) => ({ name, value: Math.round(v.value), percentage: v.percentage }));

  const ChartCard = ({ title, items }: { title: string; items: { name: string; value: number; percentage: number }[] }) => (
    <Card className="shadow-sm">
      <CardHeader><CardTitle>{title}</CardTitle></CardHeader>
      <CardContent className="h-72">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie data={items} dataKey="value" nameKey="name" innerRadius={60} outerRadius={100} paddingAngle={2}>
              {items.map((_, idx) => (<Cell key={idx} fill={COLORS[idx % COLORS.length]} />))}
            </Pie>
            <Tooltip formatter={(v: number, n: string, p: any) => [`₹${v.toLocaleString()} (${p.payload.percentage}%)`, n]} />
          </PieChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );

  return (
    <div className="grid md:grid-cols-2 gap-4">
      <ChartCard title="Sector Allocation" items={sectorData} />
      <ChartCard title="Market Cap Allocation" items={capData} />
    </div>
  );
}
