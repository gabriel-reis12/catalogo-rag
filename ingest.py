import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle

EXCEL_PATH = "data/Catalogo.xlsx"

# 1. Extrair DataFrame a partir do Excel
def extrair_dataframe_do_excel(caminho_excel):
    df = pd.read_excel(caminho_excel)
    df.columns = [col.upper().strip().replace(" ", "_") for col in df.columns]
    return df.fillna("")

# 2. Criar frases descritivas baseadas nas colunas
def criar_chunks_a_partir_do_df(df):
    chunks = []
    for _, linha in df.iterrows():
        codigo = str(linha.get("CODIGO", "")).strip()

        if not codigo.upper().startswith("P"):
            continue

        montadora = str(linha.get("MONTADORA", "")).strip()
        motor = str(linha.get("MOTOR", "")).strip()
        veiculo = str(linha.get("VEICULO", "")).strip().replace("\n", " ").replace("\r", " ")
        ano = str(linha.get("ANO_DE_APLICACAO", "")).strip()

        # Tentativa de conversão do diâmetro para float
        diametro_raw = str(linha.get("DIAMETRO_DO_CILINDRO", "")).strip().replace(",", ".")
        try:
            diametro_valor = float(diametro_raw)
            diametro_str = f"{diametro_valor:.2f} mm"
        except ValueError:
            diametro_str = "não informado"

        frase = (
            f"O código {codigo} é da montadora {montadora}. "
            f"Diâmetro do cilindro: {diametro_str}. "
            f"Motor: {motor}. "
            f"Veículo(s): {veiculo}. "
            f"Ano de aplicação: {ano}."
        )

        chunks.append(frase)

    return chunks

# 3. Criar os embeddings e salvar com FAISS
def criar_e_salvar_vector_store(chunks):
    if not chunks:
        print("⚠️ Nenhum chunk gerado. Verifique o conteúdo do Excel.")
        return

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs("embeddings", exist_ok=True)

    faiss.write_index(index, "embeddings/index.faiss")
    with open("embeddings/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

# 4. Execução principal
if __name__ == "__main__":
    print("📊 Lendo o Excel e convertendo em DataFrame...")
    df = extrair_dataframe_do_excel(EXCEL_PATH)
    print("✅ DataFrame carregado com sucesso.")

    print("✍️ Gerando frases descritivas para os embeddings...")
    chunks = criar_chunks_a_partir_do_df(df)
    print(f"✅ {len(chunks)} chunks gerados.")

    print("💾 Criando e salvando os embeddings...")
    criar_e_salvar_vector_store(chunks)

    print("🏁 Tudo pronto! Embeddings atualizados com sucesso.")