from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ("system","You are a helpful {domain} assistant."),
    ("human","explain the {topic} in simple terms")
    # SystemMessage(content = "You are a helpful {domain} assistant."),
    # HumanMessage(content = "explain the {topic} in simple terms")
])

prompt = chat_template.invoke({"domain":"biology", "topic":"photosynthesis"})

print(prompt)


