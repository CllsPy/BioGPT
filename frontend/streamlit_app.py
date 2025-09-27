import streamlit as st
import requests

API_URL = "http://localhost:8000/ask"

st.title("BioGPT Chatbot - Saúde")

question = st.text_input("Pergunte sobre saúde:")
if st.button("Enviar"):
    if question:
        resp = requests.post(API_URL, json={"question": question})
        if resp.status_code == 200:
            st.write("Resposta:", resp.json()["answer"])
        else:
            st.error("Erro na API")
