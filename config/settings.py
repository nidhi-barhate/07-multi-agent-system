import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    OLLAMA_BASE_URL=os.getenv("OLLAMA_BASE_URL")
    OLLAMA_MODEL=os.getenv("OLLAMA_MODEL")
    OLLAMA_TIMEOUT=int(os.getenv("OLLAMA_TIMEOUT", 300))