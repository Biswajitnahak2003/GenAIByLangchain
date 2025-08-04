from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.1,
)

prompt1 = PromptTemplate(
    template = "name a city of {country}",
    input_variables=["country"],
)

prompt2 = PromptTemplate(
    template = "name the most famous food of the {place}",
    input_variables = ["place"],
)

parser = StrOutputParser()

chain = prompt1 | llm | parser | prompt2 | llm | parser

result = chain.invoke({"country": "India"})

print(result)

### install Grandalf to visualize the chain
chain.get_graph().print_ascii()