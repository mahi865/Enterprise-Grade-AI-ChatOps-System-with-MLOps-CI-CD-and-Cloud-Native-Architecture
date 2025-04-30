from app.models.bert_intent import classify_intent
from app.models.gpt_wrapper import generate_response
from app.integrations.jira import handle_jira_integration
from app.integrations.salesforce import handle_salesforce_integration

def process_message(user_message: str) -> str:
    """
    NLP + RAG + routing logic.
    """
    # Step 1: Intent classification
    intent = classify_intent(user_message)

    # Step 2: Handle specific intents
    if intent == "jira":
        return handle_jira_integration(user_message)
    elif intent == "salesforce":
        return handle_salesforce_integration(user_message)
    
    # Step 3: Default to GPT-4 for general queries
    return generate_response(user_message)