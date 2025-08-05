from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# splitting a text into chunks
# text = """Early mornings hold a quiet kind of magic. The world feels softer, calmer, as if time itself is stretching before the day begins. A cool breeze carries the scent of dew-kissed grass, and golden sunlight slowly spills across the horizon. Birds chatter in gentle harmony, unaware of the chaos that will soon awaken. In these moments, life feels simple, unhurried, and full of possibility—a fresh page waiting to be written."""

# splitter = CharacterTextSplitter(
#     chunk_size = 100,
#     chunk_overlap = 0,
#     separator = ""
# )

# result = splitter.split_text(text)

# print(result)

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0,
    separator = ""
)

loader = PyPDFLoader(r"C:\Users\biswa\genai_using_langchain\langchain_text_splitters\eth_ipcv.pdf")

documents = loader.load()

result = splitter.split_documents(documents)

print(len(result))
print(result[10].page_content)