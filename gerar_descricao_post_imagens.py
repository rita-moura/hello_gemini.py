import google.generativeai as genai
import os

GOOGLE_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

vacation_image = genai.upload_file(
   path="social_media_festa.png"
)

prompt = (
   "Pode gerar uma descrição dessa imagem para o Instagram? Quero algo para escrever no post e uma descrição da imagem para fins de acessibilidade."
)
response = model.generate_content([vacation_image, prompt])

print(response.text)
