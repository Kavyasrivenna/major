import urllib.request
import json

queries = ['medicinal', 'leaf', 'leaves', 'indian-medicinal']
for q in queries:
    url = f"https://huggingface.co/api/datasets?search={q}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            items = json.loads(r.read().decode("utf-8"))
            print(f"HuggingFace search '{q}': {len(items)} datasets found")
            for it in items[:8]:
                print(f"  - {it.get('id')} (downloads: {it.get('downloads', 0)})")
    except Exception as e:
        print(f"HF Error {q}: {e}")
