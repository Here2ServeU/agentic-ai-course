# Module 10 · capstone_agent.py — Fraud Investigation Agent (Option A)
# Two tools, a domain system prompt, the agent loop, logging, tracing, and FastAPI.
# Install: pip install openai fastapi uvicorn duckduckgo-search
# Run:     uvicorn capstone_agent:app --reload   ->  http://localhost:8000/docs
# Keys (set in the environment, never in this file):
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

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "capstone-fraud-agent"

logging.basicConfig(
    filename=f"capstone_log_{datetime.date.today()}.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

client = OpenAI()


# ── Tools ─────────────────────────────────────────────────────────────
def search_web(query):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
    return str(results)


def score_fraud_risk(amount, hour, is_new_payee):
    score = 0
    reasons = []
    amount = float(amount)
    hour = int(hour)
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

    level = "HIGH" if score >= 4 else "MEDIUM" if score >= 2 else "LOW"
    return json.dumps({"risk_level": level, "score": score, "reasons": reasons})


tools = [{
    "type": "function",
    "function": {
        "name": "search_web",
        "description": "Searches the web for current fraud patterns and context.",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"]
        }
    }
}, {
    "type": "function",
    "function": {
        "name": "score_fraud_risk",
        "description": "Scores a transaction's fraud risk as LOW, MEDIUM, or HIGH. "
                       "Provide amount (dollars), hour of day (0-23), and whether the "
                       "payee is new.",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {"type": "number"},
                "hour": {"type": "integer"},
                "is_new_payee": {"type": "boolean"}
            },
            "required": ["amount", "hour", "is_new_payee"]
        }
    }
}]


SYSTEM_PROMPT = """You are a senior fraud investigator at a major bank with over
10,000 investigated cases. When given a transaction to investigate, you:
1. Use score_fraud_risk to get a structured risk rating for the transaction.
2. Use search_web when you need current context on a fraud pattern.
3. Produce a clear investigation report with: the risk level (LOW, MEDIUM, or HIGH),
   the specific signals you found, and a recommended next step.
Always explain your reasoning clearly. Never guess when a tool can give you a fact."""


def run_fraud_agent(case):
    logging.info(f"INVESTIGATION START - Case: {case}")
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": case}
    ]
    total_tokens = 0
    while True:
        response = client.chat.completions.create(model="gpt-4o", messages=messages, tools=tools)

        tokens_used = response.usage.total_tokens
        total_tokens += tokens_used
        cost = total_tokens * 0.000005
        logging.info(f"Tokens: {tokens_used} | Cost: ${cost:.4f}")

        message = response.choices[0].message
        if not message.tool_calls:
            logging.info(f"INVESTIGATION COMPLETE - Report: {message.content}")
            return {"report": message.content, "tokens": total_tokens,
                    "estimated_cost_usd": round(cost, 4)}
        messages.append(message)
        for tc in message.tool_calls:
            name = tc.function.name
            args = json.loads(tc.function.arguments)
            logging.info(f"TOOL CALL: {name} - Args: {args}")
            result = search_web(**args) if name == "search_web" else score_fraud_risk(**args)
            logging.info(f"TOOL RESULT: {str(result)[:200]}")
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})


# ── FastAPI service ───────────────────────────────────────────────────
app = FastAPI(title="Fraud Investigation Agent")


class InvestigateRequest(BaseModel):
    case: str


@app.post("/investigate")
def investigate(request: InvestigateRequest):
    return run_fraud_agent(request.case)


@app.get("/health")
def health():
    return {"status": "ok"}
