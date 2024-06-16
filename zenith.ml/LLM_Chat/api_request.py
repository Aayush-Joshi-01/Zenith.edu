from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import google.generativeai as genai
import os
import logging
import io

from mongo_connection import find_course_transcribe

app = Flask(__name__)
api = Api(app)
CORS(app)

genai.configure(api_key="AIzaSyBFgMwzCRr5ANjx70kxgKU747AC5Z-qgXs")

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
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
chat_session = model.start_chat(
    # history=[
    # ]
)

class ChatbotResource(Resource):
    """
    request
    POST /chat
    Content-Type: application/json

    {
        "user_prompt": "User prompt.",
        "id": "id",
        "chat_history": ["previous conversation history"]
    }

    response
    {
    "response": "The response from the chatbot...",
    "chat_history": ["updated conversation history."]
    }

    """
    def post(self):
        try:
            data = request.get_json()

            user_prompt = data.get('user_prompt', '')
            course_id = data.get('id')
            chat_history = data.get('chat_history', [])
            # print(data)
            if chat_history:
                for element in chat_history:
                    if not isinstance(element,dict):
                        chat_history.remove(element)
            transcribes=find_course_transcribe(course_id)
            prompt = (
                f"Your name is Zenai"
                f"Act as if you are an expert in the topic whoes video transcript We will be giving you the user will ask variety of questions that will be mentioned below along with transcript and history(that will include user question and your previous response) if a person's respose mentions the use of the last recent respose check the most recent response that you gave and give next response accordingly"
                f"The user will ask questions based on this transcript. Provide clear and concise answers in the text format do not give the md format and try to put it in point basis"
                f"within 100 words.\n\n"
                f"Transcript:\n{transcribes}\n\n"
                f"User Question: {user_prompt}\n"
                f"Conversation History: {chat_history}"
            )
            # print(chat_history)
            # print("---------------------")
            response = chat_session.send_message(prompt)
            chat_history.append({"user":user_prompt,"response":response.text})
            # print(chat_history)
            return jsonify({
                'response': response.text.replace('*', '').replace('\n', ''),
                'chat_history': chat_history
            })

        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return {'error': 'Internal server error'}, 500

api.add_resource(ChatbotResource, '/chat')

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)