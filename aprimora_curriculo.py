import google.generativeai as genai
import os

GOOGLE_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

with open('curriculo.txt', 'r') as file:
    curriculum = file.read()

prompt = f"Por favor, aprimore o meu currículo para deixá-lo mais assertivo e enfatizando os pontos positivos. Eis o meu currículo:\n{curriculum}"
response = model.generate_content(prompt)

print(response.text)