from advanced_rag_bundle.client.ollama_client import OllamaClient

class EmbeddingService:
    def __init__(self):
        self.client = OllamaClient()
    def generate(self, text: str) -> list[float]:
        return self.client.embedding(text)