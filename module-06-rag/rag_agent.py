# Module 6 · rag_agent.py
# Install: pip install openai chromadb
# Set key: export OPENAI_API_KEY='sk-...'
# Run:     python3 rag_agent.py

import os
from openai import OpenAI
import chromadb

client = OpenAI()
chroma = chromadb.Client()
collection = chroma.get_or_create_collection("docs")

# STEP 1 — Load
with open("sample_doc.txt", "r") as f:
    text = f.read()

# STEP 2 — Chunk
def chunk_text(text, size=300, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return chunks

chunks = chunk_text(text)

# STEPS 3 and 4 — Embed and Store
for i, chunk in enumerate(chunks):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )
    collection.add(
        documents=[chunk],
        embeddings=[response.data[0].embedding],
        ids=[f"chunk_{i}"]
    )

# STEP 5 — Retrieve and Answer
def ask(question):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=question
    )
    results = collection.query(
        query_embeddings=[response.data[0].embedding],
        n_results=2
    )
    context = "\n".join(results["documents"][0])
    answer = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Answer using only the context provided."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ]
    )
    return answer.choices[0].message.content

questions = [
    "How many days can employees work remotely?",
    "What are the health insurance options?",
    "Is dental included?",
    "What is the waiting period before benefits begin?"
]

for q in questions:
    print(f"Q: {q}")
    print(f"A: {ask(q)}")
    print()