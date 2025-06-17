# 1. Importar as bibliotecas necessárias
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np

# 2. Caminhos para os arquivos salvos no ingest.py
INDEX_PATH = "embeddings/index.faiss"
CHUNKS_PATH = "embeddings/chunks.pkl"

# 3. Carregar o modelo de embeddings apenas uma vez
model = SentenceTransformer('all-MiniLM-L6-v2')

# 4. Função para carregar o índice FAISS e os pedaços de texto
def load_index_and_chunks():
    # Lê o índice vetorial salvo no disco
    index = faiss.read_index(INDEX_PATH)

    # Carrega os chunks (trechos do PDF) do arquivo .pkl
    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks

# 5. Função que recebe uma pergunta e retorna os textos mais relevantes
def retrieve(question, index, chunks, top_k=3):
    # Codifica a pergunta como vetor (embedding)
    question_embedding = model.encode([question])

    # Busca os top_k vetores mais próximos no índice FAISS
    distances, indices = index.search(np.array(question_embedding), top_k)

    # Recupera os chunks de texto correspondentes aos vetores encontrados
    return [chunks[i] for i in indices[0]]
