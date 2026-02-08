import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

print(f"Checking models for API Key ending in ...{GEMINI_API_KEY[-4:] if GEMINI_API_KEY else 'None'}")

try:
    print("Listing available models...")
    found_any = False
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- Found supported model: {m.name}")
            found_any = True
            
    if not found_any:
        print("❌ No 'generateContent' models found. Your API Key might be invalid or has no access to Generative Language API.")
except Exception as e:
    print(f"❌ Error listing models: {e}")
