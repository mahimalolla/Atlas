import { Building2 } from "lucide-react";
import type { Playbook } from "../../types/atlas.ts";

type Props = { playbook: Playbook | null };

export function EvidenceTimeline({ playbook }: Props) {
  if (!playbook || playbook.supporting_evidence.length === 0) return null;

  return (
    <section className="atlas-card fade-up mt-10 p-8 md:p-10">
      <div className="flex items-center gap-3">
        <Building2 className="text-[var(--sage)]" />
        <div>
          <p className="text-sm font-bold uppercase tracking-[0.18em] text-[var(--muted)]">Supporting Evidence</p>
          <h2 className="atlas-heading mt-1 text-3xl font-extrabold text-[var(--ink)]">Relevant portfolio engagements</h2>
        </div>
      </div>

      <div className="mt-8 grid gap-5">
        {playbook.supporting_evidence.map((caseItem) => (
          <div key={`${caseItem.company}-${caseItem.source_file}`} className="relative rounded-3xl border border-[var(--border)] bg-white p-6 transition hover:-translate-y-1 hover:border-[#d8d2c7]">
            <div className="flex flex-col gap-4 md:flex-row md:items-start md:justify-between">
              <div>
                <h3 className="atlas-heading text-2xl font-extrabold text-[var(--ink)]">{caseItem.company}</h3>
                <p className="mt-1 text-sm font-bold text-[var(--muted)]">{caseItem.stage} · {caseItem.sector}</p>
              </div>
              <span className="w-fit rounded-full bg-[var(--navy-soft)] px-3 py-1 text-xs font-extrabold uppercase tracking-[0.14em] text-[var(--ink)]">
                {caseItem.source_file}
              </span>
            </div>

            <div className="mt-6 grid gap-4 md:grid-cols-3">
              <div>
                <p className="text-xs font-extrabold uppercase tracking-[0.16em] text-[var(--gold)]">Problem</p>
                <p className="mt-2 text-sm leading-6 text-[var(--ink)]">{caseItem.problem}</p>
              </div>
              <div>
                <p className="text-xs font-extrabold uppercase tracking-[0.16em] text-[var(--sage)]">Outcome</p>
                <p className="mt-2 text-sm leading-6 text-[var(--ink)]">{caseItem.outcome}</p>
              </div>
              <div>
                <p className="text-xs font-extrabold uppercase tracking-[0.16em] text-[var(--clay)]">Lesson</p>
                <p className="mt-2 text-sm leading-6 text-[var(--ink)]">{caseItem.lesson}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
