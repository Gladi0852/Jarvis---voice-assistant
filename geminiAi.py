import google.generativeai as genai
from dotenv import load_dotenv
import os
from utils import speak

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def geminiAi(command):
  response = model.generate_content(command, generation_config=genai.GenerationConfig(max_output_tokens=50))
  speak(response.text)