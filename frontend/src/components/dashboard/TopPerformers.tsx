import { useQuery } from "@tanstack/react-query";
import { PortfolioAPI, Summary } from "@/api/portfolio";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default function TopPerformers(){
  const { data, isLoading, error } = useQuery<Summary>({ queryKey: ["summary"], queryFn: PortfolioAPI.summary });
  if (isLoading) return <div className="h-40 bg-muted/50 rounded-lg animate-pulse"/>;
  if (error || !data) return <div className="text-negative">Failed to load insights.</div>;

  return (
    <div className="grid md:grid-cols-3 gap-4">
      <Card className="shadow-sm">
        <CardHeader><CardTitle>Best Performer</CardTitle></CardHeader>
        <CardContent>
          <div className="text-2xl font-semibold text-positive">{data.topPerformer.symbol}</div>
          <div className="text-muted-foreground">{data.topPerformer.name}</div>
          <div className="mt-2 text-positive">{data.topPerformer.gainPercent}%</div>
        </CardContent>
      </Card>
      <Card className="shadow-sm">
        <CardHeader><CardTitle>Worst Performer</CardTitle></CardHeader>
        <CardContent>
          <div className="text-2xl font-semibold text-negative">{data.worstPerformer.symbol}</div>
          <div className="text-muted-foreground">{data.worstPerformer.name}</div>
          <div className="mt-2 text-negative">{data.worstPerformer.gainPercent}%</div>
        </CardContent>
      </Card>
      <Card className="shadow-sm">
        <CardHeader><CardTitle>Insights</CardTitle></CardHeader>
        <CardContent>
          <div className="flex items-center justify-between"><span>Diversification Score</span><span className="font-semibold">{data.diversificationScore}/10</span></div>
          <div className="flex items-center justify-between mt-2"><span>Risk Level</span><span className="font-semibold">{data.riskLevel}</span></div>
        </CardContent>
      </Card>
    </div>
  );
}
