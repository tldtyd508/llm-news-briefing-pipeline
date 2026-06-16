import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKPOINT = ROOT / "checkpoints"
OUTPUT = ROOT / "output"


def save_step(name, data):
    CHECKPOINT.mkdir(exist_ok=True)
    (CHECKPOINT / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def load_news():
    return json.loads((ROOT / "sample-data" / "news.json").read_text(encoding="utf-8"))


def prefilter(items):
    result = [item for item in items if item.get("title") and item.get("url") and item.get("published_at")]
    save_step("01_prefilter", result)
    return result


def rank(items):
    result = sorted(items, key=lambda item: item.get("score", 0), reverse=True)
    save_step("02_ranked", result)
    return result


def summarize(items):
    result = [
        {
            **item,
            "summary": f"{item['title']} 관련 핵심 동향을 요약했습니다.",
            "insight": "시장 변화와 업무 의사결정에 영향을 줄 수 있는 이슈입니다."
        }
        for item in items
    ]
    save_step("03_summarized", result)
    return result


def render_html(items):
    OUTPUT.mkdir(exist_ok=True)
    cards = "\n".join(
        f"""
        <article class="card">
          <div class="meta">score {item.get('score', 0)} · {item.get('published_at', '')}</div>
          <h2>{item['title']}</h2>
          <p>{item['summary']}</p>
          <strong>{item['insight']}</strong>
        </article>
        """
        for item in items
    )
    html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Daily Briefing</title>
  <style>
    :root {{
      color: #172033;
      background: #f5f7fb;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    body {{
      margin: 0;
      padding: 48px;
    }}
    main {{
      max-width: 980px;
      margin: 0 auto;
    }}
    .hero {{
      margin-bottom: 28px;
    }}
    .eyebrow {{
      color: #2563eb;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}
    h1 {{
      margin: 10px 0 12px;
      font-size: 44px;
      line-height: 1.12;
    }}
    .lead {{
      margin: 0;
      color: #64748b;
      font-size: 17px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
    }}
    .card {{
      min-height: 220px;
      padding: 24px;
      border: 1px solid #dbe3ef;
      border-radius: 18px;
      background: #fff;
      box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
    }}
    .meta {{
      margin-bottom: 18px;
      color: #2563eb;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
    }}
    h2 {{
      margin: 0 0 14px;
      font-size: 24px;
      line-height: 1.25;
    }}
    p {{
      color: #475569;
      line-height: 1.65;
    }}
    strong {{
      display: block;
      margin-top: 18px;
      color: #0f172a;
      line-height: 1.55;
    }}
  </style>
</head>
<body>
  <main>
    <section class="hero">
      <div class="eyebrow">LLM News Pipeline</div>
      <h1>Daily Briefing</h1>
      <p class="lead">수집 뉴스 JSON을 필터링, 정렬, 요약해 생성한 브리핑 결과물입니다.</p>
    </section>
    <section class="grid">{cards}</section>
  </main>
</body>
</html>"""
    (OUTPUT / "briefing.html").write_text(html, encoding="utf-8")


def main():
    items = load_news()
    items = prefilter(items)
    items = rank(items)
    items = summarize(items)
    render_html(items)
    print("Generated output/briefing.html")


if __name__ == "__main__":
    main()
