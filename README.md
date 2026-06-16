# LLM News Briefing Pipeline

뉴스 JSON 데이터를 단계별로 처리해 데일리 브리핑 결과물을 생성하는 Python 파이프라인 데모입니다. 실제 LLM API 키 없이 mock client로 동작합니다.

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

