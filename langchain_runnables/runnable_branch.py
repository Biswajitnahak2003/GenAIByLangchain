from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import  RunnableLambda, RunnableParallel,RunnablePassthrough,RunnableBranch

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0
)

parser = StrOutputParser()

prompt1 = ChatPromptTemplate.from_template(
    "make a detailed report for the following topic-> {topic}"
)

prompt2 = ChatPromptTemplate.from_template(
    "summarize the following topic in 100 words: {topic}"
)
first_chain = prompt1 | llm | parser

second_chain = RunnableBranch(
    (lambda x: len(x.split())>500, prompt2 | llm | parser),
    RunnablePassthrough()
)

final_chain = first_chain | second_chain

result = final_chain.invoke({"topic": "fastapi"})

print(result)