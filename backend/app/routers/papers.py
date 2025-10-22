from typing import Annotated

from fastapi import APIRouter, Query

from ..schemas.papers import PaperListResponse
from ..services.arxiv import fetch_trending_papers

router = APIRouter(prefix="/papers", tags=["papers"])


@router.get("/trending", response_model=PaperListResponse)
def list_trending_papers(
    limit: Annotated[int, Query(ge=1, le=50)] = 10,
) -> PaperListResponse:
    """트렌딩 논문 목록을 임시 데이터로 반환합니다."""

    papers = fetch_trending_papers(limit=limit)
    return PaperListResponse(total=len(papers), items=list(papers))
