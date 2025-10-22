from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/check")
def health_check() -> dict[str, str]:
    """애플리케이션 상태를 확인하는 간단한 헬스체크."""
    return {"status": "ok"}
