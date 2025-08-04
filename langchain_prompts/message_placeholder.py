from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate([
    ("system", "You are a costumer support assistant."),
    MessagesPlaceholder(variable_name = "chat_history"),
    ("human","{query}")
])

chat_history = []

with open("langchain_prompts/chat_history.txt") as f:
    chat_history.extend(f.readlines())


print(chat_history)


prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "What is the status of my order?"
})

print(prompt)

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7 
)

result = llm.invoke(prompt)
print(result)
