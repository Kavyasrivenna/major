import urllib.request
import json
from collections import Counter

url = "https://huggingface.co/api/datasets/sanjeevani-ds/medicinal_leaves"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=10) as r:
    info = json.loads(r.read().decode("utf-8"))
    siblings = [f['rfilename'] for f in info.get('siblings', [])]
    
dirs = Counter()
for s in siblings:
    parts = s.split('/')
    if len(parts) > 1:
        dirs['/'.join(parts[:2])] += 1

print("Top directories:")
for d, count in dirs.most_common():
    print(f"  {d}: {count} files")
