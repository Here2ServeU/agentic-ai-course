# Module 9 - Observable Agent
# Install: pip install ddgs openai agents "langsmith[openai-agents]"
# Set in terminal: OPENAI_API_KEY, LANGSMITH_TRACING, LANGSMITH_ENDPOINT,
#                  LANGSMITH_API_KEY, LANGSMITH_PROJECT
# Never put keys in this file.

import os
import json
import logging
import datetime
import asyncio
from openai import OpenAI
from ddgs import DDGS
from agents import set_trace_processors
from langsmith.wrappers import OpenAIAgentsTracingProcessor

logging.basicConfig(
    filename=f"agent_log_{datetime.date.today()}.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

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
        "description": "Evaluates a math expression. Only use real numbers. Never use variable names.",
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
    logging.info(f"AGENT START - Goal: {goal}")
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful research agent. "
                "When a goal requires both a web search and a calculation, "
                "always search first to get the real number, "
                "then use that exact number in the calculation. "
                "Never pass variable names or placeholders to the calculate tool."
            )
        },
        {"role": "user", "content": goal}
    ]
    total_tokens = 0
    while True:
        response = client.chat.completions.create(
            model="gpt-4o", messages=messages, tools=tools)

        tokens_used = response.usage.total_tokens
        total_tokens += tokens_used
        cost_estimate = total_tokens * 0.000005
        logging.info(f"Tokens: {tokens_used} | Cost: ${cost_estimate:.4f}")

        message = response.choices[0].message
        if not message.tool_calls:
            logging.info(f"AGENT COMPLETE - Answer: {message.content}")
            print(message.content)
            return
        messages.append(message)
        for tc in message.tool_calls:
            tool_name = tc.function.name
            tool_args = json.loads(tc.function.arguments)
            logging.info(f"TOOL CALL: {tool_name} - Args: {tool_args}")
            result = calculate(**tool_args) if tool_name == "calculate" else search_web(**tool_args)
            logging.info(f"TOOL RESULT: {result}")
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})


if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    run_agent("What is the current price of Apple stock? Then calculate how much 500 shares are worth.")
