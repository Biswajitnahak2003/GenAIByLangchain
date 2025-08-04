from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader(r"C:\Users\biswa\genai_using_langchain\langchain_document_loaders\HCIA-AI V3.5 Training Material.pdf")

docs = loader.load()

print(docs)
