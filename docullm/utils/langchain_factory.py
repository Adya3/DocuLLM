from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings


def getEmbeddings(model_name):
    if model_name == "openai":
        return OpenAIEmbeddings()
    elif model_name == "huggingface":
        return HuggingFaceEmbeddings()
    
def getVectorStore(db_name):
    if db_name == "chroma":
        return Chroma
    # elif db_name == "faiss":
    #     return Faiss
    