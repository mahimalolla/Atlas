"use client";


import { useEffect, useState } from "react";
import { Header } from "./components/Header";
import { SearchHero } from "./components/SearchHero";
import { StatTile } from "./components/StatTile";
import { LoadingSteps } from "./components/LoadingSteps";
import { PlaybookPanel } from "./components/PlaybookPanel";
import { EvidenceTimeline } from "./components/EvidenceTimeline";
import { IntelligencePanel } from "./components/IntelligencePanel";
import { KnowledgeGraph } from "./components/KnowledgeGraph";
import { extractCases, generatePlaybook, getIntelligence } from "../services/api";
import type { Intelligence, Playbook } from "../types/atlas";

const DEFAULT_QUESTION = "How should a Series B SaaS company build its first AI team?";

export default function Home() {
  const [question, setQuestion] = useState(DEFAULT_QUESTION);
  const [loading, setLoading] = useState(false);
  const [booting, setBooting] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [intelligence, setIntelligence] = useState<Intelligence | null>(null);
  const [playbook, setPlaybook] = useState<Playbook | null>(null);

  useEffect(() => {
    async function initializeAtlas() {
      try {
        await extractCases();
        const data = await getIntelligence();
        setIntelligence(data);
      } catch (err) {
        setError("Start the FastAPI backend on http://127.0.0.1:8000, then refresh Atlas.");
      } finally {
        setBooting(false);
      }
    }

    initializeAtlas();
  }, []);

  async function handleGenerate() {
    if (!question.trim()) return;

    setLoading(true);
    setError(null);

    try {
      const result = await generatePlaybook(question);
      setPlaybook(result);
    } catch (err) {
      setError("Atlas could not generate a playbook. Check that the backend is running and cases are extracted.");
    } finally {
      setLoading(false);
    }
  }

  const summary = intelligence?.portfolio_summary;
  const health = intelligence?.portfolio_health;

  return (
    <main className="atlas-shell">
      <Header />

      <SearchHero
        question={question}
        setQuestion={setQuestion}
        onGenerate={handleGenerate}
        loading={loading}
      />

      {error ? (
        <div className="mt-6 rounded-3xl border border-[#ead4c8] bg-[#fff5ef] p-5 text-sm font-bold text-[var(--clay)]">
          {error}
        </div>
      ) : null}

      {booting ? <LoadingSteps /> : null}
      {loading ? <LoadingSteps /> : null}

      <section className="mt-10 grid gap-5 md:grid-cols-4">
        <StatTile value={health?.score ?? "--"} label="Portfolio Health" note={health?.confidence ?? "Waiting for backend"} />
        <StatTile value={summary?.companies ?? "--"} label="Companies" note="In extracted knowledge base" />
        <StatTile value={summary?.capabilities ?? "--"} label="Capabilities" note="Operating themes detected" />
        <StatTile value={summary?.engagements ?? "--"} label="Engagements" note="Prior cases analyzed" />
      </section>

      <PlaybookPanel playbook={playbook} />
      <EvidenceTimeline playbook={playbook} />
      <IntelligencePanel intelligence={intelligence} />
      <KnowledgeGraph playbook={playbook} />
    </main>
  );
}
