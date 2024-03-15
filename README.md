# DocuLLM
a documentation framework that can search and answers questions from existing docs. Currently it uses ChromaDB as database and Cohere as the LLM. You would need a Cohere API key set in your environment. Cohere has a free dev tier, check it out!

More LLM support on the way!

## Setup

```sh

# Clone the repository
git clone https://github.com/mayukh18/DocuLLM.git

# Install the dependencies
pip install -r requirements.txt
```

## Usage

#### 1. Ingest:
Ingest a repository to the system so that it can be queried upon. The `--update` flag is optional and updates a pre-existing repository in the database. The `--path` can be a URL or a local path.

```sh
python docullm.py --ingest --update --path "https://github.com/pandas-dev/pandas"
```

#### 2. Query:
Query the system with a question.

```sh
python docullm.py --query --repository pandas --question "how to do aggregation in pandas?"
```