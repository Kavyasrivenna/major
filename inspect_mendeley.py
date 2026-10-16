import urllib.request
import re

url = "https://data.mendeley.com/datasets/t256x42ms8/1"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode("utf-8")

# Let's find script with window.__INITIAL_STATE__ or json
for m in re.finditer(r'<script[^>]*>(.*?)</script>', html, re.DOTALL):
    s = m.group(1)
    if 'MedLeaf' in s:
        print("Length of MedLeaf script:", len(s))
        # Print first 2000 chars
        print(s[:2000])
        break
