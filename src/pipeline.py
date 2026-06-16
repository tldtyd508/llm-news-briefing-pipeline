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
        f"<article><h2>{item['title']}</h2><p>{item['summary']}</p><strong>{item['insight']}</strong></article>"
        for item in items
    )
    html = f"<!doctype html><html lang='ko'><meta charset='utf-8'><title>Daily Briefing</title><body>{cards}</body></html>"
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

