# Module 3 · Talking to AI: Your First API Call

*Send a message to GPT-4o and get a response — in code.*

## The idea: an API is a waiter

You sit at a table (your code). You tell the waiter what you want (the OpenAI API).
The kitchen (GPT-4o) makes it. You get a result back. You never touch the stove.

> Users go to the chat window. **Builders use the API.**

## System prompts

A **system prompt** is a job description you give the AI before the conversation
starts. It shapes every response. A vague system prompt produces a vague agent; a
specific one produces a specialist.

The four-part pattern you will reuse all course long:

```
role  →  experience / backstory  →  what to focus on  →  what format to return
```

## Install

```bash
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install openai
```

## Set your key (every new terminal)

```bash
export OPENAI_API_KEY='sk-your-actual-key-here'    # Windows CMD: set OPENAI_API_KEY=...
```

## Lab

1. Type [`first_api_call.py`](first_api_call.py) yourself and run it.
2. Run the Fraud Detection Specialist. Then change `2:47am` to `2:47pm` and run again — watch the risk level change.
3. Open [`system_prompts.py`](system_prompts.py). Pick **three** personalities, ask each *"What is an AI agent?"*, and compare. Write your own for Experiment 3.

```bash
python first_api_call.py
```

Compare your files with the reference only **after** yours runs.

> Never put your API key in a file you push. Always use environment variables.
