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
pip install langchain langchain-openai langchain-chroma chromadb
```

## Lab

1. Build [`rag_agent.py`](rag_agent.py) yourself, all five steps.
2. [`sample_doc.txt`](sample_doc.txt) is a starter document — **replace it with 200+ words from your own target domain.**
3. Run three questions that ARE in the document, then one that is NOT. Note how it responds.

```bash
python rag_agent.py
```

> **Boundary test:** the agent answers from the document and does not invent facts
> that are not there. That is the whole point of RAG.
