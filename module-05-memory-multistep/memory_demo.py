# Module 5 · Why Memory Matters (and how to add it)
# Run this to SEE the problem first, then the fix. TYPE IT YOURSELF.

from openai import OpenAI

client = OpenAI()


# ── The problem: no memory. Every call is completely isolated. ────────
def ask_no_memory(question):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content


print("--- No memory ---")
print(ask_no_memory("My name is Emmanuel."))
print(ask_no_memory("What is my name?"))   # It does not know.


# ── The fix: keep a list. Every message travels with every request. ───
conversation_history = []


def chat_with_memory(user_message):
    conversation_history.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation_history,
    )
    ai_response = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": ai_response})
    return ai_response


print("\n--- With memory ---")
print(chat_with_memory("My name is Emmanuel and I am building a fraud detection agent."))
print(chat_with_memory("What am I building?"))
print(chat_with_memory("What industry does that apply to?"))
