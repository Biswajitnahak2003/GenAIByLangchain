from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader(r"C:\Users\biswa\genai_using_langchain\langchain_document_loaders\HCIA-AI V3.5 Training Material.pdf")

docs = loader.load()

print(len(docs))
print(docs[1].page_content[:100])
print(docs[1].metadata)


# Other PDF loaders in LangChain Community
# ---------------------------------------------------


# PyPDF	Uses `pypdf` to load and parse PDFs	
# Unstructured	Uses Unstructured's open source library to load PDFs
# Amazon Textract	Uses AWS API to load PDFs	
# MathPix	Uses MathPix to load PDFs	
# PDFPlumber	Load PDF files using PDFPlumber	
# PyPDFDirectry	Load a directory with PDF files	
# PyPDFium2	Load PDF files using PyPDFium2	
# PyMuPDF	Load PDF files using PyMuPDF	
# PyMuPDF4LLM	Load PDF content to Markdown using PyMuPDF4LLM	
# PDFMiner	Load PDF files using PDFMiner	
# Upstage Document Parse Loader	Load PDF files using UpstageDocumentParseLoader	
# Docling	Load PDF files using Docling	