import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useQuery } from "@tanstack/react-query";
import { PortfolioAPI, Summary } from "@/api/portfolio";

const Stat = ({ label, value, accent }: { label: string; value: string; accent?: 'positive' | 'negative' }) => (
  <Card className="transition-transform hover:-translate-y-0.5 shadow-sm">
    <CardHeader>
      <CardTitle className="text-sm text-muted-foreground">{label}</CardTitle>
    </CardHeader>
    <CardContent>
      <div className={`text-3xl font-semibold ${accent === 'positive' ? 'text-positive' : accent === 'negative' ? 'text-negative' : ''}`}>{value}</div>
    </CardContent>
  </Card>
);

export default function OverviewCards() {
  const { data, isLoading, error } = useQuery<Summary>({ queryKey: ["summary"], queryFn: PortfolioAPI.summary });

  if (isLoading) return <div className="grid gap-4 md:grid-cols-4"><div className="h-28 bg-muted/50 rounded-lg animate-pulse" /><div className="h-28 bg-muted/50 rounded-lg animate-pulse" /><div className="h-28 bg-muted/50 rounded-lg animate-pulse" /><div className="h-28 bg-muted/50 rounded-lg animate-pulse" /></div>;
  if (error || !data) return <div className="text-negative">Failed to load summary.</div>;

  const glAccent = data.totalGainLoss >= 0 ? 'positive' : 'negative';

  return (
    <div className="grid gap-4 md:grid-cols-4">
      <Stat label="Total Portfolio Value" value={`₹${data.totalValue.toLocaleString()}`} />
      <Stat label="Total Gain/Loss" value={`₹${data.totalGainLoss.toLocaleString()} (${data.totalGainLossPercent.toFixed(2)}%)`} accent={glAccent} />
      <Stat label="Holdings" value={`${data.holdingsCount}`} />
      <Stat label="Risk Level" value={data.riskLevel} />
    </div>
  );
}
