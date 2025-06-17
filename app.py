# 1. importar o Gradio para criar a interface
import gradio as gr

# 2. Importar as funções do módulo retriever
from retriever import load_index_and_chunks, retrieve

# 3. Carrega o índice FAISS e os chunks ao iniciar o app
index, chunks = load_index_and_chunks()

# 4. Função principal que será usada na interface
def anwser_question(question):
    # usa a função retrieve para obter os trechos relevantes
    results = retrieve(question, index, chunks)

    #junta os resultados em um único texto com separador
    return "\n\n---\n\n".join(results)

# 5. Define a interface do Gradio
iface = gr.Interface(
    fn=anwser_question, # Função chamada ao enviar a pergunta
    inputs=gr.Textbox(label="Pergunte sobre o catálogo"),
    outputs=gr.Textbox(label="Reposta"),
    title ="Catálogo Técnico RAG"
)

# 6. Inicia a interface

if __name__ == "__main__":
    iface.launch()

