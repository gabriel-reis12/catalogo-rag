from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np

INDEX_PATH = "embeddings/index.faiss"
CHUNKS_PATH = "embeddings/chunks.pkl"

# Carrega índice e chunks
def load_vector_store():
    index = faiss.read_index(INDEX_PATH)
    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)
    return index, chunks

# Faz a pergunta e retorna resultados mais relevantes
def query_question(question, index, chunks, model, top_k=3):
    question_embedding = model.encode([question])
    distances, indices = index.search(question_embedding, top_k)
    results = [chunks[i] for i in indices[0]]
    return results

if __name__ == "__main__":
    index, chunks = load_vector_store()
    model = SentenceTransformer('all-MiniLM-L6-v2')

    print("✅ Pronto para responder perguntas!")
    while True:
        question = input("\nDigite sua pergunta (ou 'sair'): ")
        if question.lower() == "sair":
            break

        results = query_question(question, index, chunks, model)
        print("\n🔎 Resultados relevantes:\n")
        for i, r in enumerate(results, 1):
            print(f"{i}. {r.strip()}\n")