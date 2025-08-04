from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

chat_history = [
    SystemMessage(content = "You are a helpful assistant. "
    "Answer the user's questions in a friendly manner.")
]

while True:
    user_input = input("you: ")
    chat_history.append(HumanMessage(content = user_input))
    if user_input == "exit":
        break
    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content = result))
    print("AI:",result)

print("Chat history:", chat_history)
