from models.intent_classifier import classify_intent
from models.entity_extractor import extract_entities
from models.response_generator import generate_response
from models.vector_search import semantic_search

def run_pipeline(user_message: str):
    intent = classify_intent(user_message)
    entities = extract_entities(user_message)
    context = semantic_search(user_message)
    response = generate_response(user_message, intent, context)
    
    return {"intent": intent, "entities": entities, "response": response}
