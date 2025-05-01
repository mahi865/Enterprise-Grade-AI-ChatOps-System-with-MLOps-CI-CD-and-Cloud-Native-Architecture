from app.services.intent_classifier import classify_intent

def test_classify_intent_happy_path():
    result = classify_intent("I feel great today!")
    assert isinstance(result, str)
    assert result in ["joy", "happy", "surprise", "love", "anger", "sadness", "fear"]

def test_classify_intent_handles_error_gracefully():
    result = classify_intent(None)
    assert result == "unknown"
