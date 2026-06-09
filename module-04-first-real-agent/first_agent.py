# Module 4 · first_agent.py
# Install: pip install openai duckduckgo-search
# Set key: export OPENAI_API_KEY='sk-...'   (Windows CMD: set OPENAI_API_KEY=...)
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


def run_agent(goal):
    messages = [{"role": "user", "content": goal}]
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


run_agent("What is the current price of Apple stock? Then calculate how much 500 shares are worth.")
