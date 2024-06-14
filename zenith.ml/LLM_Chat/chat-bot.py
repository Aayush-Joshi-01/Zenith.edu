"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

from text import transcript

genai.configure(api_key="AIzaSyBFgMwzCRr5ANjx70kxgKU747AC5Z-qgXs")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
    history=[  
    ]
)

if __name__ == '__main__':
    while True:
        user_prompt = input("")
        if user_prompt == 'exit':
            break

        response = chat_session.send_message(
            "<|Prompt|>Given here is a transcript of a ed tech video act as a professional "
            "in the topic discussed. User is  going to ask certain questions on the given"
            "video's transcript, the user question along with the previous history of the "
            "conversation will be provided with them being give in <|User|> and <|History|>"
            "answer me  in not more than 200 words" + transcript + "<|Prompt|>"
            "<|User|>" + user_prompt + "<|User|> and <|History|>" +
            " ".join(chat_history) + "<|History|>")

        print(response.text)
