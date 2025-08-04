from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline 

import os
os.environ["HF_HOME"] = "D:/HuggingFace" 

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 256,
        "top_k": 50,
        "temperature": 0.7,
    },
)

print("Model loaded successfully!")

model = ChatHuggingFace(llm = llm)


result = model.invoke("What is the best way to learn about Large Language Models?")

print(result.content) 
