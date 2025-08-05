from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="C:\\Users\\biswa\\genai_using_langchain\\langchain_document_loaders\\train.csv",
    encoding="utf-8" 
)

docs = loader.load()

print(len(docs))
print(docs[1])