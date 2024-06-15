from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import google.generativeai as genai
import os
import logging
import io

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

generative_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
chat_session = ChatSession()

class ChatbotResource(Resource):
    """
    request
    POST /chat
    Content-Type: application/json

    {
        "user_prompt": "User prompt.",
        "video_id": "id",
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
            id = data.get('id', '')
            chat_history = data.get('chat_history', [])

            chat_session.chat_history = chat_history

            prompt = (
                f"You are an expert in the topic discussed in the following transcript. "
                f"The user will ask questions based on this transcript. Provide clear and concise answers "
                f"within 200 words.\n\n"
                f"Transcript:\n{transcript}\n\n"
                f"User Question: {user_prompt}\n"
                f"Conversation History: {' '.join(chat_history)}"
            )

            response = generative_model.generate(prompt=prompt)

            response_text = response.choices[0].text.strip()

            chat_session.update_history(user_prompt, response_text)

            return jsonify({
                'response': response_text,
                'chat_history': chat_session.chat_history
            })

        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return {'error': 'Internal server error'}, 500

api.add_resource(ChatbotResource, '/chat')
