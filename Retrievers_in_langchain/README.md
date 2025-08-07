LangChain Retriever Examples
This directory contains examples of various retriever types in LangChain, which are essential for building effective Retrieval-Augmented Generation (RAG) systems.
What are Retrievers?
Retrievers are a core component in LangChain that fetch relevant documents from a data source in response to a user's query. This allows a Large Language Model (LLM) to generate answers based on specific, up-to-date information rather than just its internal knowledge.
Table of Contents
Based on Data Source
•	Vector Store Retriever
•	Wikipedia Retriever
Based on Retrieval Strategy
•	Maximum Marginal Relevance (MMR)
•	Multi-Query Retriever
•	Contextual Compression Retriever
Setup
1.	Install Libraries:
2.	pip install langchain-google-genai langchain-community faiss-cpu wikipedia langchain-cohere

3.	API Keys: Ensure your GOOGLE_API_KEY and COHERE_API_KEY are set up in your environment (e.g., in a .env file or Colab Secrets).
Retrievers Based on Data Source
🌎 Vector Store Retriever
The most common retriever. It performs a simple similarity search over a collection of documents you provide.
Example:
# Create a vector store
db = FAISS.from_texts(
    ["Paris is in France.", "London is in England."],
    embedding_function
)
# Create a retriever
retriever = db.as_retriever()
retriever.invoke("Which city is in France?")

📚 Wikipedia Retriever
Fetches documents directly from Wikipedia, acting as a real-time, general-knowledge data source.
Example:
from langchain_community.retrievers import WikipediaRetriever
retriever = WikipediaRetriever(top_k_results=1)
retriever.invoke("Srinivasa Ramanujan")

Retrievers Based on Retrieval Strategy
✨ Maximum Marginal Relevance (MMR) Retriever
Fetches a set of documents that are both relevant to the query and diverse from each other, which helps to avoid redundant information.
Example:
# Assumes 'db' is a pre-existing vector store
retriever = db.as_retriever(search_type="mmr")
retriever.invoke("Tell me about fruits.")

❓ Multi-Query Retriever
Uses an LLM to generate several different versions of your original question to get a more comprehensive set of results.
Example:
from langchain.retrievers.multi_query import MultiQueryRetriever
# Assumes 'retriever' and 'llm' are pre-existing
mq_retriever = MultiQueryRetriever.from_llm(retriever=retriever, llm=llm)
mq_retriever.invoke("What is there to do in New York City?")

🎯 Contextual Compression Retriever
First fetches a set of documents and then uses a compressor to filter them, returning only the most relevant snippets. This makes the final context for the LLM much cleaner.
Example:
from langchain.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereRerank

# Assumes 'base_retriever' is pre-existing
compressor = CohereRerank()
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=base_retriever
)
compression_retriever.invoke("What year was the first iPhone released?")

