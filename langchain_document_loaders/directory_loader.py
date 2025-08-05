from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = r"C:\Users\biswa\genai_using_langchain\langchain_document_loaders\notes",
    glob = "*.pdf",
    loader_cls=PyPDFLoader
)

# docs = loader.load()
docs = loader.lazy_load()


# print(len(docs))
# print(docs[0].page_content)
# print(docs[1].metadata)

for document in docs:
    print(document.metadata)