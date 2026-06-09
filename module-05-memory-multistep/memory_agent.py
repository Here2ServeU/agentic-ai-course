# Module 5 · Multi-Step Goals — the agent from Module 4, now with a system prompt.
# A system prompt makes the agent plan. The goal below needs several steps and
# several tool calls — but it is ONE goal. TYPE THIS YOURSELF.
#
# Install:  pip install openai duckduckgo-search
# Set key:  export OPENAI_API_KEY='sk-...'

from openai import OpenAI
import json
from duckduckgo_search import DDGS

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
    # The system prompt makes the agent break goals into steps and show its reasoning.
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful research agent. You break complex goals into "
                "steps, use your tools systematically, and give clear final answers. "
                "Always show your reasoning."
            ),
        },
        {"role": "user", "content": goal},
    ]
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
    run_agent(
        "Search for the latest news about electric vehicles. "
        "Then search for Tesla stock price. "
        "Then calculate the value of 100 shares. "
        "Finally, summarize everything in 3 bullet points."
    )
