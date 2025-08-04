from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("ai for summarizzing")
user_input = st.text_input("enter your prompt")

model = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

if st.button("summarize"):
    result = model.invoke(user_input)
    st.write(result)
