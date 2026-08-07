from advanced_rag_bundle.models.source import Source
from advanced_rag_bundle.schemas.chat_response import ChatResponse
from advanced_rag_bundle.services.query_rewrite_service import QueryRewriteService
from advanced_rag_bundle.services.retrieval_service import RetrievalService
from advanced_rag_bundle.services.prompt_builder_service import PromptBuilderService
from advanced_rag_bundle.services.llm_service import LLMService

class RAGService:
    def __init__(self):
        self.retrieval_service = RetrievalService()
        self.prompt_builder = PromptBuilderService()
        self.llm_service = LLMService()
        self.query_rewrite_service = QueryRewriteService()

    def ask(self, question: str):
        search_results = self.retrieval_service.retrieve(question)
        prompt = self.prompt_builder.build(
            question=question,
            search_results=search_results
        )
        answer = self.llm_service.chat(
            prompt=prompt,
            new_chat=True
        )
        sources = []
        for result in search_results:
            sources.append(
                Source(
                    document_name=result.document_name,
                    score=result.score
                )
            )
        return ChatResponse(answer=answer, 
                            sources=sources)