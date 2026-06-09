# Module 8 · Wrapping Your Agent in FastAPI
# Turn your agent into a web service that anyone can call over the internet.
# TYPE THIS YOURSELF.
#
# Install:  pip install fastapi uvicorn openai
# Run:      uvicorn agent_api:app --reload
# Docs:     http://localhost:8000/docs   (test it right in the browser)

import json
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()
app = FastAPI(title="My First Agent API")


def calculate(expression):
    """Evaluates a math expression."""
    return str(eval(expression))


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
    }
]


def run_agent(goal):
    messages = [{"role": "user", "content": goal}]
    while True:
        r = client.chat.completions.create(
            model="gpt-4o", messages=messages, tools=tools
        )
        m = r.choices[0].message
        if not m.tool_calls:
            return m.content
        messages.append(m)
        for tc in m.tool_calls:
            args = json.loads(tc.function.arguments)
            result = calculate(**args)
            messages.append(
                {"role": "tool", "tool_call_id": tc.id, "content": str(result)}
            )


class AgentRequest(BaseModel):
    goal: str


@app.post("/run-agent")
def run_agent_endpoint(request: AgentRequest):
    answer = run_agent(request.goal)
    return {"goal": request.goal, "answer": answer}


@app.get("/health")
def health():
    return {"status": "ok"}
