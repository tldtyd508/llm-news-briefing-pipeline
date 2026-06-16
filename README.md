# LLM News Briefing Pipeline

뉴스 JSON 데이터를 단계별로 처리해 데일리 브리핑 결과물을 생성하는 Python 파이프라인 데모입니다. 실제 LLM API 키 없이 mock client로 동작합니다.

## Portfolio Summary

외부 수집 뉴스 JSON을 단계별로 처리해 데일리 브리핑 결과물을 생성하는 Python 자동화 파이프라인 예시입니다. 실제 프로젝트에서는 Claude/OpenAI API, GitHub Pages 게시, 음성 생성 기능으로 확장할 수 있습니다.

- 업무 범위: Python 자동화, JSON 파이프라인, LLM API 연동 구조 설계
- 적용 분야: Gen AI 서비스, 업무자동화/RPA, 콘텐츠 자동 생성
- 포트폴리오 상세: [PORTFOLIO.md](./PORTFOLIO.md)

## 주요 기능

- 뉴스 사전 필터링
- 중복 제거 및 우선순위 선별
- 요약/시사점 생성 mock
- HTML 브리핑 생성
- 체크포인트 저장

## 실행 방법

```bash
python3 src/pipeline.py
```

결과는 `output/briefing.html`에 생성됩니다.
