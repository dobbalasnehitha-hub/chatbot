import streamlit as st
import ollama
st.title("Ai Chatbot")
prompt=st.text_input(" whats your doubt?")
if st.button("send"):
    response=ollama.chat(
        model="gemma3:1b",
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    st.write(response["message"]
             ["content"])


