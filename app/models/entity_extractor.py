import spacy

# Load spaCy NER model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text: str) -> dict:
    try:
        doc = nlp(text)
        return {ent.label_: ent.text for ent in doc.ents}
    except Exception as e:
        print(f"[Entity Extractor] Error: {e}")
        return {}
