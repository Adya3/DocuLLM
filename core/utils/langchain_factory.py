from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings, CohereEmbeddings


def getEmbeddings(model_name):
    if model_name == "openai":
        return OpenAIEmbeddings
    elif model_name == "huggingface":
        return HuggingFaceEmbeddings
    elif model_name == "cohere":
        return CohereEmbeddings
    
def getVectorStore(db_name):
    if db_name == "chroma":
        return Chroma
    # elif db_name == "faiss":
    #     return Faiss
    