from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel,RunnablePassthrough

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0
)

parser = StrOutputParser()

bind_llm = llm.bind(stop = ["robot"])

prompt = ChatPromptTemplate.from_template(
    "tell me a story about robotics and ai"
)

chain = prompt | bind_llm | parser

result = chain.invoke({})

print(result)