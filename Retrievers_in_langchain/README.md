# 📌 What are Retrievers?

Retrievers are a core component in LangChain that fetch relevant documents from a data source in response to a user's query. This enables Large Language Models (LLMs) to generate accurate, grounded responses based on external knowledge, not just what they were trained on.

## 📚 Table of Contents
### 🔹 Based on Data Source
    🌎 Vector Store Retriever
    📚 Wikipedia Retriever

### 🔹 Based on Retrieval Strategy
    ✨ Maximum Marginal Relevance (MMR) Retriever
    ❓ Multi-Query Retriever
    🎯 Contextual Compression Retriever


## ⚙️ Setup

### Install Required Libraries:
```python
    pip install langchain-google-genai langchain-community faiss-cpu wikipedia langchain-cohere
```
### Set API Keys:

    Ensure GOOGLE_API_KEY is set in your environment, e.g., in a .env file or through Colab secrets.

## 🌎 Vector Store Retriever

The most common retriever. Performs a similarity search over a vectorized collection of your documents.

### Example:
 ```
from langchain_community.vectorstores import FAISS

db = FAISS.from_texts(
    ["Paris is in France.", "London is in England."],
    embedding_function
)
retriever = db.as_retriever()
retriever.invoke("Which city is in France?")
 ```
## 📚 Wikipedia Retriever

Fetches documents directly from Wikipedia, acting as a real-time general-knowledge retriever.

### Example:
 ```
from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=1)
retriever.invoke("Srinivasa Ramanujan")
 ```
## ✨ Maximum Marginal Relevance (MMR) Retriever

Returns results that are both relevant and diverse, avoiding repetition in search results.

### Example:
 ```
retriever = db.as_retriever(search_type="mmr")
retriever.invoke("Tell me about fruits.")
 ```
## ❓ Multi-Query Retriever

Uses an LLM to reformulate the query in multiple ways for better coverage and recall.

### Example:
 ```
from langchain.retrievers.multi_query import MultiQueryRetriever

mq_retriever = MultiQueryRetriever.from_llm(retriever=retriever, llm=llm)
mq_retriever.invoke("What is there to do in New York City?")
 ```
## 🎯 Contextual Compression Retriever

First retrieves documents, then filters them using a compressor (like rerankers) to keep only the most relevant snippets.

### Example:
 ```
from langchain.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereRerank

compressor = CohereRerank()
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)
compression_retriever.invoke("What year was the first iPhone released?")
 ```
# 📌 References
- [📚 LangChain Docs](https://docs.langchain.com/)
- [🔍 Retrievers in LangChain](https://docs.langchain.com/docs/modules/data_connection/retrievers/)
#  Author

    Biswajit Nahak
    BTech | ETC | @IIIT BBSR
