from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    temperature = 0
)


class classifier(BaseModel):
    topic: Literal["physics", "math"] = Field(
        description = "the category of users question"
    )


parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object = classifier)


prompt1 = PromptTemplate(
    template = "Given the user question below, classify it as either physics or math from\n {format_instructions}\nQuestion: {Question}",
    input_variables = ["Question"],
    partial_variables = {"format_instructions":parser2.get_format_instructions()}
)
classifier_chain = prompt1 | llm | parser2

prompt2 = PromptTemplate(
    template = "You are a physicist. Solve the following problem: {Question}",
    input_variables = ["Question"]
)

prompt3 = PromptTemplate(
    template = "You are a mathematician. Solve the following problem: {Question}",
    input_variables = ["Question"]
)

branch_chain = RunnableBranch(
    (lambda x:x["classification"].topic == "physics", prompt2 | llm | parser),
    (lambda x:x["classification"].topic == "math", prompt3 | llm | parser),
    RunnableLambda(lambda x: "your question is not related to math or physics")
)

chain = {
    "classification": classifier_chain,
    "Question": lambda x: x["Question"] 
} | branch_chain

result = chain.invoke({
    "Question": "how to calculate area of a triangle"
})

print(result)