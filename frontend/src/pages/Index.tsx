import OverviewCards from "@/components/dashboard/OverviewCards";
import AllocationCharts from "@/components/dashboard/AllocationCharts";
import HoldingsTable from "@/components/dashboard/HoldingsTable";
import PerformanceChart from "@/components/dashboard/PerformanceChart";
import TopPerformers from "@/components/dashboard/TopPerformers";
import { useSEO } from "@/components/SEO";

const Index = () => {
  useSEO({
    title: "Portfolio Analytics Dashboard | WealthManager.online",
    description: "Track holdings, sector allocation, market cap split, and performance vs Nifty 50 and Gold.",
    canonical: "https://wealthmanager.online/",
  });

  return (
    <main className="min-h-screen bg-background">
      <header className="py-10">
        <div className="container">
          <h1 className="text-4xl font-bold tracking-tight bg-clip-text text-transparent" style={{ backgroundImage: 'var(--gradient-primary)' }}>WealthManager.online</h1>
          <p className="text-muted-foreground mt-2">Portfolio Analytics Dashboard</p>
          <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'WebApplication',
            name: 'WealthManager.online Portfolio Analytics',
            description: 'Interactive portfolio analytics dashboard with holdings, allocation and performance charts',
            applicationCategory: 'FinanceApplication'
          }) }} />
        </div>
      </header>
      <section className="container space-y-8 pb-12">
        <OverviewCards />
        <AllocationCharts />
        <PerformanceChart />
        <TopPerformers />
        <HoldingsTable />
      </section>
    </main>
  );
};

export default Index;
