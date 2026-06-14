# Module 5 · first_agent.py
# Lab 5.2 — the Module 4 search agent, now with memory + planning.
# The one new idea vs. Module 4: a system prompt that tells the agent to
# break the goal into steps, use its tools systematically, and show its work.
# Install: pip install openai duckduckgo-search
# Set key: export OPENAI_API_KEY='sk-...'
# Run:     python first_agent.py

from openai import OpenAI
import json
from duckduckgo_search import DDGS

client = OpenAI()


def calculate(expression):
    return str(eval(expression))


def search_web(query):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
    return str(results)


# Two tools, two separate entries in the list. Each is its own
# {"type": "function", "function": {...}} dict.
tools = [{
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Evaluates a math expression.",
        "parameters": {
            "type": "object",
            "properties": {"expression": {"type": "string"}},
            "required": ["expression"]
        }
    }
}, {
    "type": "function",
    "function": {
        "name": "search_web",
        "description": "Searches the web for current information.",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"]
        }
    }
}]


# The new part: messages now starts with a system prompt. It turns a tool-caller
# into a planner — break the goal into steps, use tools, show the reasoning.
def run_agent(goal):
    messages = [
        {"role": "system", "content": "You are a helpful research agent. "
            "You break complex goals into steps, use your tools systematically, "
            "and give clear final answers. Always show your reasoning."},
        {"role": "user", "content": goal}
    ]
    while True:
        r = client.chat.completions.create(model="gpt-4o", messages=messages, tools=tools)
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
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})


run_agent("If one share of Apple stock costs 765 US Dollars, how much are 1287 shares worth?")

run_agent(
    "Research NVIDIA and Apple. Find what each company does. "
    "Then tell me which one you would recommend researching further for a "
    "portfolio and explain why."
)
