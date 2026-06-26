export type Intelligence = {
  portfolio_summary: {
    engagements: number;
    companies: number;
    capabilities: number;
  };
  portfolio_health: {
    score: number;
    confidence: string;
  };
  top_capabilities: {
    capability: string;
    count: number;
  }[];
  recurring_bottlenecks: {
    bottleneck: string;
    frequency: number;
  }[];
  successful_interventions: {
    intervention: string;
    frequency: number;
  }[];
  emerging_opportunities: string[];
};

export type Playbook = {
  question: string;
  title: string;
  objective: string;
  confidence: {
    score: number;
    basis: {
      cases_analyzed: number;
      action_patterns: number;
      capability_patterns: number;
    };
  };
  pattern_summary: string;
  recommended_roadmap: {
    phase: string;
    goal: string;
    actions: string[];
  }[];
  key_risks: string[];
  supporting_evidence: {
    company: string;
    stage: string;
    sector: string;
    problem: string;
    outcome: string;
    lesson: string;
    source_file: string;
  }[];
};
