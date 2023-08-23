import streamlit as st
from requests_html import HTMLSession
import requests
import vertexai 
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
vertexai.init(project="projectid", location="us-central1")

sess = HTMLSession()
#generate the documentation for the function bellow 


chat_model = ChatModel.from_pretrained("codechat-bison@001")
parameters = {
    "temperature": 1,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}

filename = "ifelse-wo-break"
with open(filename, "r") as f:
    contextTextFromFile = f.read()



appContext = contextTextFromFile

chat = chat_model.start_chat(
    context=appContext,
)

def novoPrompt(meuPrompt):
    response = chat.send_message(meuPrompt, **parameters)
    return response.text



st.title('Vertex APIs')

Prompt = st.text_area("Prompt", """aaaaaa""")

if st.button("Run"):
    st.markdown("### Result:")
    st.write(novoPrompt(Prompt))
