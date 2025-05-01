from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model and FAISS index
embedder = SentenceTransformer('all-MiniLM-L6-v2')
# This assumes you have already loaded/created a FAISS index
index = faiss.read_index("vector_store/index.faiss")
# Load document mappings (e.g., index -> text)
with open("vector_store/id_to_text.json", "r") as f:
    import json
    id_to_text = json.load(f)

def semantic_search(query: str, top_k: int = 3) -> str:
    try:
        query_vec = embedder.encode([query])
        D, I = index.search(np.array(query_vec).astype("float32"), top_k)
        results = [id_to_text[str(idx)] for idx in I[0] if str(idx) in id_to_text]
        return "\n".join(results)
    except Exception as e:
        print(f"[Vector Search] Error: {e}")
        return ""
