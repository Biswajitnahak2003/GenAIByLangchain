from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)

template1 = PromptTemplate(
    template = "write detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template = "write a 5 line summary on the following text. {text}",
    input_variables=["text"]
)


chain = template1 | llm | parser | template2 | llm | parser

result = chain.invoke({
    "topic": "black hole"
})

print(result)
