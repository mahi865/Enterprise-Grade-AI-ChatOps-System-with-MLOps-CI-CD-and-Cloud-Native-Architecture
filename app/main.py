from fastapi import FastAPI, Request
from integrations.external_apis import handle_external_apis
from models.intent_classifier import classify_intent
from models.response_generator import generate_response
from monitoring import log_request_metrics

app = FastAPI()

@app.post("/chat")
async def chat_handler(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    
    intent = classify_intent(user_message)
    response = generate_response(user_message, intent)

    external_data = await handle_external_apis(intent, user_message)
    log_request_metrics(user_message, intent)

    return {"intent": intent, "response": response, "external_data": external_data}

