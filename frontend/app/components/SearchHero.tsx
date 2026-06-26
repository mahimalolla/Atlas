import { ArrowRight, Sparkles } from "lucide-react";

type SearchHeroProps = {
  question: string;
  setQuestion: (value: string) => void;
  onGenerate: () => void;
  loading: boolean;
};

export function SearchHero({ question, setQuestion, onGenerate, loading }: SearchHeroProps) {
  return (
    <section className="soft-grid mt-12 rounded-[34px] border border-[var(--border)] bg-white/55 px-7 py-10 md:px-12 md:py-14">
      <div className="mx-auto max-w-4xl text-center">
        <div className="mx-auto mb-6 inline-flex items-center gap-2 rounded-full border border-[var(--border)] bg-white px-4 py-2 text-sm font-semibold text-[var(--muted)] shadow-sm">
          <Sparkles size={15} className="text-[var(--gold)]" />
          Atlas analyzed portfolio engagements and operating patterns
        </div>

        <h1 className="atlas-heading text-5xl font-extrabold leading-[1.02] tracking-[-0.06em] text-[var(--ink)] md:text-7xl">
          Institutional knowledge for portfolio scale.
        </h1>

        <p className="mx-auto mt-6 max-w-2xl text-lg leading-8 text-[var(--muted)]">
          Turn scattered operating experience into evidence-backed playbooks for growth-stage companies.
        </p>

        <div className="mx-auto mt-10 max-w-3xl rounded-[26px] border border-[var(--border)] bg-white p-3 shadow-[0_18px_70px_rgba(24,50,75,0.08)]">
          <div className="flex flex-col gap-3 md:flex-row">
            <input
              value={question}
              onChange={(event) => setQuestion(event.target.value)}
              placeholder="What operating challenge are you trying to solve today?"
              className="min-h-14 flex-1 rounded-2xl border border-transparent bg-[#f7f5f2] px-5 text-[15px] font-semibold text-[var(--ink)] outline-none transition focus:border-[var(--sage)]"
            />
            <button
              onClick={onGenerate}
              disabled={loading}
              className="inline-flex min-h-14 items-center justify-center gap-2 rounded-2xl bg-[var(--ink)] px-6 text-sm font-extrabold text-white transition hover:-translate-y-0.5 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {loading ? "Building..." : "Generate Playbook"}
              <ArrowRight size={16} />
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}
