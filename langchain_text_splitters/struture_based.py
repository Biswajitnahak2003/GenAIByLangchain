from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# text  = """Early mornings hold a quiet kind of magic. The world feels softer, calmer, as if time itself is stretching before the day begins. A cool breeze carries the scent of dew-kissed grass, and golden sunlight slowly spills across the horizon. Birds chatter in gentle harmony, unaware of the chaos that will soon awaken. In these moments, life feels simple, unhurried, and full of possibility—a fresh page waiting to be written."""

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=0
# )

# docs = splitter.split_text(text)

# print(len(docs))
# print(docs)


text = """import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Your random password is:", generate_password(16))
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0
)

docs = splitter.split_text(text)

print(len(docs))
print(docs[1])