# Module 5 · Memory and Multi-Step Thinking

*Add conversation memory, then give the agent goals that need 3+ steps.*

## The idea

An agent without memory forgets you the moment you stop talking.

- **Short-term memory** = the conversation history (what happened earlier in *this* chat).
- **Long-term memory** = stored information that persists across conversations (Module 6).

The trick for short-term memory: **keep a list of all messages and send the whole list
every time.**

## Install

```bash
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install openai
export OPENAI_API_KEY='sk-...'
```

## Lab 5.1 — Build the memory system

Type [`memory_agent.py`](memory_agent.py) yourself and run it. Watch the agent forget,
then remember.

```bash
python memory_agent.py
```

## Lab 5.2 — Add memory + planning to your Module 4 agent

Open `first_agent.py` from Module 4 and add a system prompt at the top of `run_agent`:

```python
def run_agent(goal):
    messages = [
        {"role": "system", "content": "You are a helpful research agent. "
            "You break complex goals into steps, use your tools systematically, "
            "and give clear final answers. Always show your reasoning."},
        {"role": "user", "content": goal}
    ]
    # ... rest of the loop is unchanged ...
```

Then run a multi-step goal:

```python
run_agent(
    "Search for the latest news about electric vehicles. "
    "Then search for Tesla stock price. "
    "Then calculate the value of 100 shares. "
    "Finally, summarize everything in 3 bullet points."
)
```

Watch the agent search, process results, calculate, then summarize — multiple steps,
multiple tool calls, **one goal**.
