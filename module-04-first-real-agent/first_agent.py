# Module 4 · Building Your First Real Agent
# A real, working AI agent with two tools and an agent loop.
# TYPE EVERY LINE YOURSELF. Compare with this file only after yours runs.
#
# Install:  pip install openai duckduckgo-search
# Set key:  export OPENAI_API_KEY='sk-...'   (Windows CMD: set OPENAI_API_KEY=...)

from openai import OpenAI
import json
from duckduckgo_search import DDGS

client = OpenAI()


# ── Tools: the things the agent can actually DO ───────────────────────
def calculate(expression):
    """Evaluates a math expression."""
    return str(eval(expression))


def search_web(query):
    """Searches the web for current information."""
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
    return str(results)


# ── Tool schemas: what the AI reads to know each tool and when to use it ─
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


# ── The agent loop: the heart of the whole system ─────────────────────
def run_agent(goal):
    messages = [{"role": "user", "content": goal}]
    while True:
        r = client.chat.completions.create(
            model="gpt-4o", messages=messages, tools=tools
        )
        m = r.choices[0].message
        if not m.tool_calls:
            print(m.content)
            return
        messages.append(m)
        for tc in m.tool_calls:
            name = tc.function.name
            args = json.loads(tc.function.arguments)
            result = calculate(**args) if name == "calculate" else search_web(**args)
            print(f"TOOL: {name} | RESULT: {str(result)[:80]}")
            messages.append(
                {"role": "tool", "tool_call_id": tc.id, "content": str(result)}
            )


if __name__ == "__main__":
    # The agent decides the order of steps. You only gave it a goal.
    run_agent(
        "What is the current price of Apple stock? "
        "Then calculate how much 500 shares are worth."
    )
