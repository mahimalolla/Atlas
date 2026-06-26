const API_BASE_URL = "http://127.0.0.1:8000";

export async function extractCases() {
  const response = await fetch(`${API_BASE_URL}/extract-cases`, { method: "POST" });
  if (!response.ok) throw new Error("Failed to extract cases");
  return response.json();
}

export async function getIntelligence() {
  const response = await fetch(`${API_BASE_URL}/intelligence`);
  if (!response.ok) throw new Error("Failed to load intelligence");
  return response.json();
}

export async function generatePlaybook(question: string) {
  const response = await fetch(`${API_BASE_URL}/playbook`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question, top_k: 5 }),
  });
  if (!response.ok) throw new Error("Failed to generate playbook");
  return response.json();
}
