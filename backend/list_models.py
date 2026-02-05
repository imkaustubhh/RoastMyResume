import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

print("Available Gemini models:")
print("-" * 50)
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Name: {model.name}")
        print(f"Display name: {model.display_name}")
        print(f"Description: {model.description}")
        print("-" * 50)
