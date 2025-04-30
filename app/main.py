from fastapi import FastAPI, HTTPException
from app.pipeline import process_message

# Initialize FastAPI app
app = FastAPI(title="Enterprise AI ChatOps", version="1.0")

@app.post("/chat")
async def chat_endpoint(user_message: str):
    """
    Endpoint to handle incoming user messages.
    """
    try:
        response = process_message(user_message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """
    Health check endpoint.
    """
    return {"message": "Welcome to the Enterprise AI ChatOps System"}