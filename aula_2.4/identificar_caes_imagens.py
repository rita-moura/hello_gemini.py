import google.generativeai as genai
import os

GOOGLE_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

dog_image = genai.upload_file(
   # path="aula_2.4/imagens/cachorro_collie_acho.png"
   path="aula_2.4/imagens/cachorro_golden_retriever.png"
)


prompt = (
   "Pode identificar a raça do cachorro da foto e me dar duas ou três frases de informações a respeito dele? "
   "De preferência, alguma curiosidade interessante em português, citando a fonte da informação e sempre de um jeito leve e interessante."
)
response = model.generate_content([dog_image, prompt])

print(response.text)
