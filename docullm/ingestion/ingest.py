from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader, UnstructuredMarkdownLoader, UnstructuredRSTLoader
from langchain.document_loaders import DirectoryLoader
from docullm.utils import getEmbeddings, getVectorStore


class DataIngestion:
    def __init__(self, model: str, db: str) -> None:
        self.model_name = model
        self.db_name = db
        self.embeddings = getEmbeddings(self.model_name)
        self.vectorstore = getVectorStore(self.db_name)
    
    def loadDocuments(self, root_dir: str) -> list:
        all_documents = []
        
        if "rst" in self.file_types:
            rst_loader = DirectoryLoader(root_dir, glob="./**/*.rst", loader_cls=UnstructuredRSTLoader)
            rst_documents = rst_loader.load()
            all_documents += rst_documents
            
        if "md" in self.file_types:
            md_loader = DirectoryLoader(root_dir, glob="./**/*.rst", loader_cls=UnstructuredMarkdownLoader)
            md_documents = md_loader.load()
            all_documents += md_documents
            
        return all_documents
    
    def ingestDocuments(self, documents):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        
        
    
    
    
if __name__ == "__main__":
    di = DataIngestion("openai", "chroma")
    di.loadDocuments("D:\CodeProjects\DocuLLM\mongo-python-driver-master")
    
    
    
    
    
    