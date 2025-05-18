import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=api_key)

# This model name is ONLY supported in SDK version >=0.4
model = genai.GenerativeModel("models/gemini-pro")

prompt = "Return a heading, subheading and paragraph about AI in JSON."

response = model.generate_content(prompt)
print(response.text)
