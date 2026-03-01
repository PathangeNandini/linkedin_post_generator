# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# import os

# load_dotenv()

# llm=ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model_name="llama-3.3-70b-versatile")
# if __name__=="__main__":
#     response=llm.invoke("What are the two main ingradients in samosa")
#     print(response.content)

import streamlit as st
from langchain_groq import ChatGroq

groq_api_key = st.secrets["GROQ_API_KEY"]

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile"
)

if __name__ == "__main__":
    resp = llm.invoke("What are the two main ingredients of samosa?")
    print(resp.content)