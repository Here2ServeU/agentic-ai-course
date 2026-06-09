# Module 9 · Observability — Knowing What Your Agent Is Doing
# Add the three things that separate a hobby project from a professional system:
#   1) file logging   2) cost tracking   3) LangSmith tracing
# TYPE THIS YOURSELF.
#
# Install:  pip install openai duckduckgo-search
# Set key:  export OPENAI_API_KEY='sk-...'

import os
import json
import logging
import datetime
from openai import OpenAI
from duckduckgo_search import DDGS

# ── 3) LangSmith tracing ──────────────────────────────────────────────
# Create a free account at https://smith.langchain.com, copy your API key,
# then set these in your ENVIRONMENT (do not hard-code real keys):
#   export LANGCHAIN_TRACING_V2=true
#   export LANGCHAIN_API_KEY='your-langsmith-key'
#   export LANGCHAIN_PROJECT='my-first-agent'
os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
os.environ.setdefault("LANGCHAIN_PROJECT", "my-first-agent")
# LANGCHAIN_API_KEY should come from your environment, not this file.

# ── 1) File logging ───────────────────────────────────────────────────
logging.basicConfig(
    filename=f"agent_log_{datetime.date.today()}.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

client = OpenAI()


def calculate(expression):
    """Evaluates a math expression."""
    return str(eval(expression))


def search_web(query):
    """Searches the web for current information."""
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
    return str(results)


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluates a math expression.",
            "parameters": {
                "type": "object",
                "properties": {"expression": {"type": "string"}},
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Searches the web for current information.",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    },
]


def run_agent(goal):
    logging.info(f"AGENT START - Goal: {goal}")
    messages = [{"role": "user", "content": goal}]
    total_tokens = 0

    while True:
        response = client.chat.completions.create(
            model="gpt-4o", messages=messages, tools=tools
        )

        # ── 2) Cost tracking ──────────────────────────────────────────
        tokens_used = response.usage.total_tokens
        total_tokens += tokens_used
        cost_estimate = total_tokens * 0.000005
        logging.info(f"Tokens: {tokens_used} | Running cost: ${cost_estimate:.4f}")

        m = response.choices[0].message
        if not m.tool_calls:
            logging.info(f"AGENT COMPLETE - Answer: {m.content}")
            print(m.content)
            print(f"\n[Total tokens: {total_tokens} | Est. cost: ${cost_estimate:.4f}]")
            return

        messages.append(m)
        for tc in m.tool_calls:
            name = tc.function.name
            args = json.loads(tc.function.arguments)
            logging.info(f"TOOL CALL: {name} - Args: {args}")
            result = calculate(**args) if name == "calculate" else search_web(**args)
            logging.info(f"TOOL RESULT: {str(result)[:200]}")
            print(f"TOOL: {name} | RESULT: {str(result)[:80]}")
            messages.append(
                {"role": "tool", "tool_call_id": tc.id, "content": str(result)}
            )


if __name__ == "__main__":
    run_agent(
        "What is the current price of Apple stock? "
        "Then calculate how much 500 shares are worth."
    )
    # Now open the agent_log_YYYY-MM-DD.txt file and read every line.
    # Then check your trace at https://smith.langchain.com
