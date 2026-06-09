# Fraud Investigation Agent

An autonomous AI agent that investigates financial transactions for fraud. It scores
transaction risk, searches the web for fraud patterns, and produces a written
investigation report — served as a FastAPI web service with full observability.

This is the **capstone** of the Agentic AI Systems Engineer course. It stacks every
skill from Modules 1–9: tool calling, a domain system prompt, the agent loop, memory,
a deployed API, file logging, and LangSmith tracing.

> This README is the reference. **Type your own capstone**, then compare. When you push
> your version to your own public GitHub repo, write the README in your own words —
> that README is what makes someone want to interview you.

## What It Does

Give it a transaction in plain English. The agent decides, on its own, to:

1. **Score the fraud risk** with the `score_fraud_risk` tool (amount, timing, new payee → LOW / MEDIUM / HIGH).
2. **Search the web** with the `search_web` tool when it needs current fraud-pattern context.
3. **Write an investigation report** — risk level, the specific signals it found, and a recommended next step.

You gave it a goal. It figured out the steps.

## Architecture

- **LLM:** GPT-4o (OpenAI)
- **Tools:** `search_web` (DuckDuckGo), `score_fraud_risk` (rule-based risk scorer)
- **Pattern:** the agent loop (`while True` until no more tool calls)
- **API:** FastAPI — `POST /investigate`, `GET /health`
- **Observability:** LangSmith tracing + file logging (`capstone_log_YYYY-MM-DD.txt`)
- **Deployment:** Docker → Render.com

## How to Run

1. Clone the repo.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate          # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your keys (copy `.env.example` → `.env`, fill it in, then export):
   ```bash
   export OPENAI_API_KEY='sk-...'
   ```
5. Run the service:
   ```bash
   uvicorn capstone_agent:app --reload
   ```
6. Open the interactive docs and test it: <http://localhost:8000/docs>

## Example

**Request** — `POST /investigate`

```json
{
  "case": "A $9,800 wire transfer at 3:14am to a newly added overseas payee, from an account that normally makes small domestic purchases."
}
```

**Response** (shape)

```json
{
  "report": "RISK LEVEL: HIGH. Signals: large amount (>= $5,000); unusual late-night timing; transfer to a new payee. Recommended action: place a temporary hold and contact the account holder to verify the transfer before it settles.",
  "tokens": 1430,
  "estimated_cost_usd": 0.0072
}
```

## Capstone Completion Checklist

- [ ] Fresh virtual environment created and activated — `(venv)` visible
- [ ] All libraries installed inside the virtual environment
- [ ] Agent runs end-to-end and completes its goal
- [ ] At least 2 tools working (`search_web`, `score_fraud_risk`)
- [ ] Domain system prompt written
- [ ] FastAPI server runs locally — `/investigate` and `/health` tested in the docs
- [ ] Logging writes to a file
- [ ] LangSmith trace visible in the dashboard
- [ ] Dockerfile created
- [ ] README includes venv setup instructions
- [ ] `venv/` listed in `.gitignore`
- [ ] Pushed to public GitHub — **no API keys in the repo**
- [ ] 60-second pitch written and rehearsed
- [ ] Virtual environment deactivated when done

## Your 60-Second Career Pitch

> 1. "I am an AI agent engineer."
> 2. "I build autonomous AI systems that use tools, memory, and planning loops to complete complex goals."
> 3. "In my capstone, I built a fraud investigation agent that scores transaction risk, searches for fraud patterns, and produces investigation reports — deployed as a FastAPI service with LangSmith observability."
> 4. "You can see the code at github.com/your-name/capstone-agent — it is fully documented."
> 5. "I would love to show you how it works."

Five sentences. Sixty seconds. It answers the only question a hiring manager cares
about: **can this person build real things?**

---

*Agentic AI Systems Engineer · Rev. Dr. Emmanuel Naweji · [www.emmanuelnaweji.com](https://www.emmanuelnaweji.com) · Transformed 2 Succeed (T2S)*
