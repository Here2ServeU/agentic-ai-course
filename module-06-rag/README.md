# Module 6 · RAG: Making Agents Smart About Your Documents

*RAG = Retrieval-Augmented Generation. Connect your agent to real data.*

## The idea: an open-book exam

Without RAG, the AI answers from memory alone. With RAG, you hand it the exact pages
of the textbook relevant to the question, right before it answers.

The five steps:

1. **Load** your documents.
2. **Chunk** them into pieces.
3. **Embed** each chunk into a list of numbers.
4. **Store** the embeddings in a vector database.
5. **Retrieve** the most relevant chunks for a question and give them to the AI.

## Install

```bash
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install openai chromadb
export OPENAI_API_KEY='sk-...'
```

## Lab

Build [`rag_agent.py`](rag_agent.py) yourself, all five steps:

1. **Load** — read [`sample_doc.txt`](sample_doc.txt) into a string.
2. **Chunk** — split the text into overlapping pieces (`size=300`, `overlap=50`).
3. **Embed** — turn each chunk into a vector with `text-embedding-3-small`.
4. **Store** — add the chunks and their embeddings to a Chroma collection.
5. **Retrieve and answer** — embed the question, query for the top 2 chunks, and
   hand them to `gpt-4o` with a system prompt that says *"Answer using only the
   context provided."*

The file ends with four questions about an employee benefits document:

```python
questions = [
    "How many days can employees work remotely?",
    "What are the health insurance options?",
    "Is dental included?",
    "What is the waiting period before benefits begin?"
]
```

```bash
python3 rag_agent.py
```

[`sample_doc.txt`](sample_doc.txt) is a starter document — **replace it with 200+ words
from your own target domain** and rewrite the questions to match. Run three questions
that ARE in the document, then one that is NOT, and note how it responds.

> **Boundary test:** the agent answers from the document and does not invent facts
> that are not there. That is the whole point of RAG.
