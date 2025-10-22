# 시스템 아키텍처 개요

## 데이터 파이프라인
1. **수집 (Collector)**: ArXiv API에서 주간 기준의 논문 메타데이터를 가져옵니다.
2. **랭킹 (Scoring)**: 조회수, 최신성, 키워드 일치도를 기반으로 점수를 계산합니다.
3. **번역/요약 (NLP Processor)**: LLM 또는 NMT 모델을 통해 요약문과 한국어 번역을 생성합니다.
4. **저장 (Persistence)**: PostgreSQL 및 객체 스토리지에 메타데이터와 생성된 콘텐츠를 저장합니다.

## 애플리케이션 계층
- **백엔드 API (FastAPI)**: 논문 데이터 제공, 관리자용 파이프라인 트리거, 인증.
- **프론트엔드 (Next.js)**: 주간 하이라이트, 검색/필터 UI, 구독 신청 폼.
- **스케줄러 (Celery + Redis)**: 주간 배치 파이프라인 관리.

## 인프라
- **CI/CD**: GitHub Actions로 테스트, 포매팅, 배포 자동화.
- **배포**: 프론트엔드(Vercel), 백엔드(Render/Fly.io), 워커(Managed container).
- **모니터링**: OpenTelemetry + Grafana, Sentry 오류 추적.
