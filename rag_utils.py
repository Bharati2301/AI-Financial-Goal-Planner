from sentence_transformers import SentenceTransformer
from langchain.schema import Document
from langchain_chroma import Chroma
from langchain.vectorstores.base import VectorStoreRetriever


class LocalEmbedding:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        return self.model.encode(texts, convert_to_tensor=False).tolist()

    def embed_query(self, text):
        return self.model.encode(text, convert_to_tensor=False).tolist()


def get_relevant_strategies(goal_query):
    embedding_function = LocalEmbedding()
    vectordb = Chroma(persist_directory="chroma_db", embedding_function=embedding_function)
    retriever: VectorStoreRetriever = vectordb.as_retriever(search_kwargs={"k": 3})
    return retriever.invoke(goal_query)

