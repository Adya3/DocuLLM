from langchain.text_splitter import RecursiveCharacterTextSplitter
from docullm.utils import getVectorStore, getEmbeddings


class VectorStore:
    def __init__(self, db_name: str, embedding_name: str, persist_dir: str) -> None:
        self.persist_dir = persist_dir
        self.embeddings = getEmbeddings(embedding_name)()
        self.db = getVectorStore(db_name)
        
    def ingest(self, documents: list) -> None:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        self.vectorstore = self.db.from_documents(documents=texts, 
                                    embedding=self.embeddings,
                                    persist_directory=self.persist_dir)
        self.vectorstore.persist()
        
    def load(self):
        self.vectorstore = self.db(self.persist_dir, self.embeddings)
    
    def getRetriever(self, k):
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": k})
        return retriever
        