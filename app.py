import os
import warnings
warnings.filterwarnings("ignore")

import chromadb
from langchain.llms import OpenAI, Cohere
from langchain.chains import RetrievalQA
from docullm.data import DataCollection
from docullm.store import VectorStore
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings, CohereEmbeddings

ABS_PATH = "D:\CodeProjects\DocuLLM"
DB_DIR = os.path.join(ABS_PATH, "embed-db-mongo")
print(DB_DIR)

if __name__ == "__main__":
    # data = DataCollection(["md"])
    # data.loadDocuments("D:\CodeProjects\DocuLLM\data\mongo-python-driver-master")
    # documents = data.getDocuments()
    
    # print(DB_DIR)
    # vectordb = VectorStore("chroma", "cohere", DB_DIR, client_settings)
    # # vectordb.ingest(documents)
    # vectordb.load()
    
    # retriever = vectordb.getRetriever(k=4)
    
    # qa_chain = RetrievalQA.from_chain_type(llm=Cohere(), 
    #                               chain_type="stuff", 
    #                               retriever=retriever, 
    #                               return_source_documents=True)

    # query = "How does aggregation work?"
    # llm_response = qa_chain(query)
    # print(llm_response)

    # embeddings = CohereEmbeddings()

    # vectorstore = Chroma(
    #     collection_name="langchain_store",
    #     embedding_function=embeddings,
    #     persist_directory=DB_DIR,
    # )

    # print("Docs", len(documents))
    # vectorstore.add_documents(documents=documents, embedding=embeddings)
    # print("Done")


    embeddings = CohereEmbeddings()

    vectorstore = Chroma(
        collection_name="langchain_store",
        embedding_function=embeddings,
        persist_directory=DB_DIR,
    )
    
    # result = vectorstore.similarity_search_with_score(query="mongo", k=4)
    # print(result)
    
    retriever = vectorstore.as_retriever(k=6)
    
    qa_chain = RetrievalQA.from_chain_type(llm=Cohere(), 
                                  chain_type="stuff", 
                                  retriever=retriever,
                                  return_source_documents=False)

    query = """
    INSTRUCTION: Only use the context provided to answer the question. Don't use external info.
    Output with a code snippet if possible. Output should be in markdown.
    
    QUESTION: How does aggregation work?
    """
    llm_response = qa_chain(query)
    print(llm_response)

    with open("result.md", "w") as fp:
        fp.write(llm_response["result"])
    