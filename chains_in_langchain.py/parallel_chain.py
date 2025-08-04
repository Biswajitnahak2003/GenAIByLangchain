from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

llm1 = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    temperature = 0.7
)


llm2 = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.7
)


prompt1 = PromptTemplate(
    template = "give me a detailed report on the {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "give me 5 MCQs from the {topic}",
    input_variables = ["topic"]
)

prompt3 = PromptTemplate(
    template = "merge both the report->{report} and MCQS->{MCQs} in a single document",
    input_variables = ["report","MCQs"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "report" : prompt1 | llm1 | parser,
    "MCQs" : prompt2 | llm2 | parser
})

merged_chain = prompt3 | llm1 | parser 

chain = parallel_chain | merged_chain

topic = """Why use Pydantic?¶

    Powered by type hints — with Pydantic, schema validation and serialization are controlled by type annotations; less to learn, less code to write, and seamless integration with your IDE and static analysis tools. Learn more…
    Speed — Pydantic's core validation logic is written in Rust. As a result, Pydantic is among the fastest data validation libraries for Python. Learn more…
    JSON Schema — Pydantic models can emit JSON Schema, allowing for easy integration with other tools. Learn more…
    Strict and Lax mode — Pydantic can run in either strict mode (where data is not converted) or lax mode where Pydantic tries to coerce data to the correct type where appropriate. Learn more…
    Dataclasses, TypedDicts and more — Pydantic supports validation of many standard library types including dataclass and TypedDict. Learn more…
    Customisation — Pydantic allows custom validators and serializers to alter how data is processed in many powerful ways. Learn more…
    Ecosystem — around 8,000 packages on PyPI use Pydantic, including massively popular libraries like FastAPI, huggingface, Django Ninja, SQLModel, & LangChain. Learn more…
    Battle tested — Pydantic is downloaded over 360M times/month and is used by all FAANG companies and 20 of the 25 largest companies on NASDAQ. If you're trying to do something with Pydantic, someone else has probably already done it. Learn more…

Installing Pydantic is as simple as: pip install pydantic"""

result = chain.invoke({"topic":topic})

print(result)

chain.get_graph().print_ascii()