import google.generativeai as genai
import os
import gradio

GOOGLE_API_KEY = os.environ["GEMINI_API_KEY"]
initial_prompt = "Você é um consultor de desenvolvimento de projetos."

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=initial_prompt)

chat = model.start_chat()

def gradio_wrapper(message, _history):
    response = chat.send_message(message)
    return response.text


chatInteface = gradio.ChatInterface(gradio_wrapper)
chatInteface.launch()
