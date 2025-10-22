from datetime import date
from typing import List

from pydantic import BaseModel, Field


class Paper(BaseModel):
    """논문 정보를 표현하는 기본 스키마."""

    arxiv_id: str = Field(description="ArXiv 고유 식별자")
    title: str = Field(description="논문 제목")
    summary: str = Field(description="원문 요약")
    translated_summary: str = Field(description="한국어 번역 요약")
    categories: List[str] = Field(default_factory=list, description="ArXiv 카테고리 목록")
    published: date = Field(description="논문 게재일")
    weekly_rank: int = Field(description="주간 랭킹")


class PaperListResponse(BaseModel):
    """트렌딩 논문 리스트 응답."""

    total: int
    items: List[Paper]
