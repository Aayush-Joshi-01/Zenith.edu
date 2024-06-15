# Chatbot API with Google Generative AI

This Flask-based API utilizes Google's Generative AI to provide chatbot responses based on user prompts and conversation history. The API is configured to handle CORS and uses the Flask-RESTful extension for RESTful API design.

## Requirements

To run this application, ensure you have the following installed:

- Python 3.7+
- Flask
- Flask-RESTful
- Flask-CORS
- google-generativeai
- logging

You can install the required Python packages using pip:

```bash
pip install Flask Flask-RESTful Flask-CORS google-generativeai
```

## Configuration

The application requires a Google API key for the Generative AI service. Configure the API key in the `genai.configure` function:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

Ensure you replace `"YOUR_API_KEY_HERE"` with your actual API key.

## Running the Application

To run the application, use the following command:

```bash
python app.py
```

This will start the Flask server on `http://127.0.0.1:5000`.

## API Endpoints

### POST /chat

This endpoint accepts a JSON payload with the user prompt, video ID, and chat history, and returns a response from the chatbot along with the updated conversation history.

#### Request

```json
{
    "user_prompt": "User prompt.",
    "id": "id",
    "chat_history": ["previous conversation history"]
}
```

- `user_prompt`: The prompt or question from the user.
- `id`: The ID associated with the conversation or video.
- `chat_history`: An array of previous conversation history.

#### Response

```json
{
    "response": "The response from the chatbot...",
    "chat_history": ["updated conversation history."]
}
```

- `response`: The generated response from the chatbot.
- `chat_history`: The updated conversation history including the new prompt and response.

## Logging

The application uses Python's logging module to log information and errors. By default, it logs all information at the `INFO` level. You can configure the logging level and format as needed.

## Code Structure

- `app.py`: Main application file containing the Flask app, API endpoint, and chatbot logic.
- `ChatSession`: A class to manage chat history.

### Example of `ChatbotResource` class

```python
class ChatbotResource(Resource):
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
```

## Notes

- Make sure to handle your API key securely and avoid exposing it in public repositories.
- The `transcript` variable in the prompt generation should be defined or passed appropriately.

This README provides an overview and basic usage instructions for the Chatbot API using Google Generative AI. Customize and extend the application as needed for your use case.
