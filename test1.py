import requests

# Define the API URL
url = "http://127.0.0.1:5000/chat"  # Update the URL if the Flask server is running elsewhere

# Define the request payload
data = {
    "message": "What is deep learning?"
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response
if response.status_code == 200:
    print("Chatbot Response:", response.json().get("response"))
else:
    print("Error:", response.json())
