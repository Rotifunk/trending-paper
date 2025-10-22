from fastapi import FastAPI

from .routers import health, papers

app = FastAPI(title="Trending Papers Weekly", version="0.1.0")

app.include_router(health.router)
app.include_router(papers.router)


@app.get("/")
def read_root() -> dict[str, str]:
    """프로젝트 상태를 간단히 안내하는 루트 엔드포인트."""
    return {
        "message": "Trending Papers Weekly API",
        "docs": "/docs",
    }
