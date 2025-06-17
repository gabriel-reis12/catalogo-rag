# 📘 Projeto de RAG para Catálogo Técnico

Este é um projeto de **RAG (Retrieval-Augmented Generation)** para busca inteligente em um catálogo técnico de pistões automotivos. Utiliza Python, pandas, FAISS, SentenceTransformers e uma interface simples com Gradio.

---

## 🗂 Estrutura do Projeto

```
📁 catalogo-rag/
├── data/                  # Contém o arquivo Excel com os dados
│   └── Catalogo.xlsx
├── embeddings/            # Armazena o índice FAISS e os chunks salvos
│   ├── index.faiss
│   └── chunks.pkl
├── ingest.py              # Processa o Excel, gera descrições e embeddings
├── query.py               # Consulta o índice usando uma pergunta
├── retriever.py           # Lógica de carregamento e busca FAISS
├── app.py                 # Interface em Gradio
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

---

## ⚙️ Funcionalidades

- 📥 Lê um catálogo técnico em formato Excel (`data/Catalogo.xlsx`)
- 🧠 Gera descrições automáticas de cada item usando pandas
- 🔎 Cria embeddings com `sentence-transformers`
- 📦 Indexa com `FAISS` para busca semântica eficiente
- 🧪 Interface de consulta via terminal (`query.py`)
- 🌐 Interface web simples com Gradio (`app.py`)

---

## 🚀 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/catalogo-rag.git
cd catalogo-rag
```

### 2. Crie o ambiente virtual (opcional, mas recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Gere os embeddings

```bash
python ingest.py
```

### 5. Rode a interface Gradio

```bash
python app.py
```

---

## 💬 Exemplo de uso

Digite perguntas como:

- `Quais pistões da GM possuem diâmetro maior que 70?`
- `Qual o código do pistão para o veículo Gol?`
- `Motor EA111 flex com 4 pistões, qual o código?`

---

## 📦 Requisitos

As principais bibliotecas usadas:

- `pandas`
- `sentence-transformers`
- `faiss-cpu`
- `gradio`
- `openpyxl`

Veja todas no arquivo `requirements.txt`.

---

## 🤝 Contribuição

Sinta-se livre para abrir uma **issue** ou **pull request** se quiser sugerir melhorias ou correções!

---

## 🛡️ Licença

Este projeto está licenciado sob a **MIT License**.
As pastas "Data" e "Embeddings" contém conteúdos que não podem ser disponibilizados.
