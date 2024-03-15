import os

import warnings
warnings.filterwarnings("ignore")

import git
from core.data import DataCollection
from core.store import VectorStore
from core.utils import load_config
from argparse import ArgumentParser

config = load_config("config.yaml")

def main():
    parser = ArgumentParser("Run queries and ask questions based on the documentation of a codebase")
    parser.add_argument("--ingest", action="store_true", help="Set this flag to ingest a repository into the database")
    parser.add_argument("--query", action="store_true", help="Set this flag to query the database with a question")
    parser.add_argument("--path", type=str, help="URL or local path of the repository. If you are \
                                                    using the URL, it will download the main branch")
    parser.add_argument("--update", action="store_true", help="Set this flag to update a pre-exxisting repository data")
    args = parser.parse_args()
    
    if os.path.exists(config['download_path']) == False:
        raise Exception("Please provide a valid \'download_path\' in the config")
    if os.path.exists(config['base_db_path']) == False:
        raise Exception("Please provide a valid \'base_db_path\' in the config")
    
    if args.ingest:
        ingest(args)
    elif args.query:
        query(args)
        
def query(args):
    pass
        
def ingest(args):
    repo_name = os.path.basename(args.path)
    if "http" in args.path:
        local_repo_path = os.path.join(config['download_path'], repo_name)
        git.Repo.clone_from(args.path, local_repo_path)
    else:
        local_repo_path = args.path


    # Data collection. Collects all the documentation data from the repository
    data = DataCollection(["md"])
    data.loadDocuments(local_repo_path)
    documents = data.getDocuments()
    
    db_path = os.path.join(config['base_db_path'], f"db_{repo_name})
    if os.path.exists(db_path) and args.update == False:
        print("Database already exists. Please set \'update\' = True to update the repository data")
        return
    
    vectordb = VectorStore(repo_name, "chroma", "cohere", db_path)
    vectordb.ingest(documents)
    print("Database built and documents ingested successfully!")
    
    
if __name__ == "__main__":
    main()
        
    
