from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name = "BAAI/bge-small-en-v1.5"
)
# text = "hello!Nice to meet you."
# vector = embedding.embed_query(text)

documents = [
    "Paris is a beautiful city known for its art and culture.",
    "The Eiffel Tower is a famous landmark in Paris.",
    "The best cheese comes from grass-fed cows in the Normandy region."
]

doc_vectors = embedding.embed_documents(documents)
print(str(doc_vectors))
print(len(doc_vectors))