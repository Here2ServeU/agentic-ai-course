from openai import OpenAI
# "from openai" means: from the openai library we just installed.
# "import OpenAI" means: bring in the main tool from that library.
# This one line gives us everything we need to talk to GPT-4.

client = OpenAI()
# This creates a connection to OpenAI. It automatically reads your API key from your
# environment — the key you set up as an environment variable. We will set that in a
# moment.

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "What is an AI agent in one sentence?"}
    ]
)
# This is the actual API call. "model" tells OpenAI which AI we want — gpt-4o is the
# most capable. "messages" is the conversation. "role: user" means this message is
# coming from us. "content" is what we are saying.

print(response.choices[0].message.content)
# This prints the AI's response. "choices[0]" gets the first response.
# ".message.content" gets the actual text.
