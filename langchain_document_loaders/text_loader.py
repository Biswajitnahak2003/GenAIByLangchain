from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2
)

# prompt1 = ChatPromptTemplate.from_template(
#     "Write a 100-word poem about the {topic}."
# )

parser = StrOutputParser()

# chain = prompt1 | llm | parser

# result = chain.invoke({"topic":"love"})

# file_name = "poem.txt"

# with open(file_name, "w",  encoding="utf-8")as f:
#     f.write(result)

# print("poem saved to file name {}".format(file_name))

loader = TextLoader("poem.txt", encoding="utf-8")

document = loader.load()

# print(document[0].page_content)
# print(document[0].metadata)

prompt2 = ChatPromptTemplate.from_template(
    "summarize the poem {poem}"
)

chain2 = prompt2 | llm | parser

result = chain2.invoke({"poem": document[0].page_content})
print(result)