import json
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

def build_vectorstore():
    with open("strategy_data.json", "r") as f:
        data = json.load(f)

    documents = []
    for entry in data:
        content = f"Goal: {entry['goal']}\nStrategy: {entry['strategy']}"
        documents.append(Document(page_content=content))

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(documents, embedding=embeddings, persist_directory="chroma_db")
    vectordb.persist()
    print("Vector DB created successfully.")

if __name__ == "__main__":
    build_vectorstore()
