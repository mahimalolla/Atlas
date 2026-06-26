import { AlertTriangle, CheckCircle2, Layers3 } from "lucide-react";
import type { Playbook } from "../../types/atlas.ts";

type Props = { playbook: Playbook | null };

export function PlaybookPanel({ playbook }: Props) {
  if (!playbook) {
    return (
      <section className="atlas-card mt-10 p-8 text-center">
        <p className="text-sm font-bold uppercase tracking-[0.18em] text-[var(--muted)]">Operating Playbook</p>
        <h2 className="atlas-heading mx-auto mt-4 max-w-2xl text-3xl font-extrabold text-[var(--ink)]">
          Ask Atlas to convert prior portfolio experience into a structured recommendation.
        </h2>
      </section>
    );
  }

  return (
    <section className="atlas-card fade-up mt-10 overflow-hidden">
      <div className="grid gap-0 lg:grid-cols-[1.35fr_0.65fr]">
        <div className="p-8 md:p-10">
          <div className="flex items-center gap-3">
            <div className="grid h-10 w-10 place-items-center rounded-full bg-[var(--navy-soft)] text-[var(--ink)]">
              <Layers3 size={18} />
            </div>
            <div>
              <p className="text-sm font-bold uppercase tracking-[0.18em] text-[var(--muted)]">Operating Playbook</p>
              <h2 className="atlas-heading mt-1 text-3xl font-extrabold text-[var(--ink)]">Recommended path forward</h2>
            </div>
          </div>

          <div className="mt-8 rounded-3xl bg-[#f8f6f1] p-6">
            <p className="text-sm font-extrabold uppercase tracking-[0.16em] text-[var(--gold)]">Objective</p>
            <p className="mt-3 leading-8 text-[var(--ink)]">{playbook.objective}</p>
          </div>

          <div className="mt-8 space-y-5">
            {playbook.recommended_roadmap.map((phase, index) => (
              <div key={phase.phase} className="rounded-3xl border border-[var(--border)] bg-white p-6">
                <div className="flex items-start gap-4">
                  <div className="atlas-heading grid h-9 w-9 shrink-0 place-items-center rounded-full bg-[var(--sage-soft)] text-lg font-extrabold text-[var(--sage)]">
                    {index + 1}
                  </div>
                  <div>
                    <h3 className="atlas-heading text-xl font-extrabold text-[var(--ink)]">{phase.phase}</h3>
                    <p className="mt-2 text-sm leading-6 text-[var(--muted)]">{phase.goal}</p>
                    <ul className="mt-4 space-y-2">
                      {phase.actions.map((action) => (
                        <li key={action} className="flex gap-2 text-sm font-semibold text-[var(--ink)]">
                          <CheckCircle2 size={17} className="mt-0.5 shrink-0 text-[var(--sage)]" />
                          {action}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        <aside className="border-t border-[var(--border)] bg-[#fbfaf8] p-8 md:p-10 lg:border-l lg:border-t-0">
          <p className="text-sm font-bold uppercase tracking-[0.18em] text-[var(--muted)]">Recommendation Confidence</p>
          <div className="atlas-heading mt-4 text-7xl font-extrabold text-[var(--gold)]">{playbook.confidence.score}</div>
          <p className="mt-2 font-extrabold text-[var(--ink)]">High confidence</p>

          <div className="mt-7 grid gap-3">
            <div className="rounded-2xl border border-[var(--border)] bg-white p-4">
              <div className="text-2xl font-extrabold text-[var(--ink)]">{playbook.confidence.basis.cases_analyzed}</div>
              <div className="text-sm font-semibold text-[var(--muted)]">Portfolio engagements</div>
            </div>
            <div className="rounded-2xl border border-[var(--border)] bg-white p-4">
              <div className="text-2xl font-extrabold text-[var(--ink)]">{playbook.confidence.basis.action_patterns}</div>
              <div className="text-sm font-semibold text-[var(--muted)]">Action patterns</div>
            </div>
            <div className="rounded-2xl border border-[var(--border)] bg-white p-4">
              <div className="text-2xl font-extrabold text-[var(--ink)]">{playbook.confidence.basis.capability_patterns}</div>
              <div className="text-sm font-semibold text-[var(--muted)]">Capability patterns</div>
            </div>
          </div>

          <div className="mt-8">
            <div className="flex items-center gap-2 text-sm font-extrabold uppercase tracking-[0.16em] text-[var(--clay)]">
              <AlertTriangle size={16} /> Key Risks
            </div>
            <ul className="mt-4 space-y-3">
              {playbook.key_risks.map((risk) => (
                <li key={risk} className="rounded-2xl bg-white p-4 text-sm leading-6 text-[var(--ink)]">
                  {risk}
                </li>
              ))}
            </ul>
          </div>
        </aside>
      </div>
    </section>
  );
}
