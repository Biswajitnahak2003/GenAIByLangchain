from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0
)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template(
    "can you please answer my {question} \n using the following context: {context}"
)

url = "https://www.amazon.in/amazon-basics-Ballpoint-Lightweight-Professional/dp/B0CWVGKN7V/ref=sr_1_10?_encoding=UTF8&content-id=amzn1.sym.113c2269-a035-4fd3-b2ad-5f3955fb149a&dib=eyJ2IjoiMSJ9.C2-HBiCHLahnZN_vR5nK5fDbRQeK2RdLgGyFrNK0KwQ_4fQNfjz_3XpYwJ-w1OfuGLPIk44eHD_ZJ2o7EZvj5Py8YIvU_ktazNd4Ue8hg-t2NRTN3ytWYJGOPX_XNSKvKZ7TKpJN5EBzDezzyjuWrPri7GXeXh1TC53icGBReJj5VuloMx3hGqZZXRQCeKJyhcmz91llGzNY8PLl7j34zU7sIkCAm_AkUUHZZDglSEHWV8tEtlFvtVEDiumI0SO_U-R8EK-R84wesgjTFZEUIYmb5gMzqdcu-fYI4yhjF6I.ylRcY0CEHJlcGfWe_FXgxImAq6SXKvwq2zIBtnC9uDI&dib_tag=se&pd_rd_r=50cfa086-2dd6-4d04-8ab5-1cc1692e196f&pd_rd_w=C0xZ4&pd_rd_wg=h3u7H&qid=1754411057&refinements=p_85%3A10440599031&rps=1&s=office&sr=1-10&th=1"

loader = WebBaseLoader(url)
docs = loader.load()

chain = prompt | llm | parser

result = chain.invoke({
    "question": "What is the price of the product?",
    "context": docs[0].page_content
})

print(len(docs))
print(result)