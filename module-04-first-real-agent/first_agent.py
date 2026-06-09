from openai import OpenAI
# Bring in the OpenAI library.

import json
# We need json to read the arguments the agent sends to our tools.

client = OpenAI()
# Connect to OpenAI. It reads your API key automatically from the environment.


def calculate(expression):
    return str(eval(expression))
# This is our tool. Two lines. It takes a math expression as text, runs it, and
# returns the answer as text. That is all it needs to do.


# Now the tool schema. This is the description the AI reads to understand what the
# tool does and when to use it.
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
}]
# The name must exactly match the Python function name. The description tells the AI
# when to use it. The parameters tell it what to pass in.


# Now the agent loop. This is the heart of the whole system.
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
            result = calculate(**json.loads(tc.function.arguments))
            print(f"TOOL: calculate | RESULT: {result}")
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})
# messages starts as a list with just the user's goal.
# while True means loop forever — until we return.
# We ask GPT-4 what to do next — give it the messages and the tools list.
# If the AI has no tool calls, it is done. Print the answer and return.
# If it has a tool call, we run calculate with the arguments it chose.
# We print the result so we can watch what the agent is doing.
# We add the result back into messages so the AI can read it on the next loop.


run_agent("If one share of Apple stock costs 345 dollars, how much are 754 shares worth?")
