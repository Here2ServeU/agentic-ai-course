# Module 3 · first_api_call.py
# Set your key first (never in the file):
#   Mac/Linux:   export OPENAI_API_KEY='sk-your-actual-key-here'
#   Windows CMD: set OPENAI_API_KEY=sk-your-actual-key-here
# Run: python first_api_call.py

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "What is an AI agent in one sentence?"}
    ]
)

print(response.choices[0].message.content)
