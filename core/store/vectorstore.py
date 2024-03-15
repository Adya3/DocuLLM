from langchain.text_splitter import RecursiveCharacterTextSplitter
from core.utils import getVectorStore, getEmbeddings


class VectorStore:
    def __init__(self, collection_name: str, db_type: str, embedding_type: str, persist_dir: str) -> None:
        self.persist_dir = persist_dir
        self.collection_name = collection_name
        self.embeddings = getEmbeddings(embedding_type)
        self.db = getVectorStore(db_type)
        self.load()
        
    def load(self):
        self.vectorstore = self.db(
            collection_name=self.collection_name,
            embedding_function=self.embeddings(),
            persist_directory=self.persist_dir,
        )
        
    def ingest(self, documents: list) -> None:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        self.vectorstore.add_documents(documents=texts, 
                                    embedding=self.embeddings(),
                                    persist_directory=self.persist_dir)
        self.vectorstore.persist()
    
    def getRetriever(self, k):
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": k})
        return retriever
        