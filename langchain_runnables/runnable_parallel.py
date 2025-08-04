from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0
)

parser = StrOutputParser()


prompt1 = ChatPromptTemplate.from_template(
    "Generate a detailed note about the {topic}"
)

prompt2 = ChatPromptTemplate.from_template(
    "Generate a quick note about the \n\n{topic}"
)

parallel_chain = RunnableParallel({
    "detailed_note" : RunnableSequence(prompt1, llm, parser),
    "quick_note" : RunnableSequence(prompt2, llm, parser)
})

result = parallel_chain.invoke({"topic":"lightGBM"})

print(result["detailed_note"])
print(result["quick_note"])
