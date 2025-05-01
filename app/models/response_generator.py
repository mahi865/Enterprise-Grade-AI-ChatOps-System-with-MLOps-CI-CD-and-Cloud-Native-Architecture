from transformers import pipeline

# Use LLM wrapper (could be a local model or API like GPT/Claude)
generator = pipeline("text-generation", model="gpt2")

def generate_response(message: str, intent: str, context: str = "") -> str:
    prompt = f"Intent: {intent}\nUser: {message}\nContext: {context}\nBot:"
    try:
        result = generator(prompt, max_length=100, num_return_sequences=1)
        return result[0]['generated_text'].split("Bot:")[-1].strip()
    except Exception as e:
        print(f"[Response Generator] Error: {e}")
        return "Sorry, I'm having trouble responding right now."
