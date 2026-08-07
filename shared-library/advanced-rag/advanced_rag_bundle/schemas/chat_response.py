from advanced_rag_bundle.models.source import Source
from pydantic import BaseModel

class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]