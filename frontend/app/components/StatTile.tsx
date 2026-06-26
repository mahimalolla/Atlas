type StatTileProps = {
  value: string | number;
  label: string;
  note?: string;
};

export function StatTile({ value, label, note }: StatTileProps) {
  return (
    <div className="atlas-card p-6 transition hover:-translate-y-1 hover:border-[#d8d2c7]">
      <div className="atlas-heading text-4xl font-extrabold text-[var(--ink)]">{value}</div>
      <div className="mt-3 h-px w-10 bg-[var(--gold)]" />
      <p className="mt-4 text-sm font-bold uppercase tracking-[0.16em] text-[var(--muted)]">{label}</p>
      {note ? <p className="mt-2 text-sm text-[var(--soft)]">{note}</p> : null}
    </div>
  );
}
