import google.generativeai as genai
import os

GOOGLE_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

food_plate = genai.upload_file(
   path="prato_de_comida.png"
)

prompt = "Pode identificar com cuidado o que é servido nesse prato e estimar grosseiramente as suas calorias?"
response = model.generate_content([food_plate, prompt])

print(response.text)
