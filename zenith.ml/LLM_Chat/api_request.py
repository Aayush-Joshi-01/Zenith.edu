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
    history=[
    ]
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
            print(data)
            transcribes=find_course_transcribe(course_id)
            prompt = (
                f"You are an expert in the topic discussed in the following transcript. "
                f"The user will ask questions based on this transcript. Provide clear and concise answers "
                f"within 200 words.\n\n"
                f"Transcript:\n{transcribes}\n\n"
                f"User Question: {user_prompt}\n"
                f"Conversation History: {chat_history}"
            )
            print(prompt)

            response = chat_session.send_message(prompt)
            chat_history.append({"user":user_prompt,"response":response.text})
            return jsonify({
                'response': response.text,
                'chat_history': chat_history
            })

        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return {'error': 'Internal server error'}, 500

api.add_resource(ChatbotResource, '/chat')

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)