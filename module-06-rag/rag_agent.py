# Module 6 · rag_agent.py
# Install: pip install langchain langchain-openai langchain-chroma chromadb
# Set key: export OPENAI_API_KEY='sk-...'
# Run:     python rag_agent.py

# STEP 1 — Load
from langchain.document_loaders import TextLoader
loader = TextLoader("sample_doc.txt")
documents = loader.load()

# STEP 2 — Chunk
from langchain.text_splitter import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = splitter.split_documents(documents)

# STEP 3 and 4 — Embed and Store
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embeddings)

# STEP 5 — Retrieve and Answer
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
llm = ChatOpenAI(model="gpt-4o")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

questions = [
    "How many days can employees work remotely?",
    "What are the health insurance options?",
    "Is dental included?",
    "What is the waiting period before benefits begin?"
]

for q in questions:
    result = qa.invoke({"query": q})
    print(f"Q: {q}")
    print(f"A: {result['result']}")
    print()
