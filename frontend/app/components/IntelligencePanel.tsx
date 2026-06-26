import { Activity, ArrowUpRight, Brain, Target } from "lucide-react";
import type { Intelligence } from "../../types/atlas.ts";

type Props = { intelligence: Intelligence | null };

export function IntelligencePanel({ intelligence }: Props) {
  if (!intelligence) return null;

  return (
    <section className="mt-10 grid gap-6 lg:grid-cols-[0.9fr_1.1fr]">
      <div className="atlas-card p-7">
        <div className="flex items-center gap-3">
          <Brain className="text-[var(--sage)]" />
          <h2 className="atlas-heading text-2xl font-extrabold text-[var(--ink)]">Portfolio Intelligence</h2>
        </div>
        <p className="mt-3 text-sm leading-6 text-[var(--muted)]">
          Atlas surfaces the operating capabilities showing up repeatedly across portfolio engagements.
        </p>

        <div className="mt-6 space-y-3">
          {intelligence.top_capabilities.slice(0, 6).map((item) => (
            <div key={item.capability} className="flex items-center justify-between rounded-2xl border border-[var(--border)] bg-white p-4">
              <span className="font-extrabold text-[var(--ink)]">{item.capability}</span>
              <span className="rounded-full bg-[var(--sage-soft)] px-3 py-1 text-sm font-extrabold text-[var(--sage)]">
                {item.count} engagements
              </span>
            </div>
          ))}
        </div>
      </div>

      <div className="grid gap-6">
        <div className="atlas-card p-7">
          <div className="flex items-center gap-3">
            <Target className="text-[var(--gold)]" />
            <h3 className="atlas-heading text-2xl font-extrabold text-[var(--ink)]">Emerging Opportunities</h3>
          </div>
          <div className="mt-6 grid gap-3 md:grid-cols-2">
            {intelligence.emerging_opportunities.map((opportunity) => (
              <div key={opportunity} className="rounded-2xl bg-[#fbf6e9] p-5 text-sm font-bold leading-6 text-[var(--ink)]">
                {opportunity}
              </div>
            ))}
          </div>
        </div>

        <div className="atlas-card p-7">
          <div className="flex items-center gap-3">
            <Activity className="text-[var(--clay)]" />
            <h3 className="atlas-heading text-2xl font-extrabold text-[var(--ink)]">Recurring Bottlenecks</h3>
          </div>
          <div className="mt-6 flex flex-wrap gap-3">
            {intelligence.recurring_bottlenecks.slice(0, 8).map((item) => (
              <span key={item.bottleneck} className="inline-flex items-center gap-2 rounded-full border border-[var(--border)] bg-white px-4 py-2 text-sm font-extrabold text-[var(--ink)]">
                {item.bottleneck}
                <ArrowUpRight size={14} className="text-[var(--muted)]" />
              </span>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
