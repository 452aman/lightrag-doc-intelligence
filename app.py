import streamlit as st

st.set_page_config(page_title="LightRAG Document Intelligence System", page_icon="🧠")
st.title("Ask me anything")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.header("Upload your document")
    uploaded_file = st.file_uploader("Choose a file", type="pdf")

for message in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(message)


user_message = st.chat_input("Type your question here...")

if user_message:
    st.session_state.chat_history.append(user_message)
    st.rerun() 