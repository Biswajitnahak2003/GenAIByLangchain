from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title = "ai assistant",
    page_icon = "✨",
    layout = "centered",
)

st.title("The AI summarizer")
st.write("tell what you want to summarize.i will take care of the rest!!")

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

template = load_prompt("template.json")


user_input = st.text_input("Enter the topic you want to understand:")
style = st.selectbox("Select the style of explanation:", ["simple", "detailed", "technical"])
length = st.selectbox("Select the length of the explanation:", ["short", "medium", "long"])

if st.button("Summarize"):
    chain = template | llm
    result = chain.invoke({
        "topic": user_input,
        "style": style,
        "length": length
    })
    st.write(result)

