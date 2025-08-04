from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation",
    max_new_tokens= 256,
    temperature=0
)


model = ChatHuggingFace(llm = llm)

result = model.invoke("Hello")

print(result.content)