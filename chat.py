import streamlit as st
import random
import time
import vertexai
import requests
from vertexai.preview.language_models import ChatModel, InputOutputTextPair


vertexai.init(project="projectid", location="us-central1")

chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 1,
    "max_output_tokens": 1024,
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


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = novoPrompt(prompt)
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})