from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

parser = JsonOutputParser()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)

template = PromptTemplate(
    template = "give me a json object with the following keys: name, age, and city.",
    input_variables = [],
    partial_variables = {"format_instruction": parser.get_format_instructions() }
)

chain = template | llm | parser 

result = chain.invoke({})

print(result)
print(type(result))