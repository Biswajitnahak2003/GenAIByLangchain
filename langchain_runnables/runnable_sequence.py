from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a detailed documentation about the {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following documentation in three bullet points:\n\n{documentation}",
    input_variables=["documentation"]
)

chain = RunnableSequence(
    prompt1,
    llm,
    parser,
    lambda text: {"documentation": text},
    prompt2,
    llm,
    parser
)

result = chain.invoke({
    "topic": "runnables in langchain"
})

print(result)