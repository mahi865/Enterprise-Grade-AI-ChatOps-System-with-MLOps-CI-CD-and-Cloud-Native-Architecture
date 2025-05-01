from transformers import pipeline

# Pre-trained transformer for intent/emotion classification
classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", return_all_scores=True)

def classify_intent(user_message: str) -> str:
    try:
        predictions = classifier(user_message)
        intent = max(predictions[0], key=lambda x: x['score'])['label']
        return intent
    except Exception as e:
        print(f"[Intent Classifier] Error: {e}")
        return "unknown"
