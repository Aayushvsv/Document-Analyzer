# app/ml/rag.py

from pathlib import Path
import json
import faiss
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

# --- Configuration ---
ASSETS_PATH = Path(__file__).parent / "assets"
FAISS_INDEX_PATH = ASSETS_PATH / "faiss_index.bin"
KNOWLEDGE_BASE_PATH = ASSETS_PATH / "knowledge_base.json"

# --- Asset Loading ---
print("Loading RAG assets from local files...")

# 1. Load the FAISS index
index = faiss.read_index(str(FAISS_INDEX_PATH))

# 2. Load the knowledge base texts
with open(KNOWLEDGE_BASE_PATH, "r") as f:
    knowledge_base_texts = json.load(f)

# 3. Load the embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# 4. Load the generative model
gen_tokenizer = AutoTokenizer.from_pretrained("gpt2")
gen_tokenizer.pad_token = gen_tokenizer.eos_token
gen_model = AutoModelForCausalLM.from_pretrained("gpt2")

print("✅ RAG assets loaded successfully!")


# --- RAG Function ---
def get_rag_answer(question: str, top_k: int = 3) -> dict:
    """
    Retrieves relevant documents and generates an answer to a question.
    """
    question_embedding = embedding_model.encode([question])
    distances, indices = index.search(question_embedding, top_k)
    retrieved_docs = [knowledge_base_texts[i] for i in indices[0]]
    context = "\n\n".join(retrieved_docs)
    prompt = f"Based on the following context, please answer the question.\n\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    inputs = gen_tokenizer(prompt, return_tensors="pt")
    input_length = inputs.input_ids.shape[1]
    outputs = gen_model.generate(
        **inputs,
        max_length=input_length + 200,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        pad_token_id=gen_tokenizer.eos_token_id
    )
    generated_text = gen_tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    if "Answer:" in generated_text:
        answer = generated_text.split("Answer:")[1].strip()
    else:
        answer = generated_text.replace(prompt.replace("Answer:", ""), "").strip()

    return {"answer": answer}
