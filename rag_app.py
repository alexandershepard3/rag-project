from fastapi import FastAPI
from dotenv import load_dotenv
import os
import sys

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
    return {"message": "RAG app is running"}