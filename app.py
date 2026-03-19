import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_groq import ChatGroq


st.set_page_config(page_title="LightRAG Document Intelligence System", page_icon="🧠")
st.title("Ask me anything")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.header("Upload your document")
    uploaded_file = st.file_uploader("Choose a file", type="pdf")


for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


user_message = st.chat_input("Type your question here...")

if user_message:

    st.session_state.chat_history.append({"role": "user", "content": user_message})
    
    with st.chat_message("user"):
        st.write(user_message)
        
    try:
        response = llm.invoke(user_message)
        actual_text = response.content
        
        st.session_state.chat_history.append({"role": "assistant", "content": actual_text})
        
        st.rerun() 
        
    except Exception as e:
        st.error(f"Error: {e}")