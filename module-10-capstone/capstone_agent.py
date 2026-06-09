# Module 10 · Capstone — Fraud Investigation Agent (Option A)
# The full build: 2 tools, a domain system prompt, memory, a FastAPI service,
# file logging, and LangSmith tracing. This is everything you learned, stacked.
#
# TYPE THIS YOURSELF. Use this file only to compare with yours.
#
# Install:  pip install openai fastapi uvicorn duckduckgo-search
# Run:      uvicorn capstone_agent:app --reload
# Docs:     http://localhost:8000/docs   (test /investigate and /health)
#
# Keys (set in the ENVIRONMENT, never in this file):
#   export OPENAI_API_KEY='sk-...'
#   export LANGCHAIN_TRACING_V2=true
#   export LANGCHAIN_API_KEY='your-langsmith-key'
#   export LANGCHAIN_PROJECT='capstone-fraud-agent'

import os
import json
import logging
import datetime

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from duckduckgo_search import DDGS

# ── Observability: LangSmith tracing ──────────────────────────────────
os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
os.environ.setdefault("LANGCHAIN_PROJECT", "capstone-fraud-agent")
# LANGCHAIN_API_KEY must come from your environment.

# ── Observability: file logging ───────────────────────────────────────
logging.basicConfig(
    filename=f"capstone_log_{datetime.date.today()}.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

client = OpenAI()


# ── Tool 1: search the web for fraud patterns / context ───────────────
def search_web(query):
    """Searches the web for current fraud patterns and context."""
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
    return str(results)


# ── Tool 2: score the fraud risk of a transaction ────────────────────
def score_fraud_risk(amount, hour, is_new_payee):
    """Scores a transaction's fraud risk as LOW, MEDIUM, or HIGH with reasons."""
    score = 0
    reasons = []

    amount = float(amount)
    hour = int(hour)
    # accept bools or strings like "true"/"yes"
    if isinstance(is_new_payee, str):
        is_new_payee = is_new_payee.strip().lower() in ("true", "yes", "1", "y")

    if amount >= 5000:
        score += 2
        reasons.append("large amount (>= $5,000)")
    elif amount >= 1000:
        score += 1
        reasons.append("moderate amount (>= $1,000)")

    if hour < 6 or hour >= 23:
        score += 2
        reasons.append("unusual late-night / early-morning timing")

    if is_new_payee:
        score += 2
        reasons.append("transfer to a new payee")

    if score >= 4:
        level = "HIGH"
    elif score >= 2:
        level = "MEDIUM"
    else:
        level = "LOW"

    return json.dumps(
        {"risk_level": level, "score": score, "reasons": reasons}
    )


tools = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Searches the web for current fraud patterns and context.",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "score_fraud_risk",
            "description": (
                "Scores a transaction's fraud risk as LOW, MEDIUM, or HIGH. "
                "Provide the amount in dollars, the hour of day (0-23), and whether "
                "the payee is new."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {"type": "number"},
                    "hour": {"type": "integer"},
                    "is_new_payee": {"type": "boolean"},
                },
                "required": ["amount", "hour", "is_new_payee"],
            },
        },
    },
]


SYSTEM_PROMPT = """You are a senior fraud investigator at a major bank with over
10,000 investigated cases. When given a transaction to investigate, you:
1. Use score_fraud_risk to get a structured risk rating for the transaction.
2. Use search_web when you need current context on a fraud pattern.
3. Produce a clear investigation report with: the risk level (LOW, MEDIUM, or HIGH),
   the specific signals you found, and a recommended next step.
Always explain your reasoning clearly. Never guess when a tool can give you a fact."""


def run_fraud_agent(case):
    """Runs the fraud investigation agent loop on a case description."""
    logging.info(f"INVESTIGATION START - Case: {case}")
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": case},
    ]
    total_tokens = 0

    while True:
        response = client.chat.completions.create(
            model="gpt-4o", messages=messages, tools=tools
        )

        tokens_used = response.usage.total_tokens
        total_tokens += tokens_used
        cost = total_tokens * 0.000005
        logging.info(f"Tokens: {tokens_used} | Running cost: ${cost:.4f}")

        m = response.choices[0].message
        if not m.tool_calls:
            logging.info(f"INVESTIGATION COMPLETE - Report: {m.content}")
            return {
                "report": m.content,
                "tokens": total_tokens,
                "estimated_cost_usd": round(cost, 4),
            }

        messages.append(m)
        for tc in m.tool_calls:
            name = tc.function.name
            args = json.loads(tc.function.arguments)
            logging.info(f"TOOL CALL: {name} - Args: {args}")
            if name == "search_web":
                result = search_web(**args)
            else:
                result = score_fraud_risk(**args)
            logging.info(f"TOOL RESULT: {str(result)[:200]}")
            messages.append(
                {"role": "tool", "tool_call_id": tc.id, "content": str(result)}
            )


# ── FastAPI service ───────────────────────────────────────────────────
app = FastAPI(title="Fraud Investigation Agent")


class InvestigateRequest(BaseModel):
    case: str


@app.post("/investigate")
def investigate(request: InvestigateRequest):
    """Investigate a transaction and return a fraud report."""
    return run_fraud_agent(request.case)


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    # Quick local test without the server:
    example = (
        "Transaction: a $9,800 wire transfer at 3:14am to a newly added overseas "
        "payee, from an account that normally makes small domestic purchases."
    )
    print(run_fraud_agent(example)["report"])
