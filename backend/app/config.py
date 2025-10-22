from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """애플리케이션 전역 설정."""

    environment: str = "development"
    arxiv_base_url: str = "https://export.arxiv.org/api/query"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


def get_settings() -> Settings:
    """싱글톤 패턴 대신 간단한 팩토리 함수를 제공."""
    return Settings()
