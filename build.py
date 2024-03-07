import os

import warnings
warnings.filterwarnings("ignore")

import git
from docullm.data import DataCollection
from docullm.store import VectorStore
from argparse import ArgumentParser

config = ""
CURR_PATH = os.path.curdir

def main():
    parser = ArgumentParser("Build the database of documents")
    parser.add_argument("--db_path", type=str, help="path where the database dir will be created")
    parser.add_argument("--repo_path", type=str, help="URL or local path of the repository. If you are \
                                                    using the URL, it will download the main branch")
    args = parser.parse_args()
    
    
    repo_name = os.path.basename(args.repo_path)
    if "http" in args.repo_path:
        local_repo_path = os.path.join(CURR_PATH, repo_name)
        git.Repo.clone_from(args.repo_path, local_repo_path)
    else:
        local_repo_path = args.repo_path


    # Data collection. Collects all the documentation data from the repository
    data = DataCollection(["md"])
    data.loadDocuments(local_repo_path)
    documents = data.getDocuments()
    
    vectordb = VectorStore(repo_name, "chroma", "cohere", args.db_path)
    vectordb.ingest(documents)
    
    print("Database built and documents ingested successfully!")
    
main()
        
    
