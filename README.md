# codey-examples


```
export PROJECT_ID="your-project-id

pip install streamlit 
pip install vertexai

streamlit run app.py
streamlit run chat.py
```


## Examples from the documentation 

https://cloud.google.com/vertex-ai/docs/samples/aiplatform-sdk-code-chat?hl=en

```python
from vertexai.preview.language_models import CodeChatModel


def write_a_function(temperature: float = 0.5) -> object:
    """Example of using Code Chat Model to write a function."""

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1024,  # Token limit determines the maximum amount of text output.
    }

    code_chat_model = CodeChatModel.from_pretrained("codechat-bison@001")
    chat = code_chat_model.start_chat()

    response = chat.send_message(
        "Please help write a function to calculate the min of two numbers", **parameters
    )
    print(f"Response from Model: {response.text}")
```


## App.py Explanation

This code is a simple example of how to use the Vertex AI APIs. It uses the ChatModel class to create a chat bot that can generate text responses to user prompts. 

The code first initializes the Vertex AI SDK and then loads a pre-trained chat model. The model is then used to start a chat session with the user. The user can then type in prompts and the chat bot will generate responses.

The code is divided into two main parts: the chat model and the user interface. The chat model is responsible for generating text responses to user prompts. The user interface is responsible for displaying the chat session to the user and allowing the user to type in prompts.

The chat model is a language model that has been trained on a large dataset of text. This allows the model to generate text that is both coherent and informative. The user interface is a simple web page that displays the chat session and allows the user to type in prompts.