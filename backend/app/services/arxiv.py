"""ArXiv 데이터 수집 서비스."""

from collections.abc import Sequence
from datetime import date

from ..schemas.papers import Paper


def fetch_trending_papers(limit: int = 10) -> Sequence[Paper]:
    """ArXiv API를 호출하는 대신 임시 데이터를 반환합니다.

    이후 구현에서는 HTTP 요청, 파싱, 점수화 로직이 이 함수로 이동할 예정입니다.
    """

    return [
        Paper(
            arxiv_id="2401.00001",
            title="Example Foundation Model",
            summary="샘플 논문 요약입니다.",
            translated_summary="샘플 논문 요약 (한국어).",
            categories=["cs.AI"],
            published=date(2024, 1, 1),
            weekly_rank=1,
        )
    ][:limit]
