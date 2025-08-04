from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="tell me 10 names about this topic-> {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="from those 10 names from the {topic} find 1 best name that related to lord Jagannath",
    input_variables=["topic"]
)

first_chain = RunnableSequence(prompt1, llm, parser)

parallel_chain = RunnableParallel({
    "names_10" : RunnablePassthrough(),
    "name": RunnableSequence(prompt2, llm, parser)
})

final_chain = RunnableSequence(first_chain, parallel_chain)

result = final_chain.invoke({
    "topic" : "odia gods related names"
})

print(result)