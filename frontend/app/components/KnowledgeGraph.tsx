import { Network } from "lucide-react";
import type { Playbook } from "../../types/atlas.ts";

type Props = { playbook: Playbook | null };

export function KnowledgeGraph({ playbook }: Props) {
  const companies = playbook?.supporting_evidence.slice(0, 4) ?? [];

  if (!playbook || companies.length === 0) return null;

  return (
    <section className="atlas-card fade-up mt-10 p-8 md:p-10">
      <div className="flex items-center gap-3">
        <Network className="text-[var(--ink)]" />
        <div>
          <p className="text-sm font-bold uppercase tracking-[0.18em] text-[var(--muted)]">Knowledge Relationships</p>
          <h2 className="atlas-heading mt-1 text-3xl font-extrabold text-[var(--ink)]">How prior cases connect to this playbook</h2>
        </div>
      </div>

      <div className="soft-grid mt-8 overflow-hidden rounded-[28px] border border-[var(--border)] bg-[#fbfaf8] p-8">
        <div className="mx-auto grid max-w-4xl gap-6 md:grid-cols-[1fr_1.2fr_1fr] md:items-center">
          <div className="space-y-3">
            {companies.map((company) => (
              <div key={company.company} className="rounded-2xl border border-[var(--border)] bg-white p-4 text-sm font-extrabold text-[var(--ink)] shadow-sm">
                {company.company}
              </div>
            ))}
          </div>

          <div className="rounded-[30px] border border-[var(--border)] bg-white p-7 text-center shadow-sm">
            <p className="text-xs font-extrabold uppercase tracking-[0.18em] text-[var(--gold)]">Recurring Pattern</p>
            <h3 className="atlas-heading mt-3 text-3xl font-extrabold text-[var(--ink)]">Clear ownership before scale</h3>
            <p className="mt-3 text-sm leading-6 text-[var(--muted)]">Atlas connects prior engagements by the operating moves that repeatedly improved outcomes.</p>
          </div>

          <div className="space-y-3">
            {playbook.recommended_roadmap.slice(0, 3).map((phase) => (
              <div key={phase.phase} className="rounded-2xl border border-[var(--border)] bg-white p-4 text-sm font-extrabold text-[var(--ink)] shadow-sm">
                {phase.phase.replace("Phase ", "P")}
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
