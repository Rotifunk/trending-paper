# Trending Papers Weekly

Trending Papers Weekly는 매주 ArXiv에서 AI 관련 트렌디한 논문을 수집하고 한국어로 요약·번역하여 소개하는 웹 애플리케이션입니다.

## 프로젝트 목표
- 최신 AI 논문을 자동으로 수집하고 필터링합니다.
- 논문의 핵심 내용을 요약하고 한국어로 번역합니다.
- 웹 인터페이스를 통해 지난 주차 아카이브와 검색 기능을 제공합니다.

## 모듈 구성
| 경로 | 설명 |
| --- | --- |
| `backend/` | 데이터 수집, 번역/요약 파이프라인, API 서버를 포함한 FastAPI 기반 백엔드 |
| `frontend/` | Next.js 기반 웹 프론트엔드 코드 |
| `scripts/` | 배치 작업 및 파이프라인 실행 스크립트 |
| `docs/` | 요구 사항, 설계 문서 |
| `public/` | 정적 자산 |

## 초기 로드맵
1. 데이터 파이프라인 MVP: ArXiv에서 주간 논문 수집 및 저장
2. 번역/요약 모듈 통합 및 캐싱 전략 수립
3. API 및 관리자 대시보드 구축
4. 프론트엔드 웹 페이지 구현 및 배포 자동화

## 개발 환경
- Python 3.11
- Node.js 20
- PostgreSQL 15

## 빠른 시작
```bash
# 백엔드 개발 서버 실행
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

프론트엔드 및 인프라 구성은 추후 추가될 예정입니다.
