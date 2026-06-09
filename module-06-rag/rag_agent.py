# Module 6 · RAG — Making Agents Smart About Your Documents
# Retrieval-Augmented Generation: connect the agent to YOUR data.
# TYPE THIS YOURSELF, one step at a time.
#
# Install:
#   pip install langchain langchain-openai langchain-chroma chromadb
# Set key:
#   export OPENAI_API_KEY='sk-...'
#
# The 5 steps: Load -> Chunk -> Embed -> Store -> Retrieve & Answer.

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

# STEP 1 — Load
loader = TextLoader("sample_doc.txt")
documents = loader.load()

# STEP 2 — Chunk
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = splitter.split_documents(documents)

# STEP 3 & 4 — Embed and Store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embeddings)

# STEP 5 — Retrieve and Answer
llm = ChatOpenAI(model="gpt-4o")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

# Ask several questions. The agent answers from the document — it does not make
# up information that is not there. Try a question that is NOT in the doc and see.
questions = [
    "How many days can employees work remotely?",
    "What are the health insurance options?",
    "Is dental included?",
    "What is the waiting period before benefits begin?",
]

for q in questions:
    result = qa.invoke({"query": q})
    print(f"Q: {q}")
    print(f"A: {result['result']}")
    print()
