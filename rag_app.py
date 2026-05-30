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

        # Generate response
        response = model.generate_content(
            "Give me a number between 1 and 10"
        )

        # Return text
        return {
            "message": response.text
        }

    except Exception as e:
        return {
            "error": str(e)
        }