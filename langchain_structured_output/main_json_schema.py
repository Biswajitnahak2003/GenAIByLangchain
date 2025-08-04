import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

with open("langchain_strutured_output/schema.json", "r") as f:
    json_schema = json.load(f)

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)

structured_llm = llm.with_structured_output(json_schema)

prompt = [ 
    HumanMessage(
        "Extract the user profile from this text: The user, John Doe, can be reached at john.doe@email.com. He is a premium subscriber."
    )
]

result = structured_llm.invoke(prompt)

print(result)