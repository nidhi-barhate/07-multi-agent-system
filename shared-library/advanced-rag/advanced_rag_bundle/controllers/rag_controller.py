from fastapi import APIRouter

from advanced_rag_bundle.services.knowledge_service import KnowledgeService
from advanced_rag_bundle.config.repository_config import knowledge_repository
from advanced_rag_bundle.schemas.search_request import SearchRequest
from advanced_rag_bundle.services.retrieval_service import RetrievalService
from advanced_rag_bundle.services.rag_service import RAGService

router = APIRouter()


@router.post("/api/knowledge/load")
def load_knowledge():
    knowledge_service = KnowledgeService()
    total_chunks = knowledge_service.load_knowledge_base("knowledge")
    return {
        "message": "Knowledge base loaded successfully.",
        "total_chunks": total_chunks
    }

@router.get("/api/knowledge/chunks")
def get_chunks():
    return knowledge_repository.find_all()

@router.post("/api/knowledge/search")
def search(request: SearchRequest):
    retrieval_service = RetrievalService()
    return retrieval_service.retrieve(request.question)

@router.post("/api/rag/ask")
def ask(request: SearchRequest):
    rag_service = RAGService()
    return rag_service.ask(
        request.question
    )