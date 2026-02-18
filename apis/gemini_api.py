from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
gem_client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

response = gem_client.models.generate_content(
    model="gemini-3-flash-preview", contents="Cuéntame un chiste.",
)

print(response.text)