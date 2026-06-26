import { Compass} from "lucide-react";

export function Header() {
  return (
    <header className="mb-8 flex items-center justify-between">
      <div className="flex items-center gap-4">
        <div
          className="
            float-soft
            grid h-12 w-12 place-items-center
            rounded-2xl
            border border-[var(--border)]
            bg-gradient-to-br
            from-white
            to-[var(--paper)]
            shadow-[0_12px_30px_rgba(23,50,77,.08)]
          "
        >
          <Compass
            size={20}
            strokeWidth={2.3}
            className="text-[var(--ink)]"
          />
        </div>

        <div>
          <h1 className="atlas-logo text-4xl leading-none text-[var(--ink)]">
            Atlas
          </h1>

          <div className="mt-1 flex items-center gap-2">
            <div className="gold-rule" />

            <p className="text-[11px] font-bold uppercase tracking-[0.28em] text-[var(--muted)]">
              Operating Intelligence
            </p>
          </div>
        </div>
      </div>

      <div className="hidden items-center gap-3 md:flex">
        <span className="gold-pill rounded-full px-4 py-2 text-xs font-bold tracking-wide">
          Builder in Residence
        </span>

        <a
          href="https://github.com/mahimalolla/Atlas"
          target="_blank"
          rel="noopener noreferrer"
          className="
            atlas-card
            flex items-center gap-2
            rounded-full
            px-4 py-2
            text-sm
            font-semibold
            text-[var(--ink)]
            hover:scale-[1.03]
          "
        >
          GitHub
        </a>
      </div>
    </header>
  );
}