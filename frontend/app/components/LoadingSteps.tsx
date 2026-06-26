import { Loader2 } from "lucide-react";

export function LoadingSteps() {
  const steps = [
    "Analyzing similar operating engagements",
    "Finding recurring patterns",
    "Scoring recommendation confidence",
    "Building operating playbook",
  ];

  return (
    <div className="atlas-card fade-up mt-10 p-7">
      <div className="flex items-center gap-3 text-[var(--ink)]">
        <Loader2 className="animate-spin text-[var(--sage)]" size={20} />
        <span className="font-extrabold">Atlas is working</span>
      </div>
      <div className="mt-5 grid gap-3 md:grid-cols-4">
        {steps.map((step) => (
          <div key={step} className="rounded-2xl border border-[var(--border)] bg-[#fbfaf8] p-4 text-sm font-semibold text-[var(--muted)]">
            {step}
          </div>
        ))}
      </div>
    </div>
  );
}
