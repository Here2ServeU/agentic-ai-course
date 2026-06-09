# Module 5 · Memory and Multi-Step Thinking

*Add conversation memory, then give the agent goals that need 3+ steps.*

## The idea

An agent without memory is like an assistant who forgets you the moment you stop talking.

- **Short-term memory** = the conversation history (what happened earlier in *this* chat).
- **Long-term memory** = stored information that persists across conversations (Module 6).

Today: short-term. The trick is simple — **keep a list of all messages and send the
whole list every time.**

## Install

```bash
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install openai duckduckgo-search
```

## Lab

1. Type and run [`memory_demo.py`](memory_demo.py) — see the agent forget, then remember.
2. Type [`memory_agent.py`](memory_agent.py) — the Module 4 agent plus a system prompt that makes it plan a multi-step goal.

```bash
python memory_demo.py
python memory_agent.py
```

Watch the agent search, process results, calculate, then summarize — multiple steps,
multiple tool calls, **one goal**. Compare with the reference files only after yours run.
