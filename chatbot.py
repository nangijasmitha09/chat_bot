import streamlit as st
import ollama
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="robot"
)
st.title("My AI Chatbot")
st.caption ("Powered by Ollama + streamlit")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
prompt = st.chat_input("Type your message...")
if prompt:
    st.session_state.messages.append({
        "role":"user",
        "content":prompt
    })
    with st.chat_message("user"):
        st.write(Prompt)
    response=ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages.append
    )
    answer=response["messages"]["content"]
    st.session_state.messages.append({
        "role":"assistant",
        "content":answer
    })
    with st.chat_message("assistant"):
        st.write(answer)