import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from integrations.external_apis import handle_external_apis
from models.intent_classifier import classify_intent
from models.response_generator import generate_response
from monitoring import log_request_metrics

# Load environment variables from .env file
load_dotenv()

# Access environment variables (optional: print for debugging)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
ENV = os.getenv("ENV")

SENTRY_DSN = os.getenv("SENTRY_DSN")
SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")
CLOUD_API_KEY = os.getenv("CLOUD_API_KEY")

print(f"Environment: {ENV}")

# Initialize FastAPI app
app = FastAPI()

# Define the chat endpoint
@app.post("/chat")
async def chat_handler(request: Request):
    # Parse user message from the request
    data = await request.json()
    user_message = data.get("message", "")

    # Classify the user's intent
    intent = classify_intent(user_message)

    # Generate a response based on the intent and user message
    response = generate_response(user_message, intent)

    # Handle external API calls based on the intent
    external_data = await handle_external_apis(intent, user_message)

    # Log the request and intent for monitoring
    log_request_metrics(user_message, intent)

    # Return the response, intent, and any external data
    return {"intent": intent, "response": response, "external_data": external_data}

# Entry point for running the application (if needed for local development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)