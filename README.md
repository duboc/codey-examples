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