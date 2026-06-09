# Module 3 · Your First API Call
# Talk to GPT-4o from your own code. TYPE THIS YOURSELF first.
#
# Before running, set your key in the terminal (never in the file):
#   Mac/Linux:        export OPENAI_API_KEY='sk-your-actual-key-here'
#   Windows CMD:      set OPENAI_API_KEY=sk-your-actual-key-here

from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY from your environment automatically

# ── Part A: a plain question (a chatbot) ──────────────────────────────
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "What is an AI agent in one sentence?"}
    ],
)
print(response.choices[0].message.content)


# ── Part B: the same model, given a job — a Fraud Detection Specialist ─
# A system prompt is a job description you give the AI before the conversation
# starts. It shapes every response from that point on.
#
# Try it: run once with "2:47am", then change it to "2:47pm" and run again.
# Watch the risk level change — that knowledge came entirely from the system prompt.
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": """You are a senior fraud investigator at a major bank.
You have investigated over 10,000 fraud cases.
When given any information about a transaction, you analyze it
for risk patterns, unusual timing, suspicious amounts, and new
payees. You always give a risk level of LOW, MEDIUM, or HIGH
and explain your reasoning clearly.""",
        },
        {
            "role": "user",
            "content": "Transaction: $4,200 wire transfer at 2:47am to a new payee.",
        },
    ],
)
print(response.choices[0].message.content)
