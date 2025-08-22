from flask import Flask, request
from flask_restful import Api, Resource
import os
from groq import Groq

app = Flask(__name__)
api = Api(app)

# Set your Groq API key (Store securely, use environment variables in production)
API_KEY =os.getenv('GROQ_API_KEY')  # Replace with your actual API key
if not API_KEY:
    raise ValueError("Groq API key is missing. Please set the API_KEY variable.")

# Initialize the Groq client
client = Groq(api_key=API_KEY)

class Chat(Resource):
    def post(self):
        """Chatbot endpoint to accept user messages and return LLaMA-generated responses."""
        try:
            data = request.get_json()
            user_message = data.get("message", "").strip()

            # Validate input
            if not user_message:
                return {"error": "Message cannot be empty"}, 400

            # Generate a response from LLaMA
            response = client.chat.completions.create(
                model="llama3-8b-8192",  # Using LLaMA-3 8B model
                messages=[{"role": "user", "content": user_message}]
            )

            # Extract and return the chatbot response
            chatbot_reply = response.choices[0].message.content
            return {"response": chatbot_reply}, 200

        except Exception as e:
            return {"error": "An error occurred while processing your request."}, 500

# Add resources to the API
api.add_resource(Chat, "/chat")

if __name__ == "__main__":
    app.run(debug=True)



