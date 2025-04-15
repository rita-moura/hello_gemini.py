import google.generativeai as genai
import os

GOOGLE_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

students_spreadsheet = genai.upload_file(
   path="aula_2.4/arquivos/desempenho_estudantes_enem.csv",
   display_name="Notas do Enem"
)

prompt = "Pode gerar um relatório de dois ou três parágrafos baseado nesses dados? Fale de tendências nos grupos de estudantes."
response = model.generate_content([students_spreadsheet, prompt])

print(response.text)