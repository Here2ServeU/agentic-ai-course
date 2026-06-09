# Module 1 · What Is an AI Agent?

*For complete beginners. No experience required.*

## The one idea

> **A chatbot answers. An agent acts.**

Write that down. It is the most important sentence in this course.

## The 4 parts of every agent

1. **Brain** — the large language model (GPT-4o). It thinks and decides.
2. **Tools** — what the agent can *do*: search the web, read a file, call an API, calculate.
3. **Memory** — short-term (this conversation) and long-term (stored, retrieved when needed).
4. **Loop** — think → act → observe → think again, until the goal is complete.

## Set up your computer

1. Install **Python 3.11+** — [python.org/downloads](https://www.python.org/downloads). On Windows, check **"Add Python to PATH."**
2. Install **VS Code** — [code.visualstudio.com](https://code.visualstudio.com).
3. Get an **OpenAI API key** — [platform.openai.com](https://platform.openai.com). Save it somewhere safe.

## Lab

```bash
# 1. Create + activate your virtual environment
python3 -m venv venv          # Windows: python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Run your first program
python hello.py
```

Expected output:

```
Hello, I am an AI agent builder.
I start today.
```

**Type `hello.py` yourself first.** Then compare with [`hello.py`](hello.py) in this folder.

When you are done: `deactivate`
