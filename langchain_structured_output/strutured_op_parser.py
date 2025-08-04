from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)

schema = (
    ResponseSchema(name = "fact1", description= "A fact about the topic"),
    ResponseSchema(name = "fact2", description= "Another fact about the topic"),
    ResponseSchema(name = "fact3", description= "A third fact about the topic")
)

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="give me three facts about the topic: {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | llm | parser

result = chain.invoke({"topic": "llms "})

print(result)