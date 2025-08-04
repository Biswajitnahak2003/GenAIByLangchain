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

def word_count(text):
    return len(text.split())

prompt = ChatPromptTemplate.from_template(
    "tell me a joke about the {topic}"
)

joke_gen_chain = RunnableSequence(prompt, llm, parser)

parallel_chain = RunnableParallel({
    "joke":RunnablePassthrough(),
    "word_count":RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "cats"})

print("""{}\n\n word count-{}""".format(result["joke"], result["word_count"]))