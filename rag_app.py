from fastapi import FastAPI
from dotenv import load_dotenv
import os
import sys
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Read API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Fail clearly if missing
if not GEMINI_API_KEY:
    print("ERROR: GEMINI_API_KEY is missing!", file=sys.stderr)
    sys.exit(1)

# Create FastAPI app
app = FastAPI()

# Test route
@app.get("/health")
def home():
    return {"Status": "OK"}


    # --- THIS IS THE FUNCTION YOU MODIFY ---
@app.get("/test-gemini")
def test_gemini():
    try:
        # Configure Gemini
        genai.configure(api_key=GEMINI_API_KEY)

        # Create model using supported model name
        model = genai.GenerativeModel(
            "models/gemini-2.5-flash"
        )
        user_prompt = "picking a favorite color"
        outline_prompt = f"Create an outline for {user_prompt}"

        # Generate response
        outline_response = model.generate_content(
            outline_prompt
        )
        response_prompt = f"Create a 3 sentenceresponse to the following outline: {outline_response.text}"
        response = model.generate_content(
            response_prompt
        )
        # Return text
        return {
            "message": response.text
        }

    except Exception as e:
        return {
            "error": str(e)
        }