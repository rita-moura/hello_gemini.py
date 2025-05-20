import google.generativeai as genai
import os
import gradio as gr

GOOGLE_API_KEY = os.environ["GEMINI_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()

def gradio_wrapper(message, _history):
   # Extraia o texto da mensagem
   prompt = [message["text"]]
   uploaded_files = []
   # Iterar sobre cada arquivo recebido
   if message["files"]:
     for file_gradio_data in message["files"]:
       # Obter o caminho local do arquivo
       file_path = file_gradio_data["path"]
       # Fazer upload do arquivo para o Gemini
       uploaded_file_info = genai.upload_file(path=file_path)
       # Adicionar o arquivo uploadado à lista
       uploaded_files.append(uploaded_file_info)
   prompt.extend(uploaded_files)
   # Envie o prompt para o chat e obtenha a resposta
   response = chat.send_message(prompt)
   return response.text

chat_interface = gr.ChatInterface(
   fn=gradio_wrapper,
   title="Chatbot com Suporte a Arquivos 🤖",
   multimodal=True
)
chat_interface.launch()