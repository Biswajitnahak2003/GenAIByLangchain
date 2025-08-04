from langchain_google_genai import GoogleGenerativeAIEmbeddings
import numpy as np
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model = "models/gemini-embedding-001",
    dimensions = 300
)

documents = [
    "The new electric car model boasts a 500-mile range.",
    "Solar panels can significantly reduce your electricity bill.",
    "The stock market saw a dip in tech company shares this week.",
    "For a healthy diet, it's important to eat fruits and vegetables.",
    "Quantum computing could revolutionize data processing."   
]

query = "How can I save money on power for my home?"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

similarity_scores = cosine_similarity([query_embedding],doc_embeddings)[0]

best_match_index = np.argmax(similarity_scores)
best_match = documents[best_match_index]
print("Similarity scores:", similarity_scores)
print("best_match scores is :", best_match_index)
print(query)
print("answer:", best_match)


# index,similarity_scores = sorted(list(enumerate(similarity_scores)),key = lambda x:x[1])[-1]

# print(query)
# print(documents[index])
# print("similarity score is:",similarity_scores)