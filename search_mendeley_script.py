import urllib.request
import re

url = "https://static.data.mendeley.com/scripts/script-v2.0.5.min.js"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as r:
    js = r.read().decode("utf-8")

# Find occurrences of api or download or zip
print("JS length:", len(js))
endpoints = set(re.findall(r'\"([^\"]*datasets[^\"]*)\"', js))
for ep in list(endpoints)[:20]:
    print("Endpoint:", ep)

# Also search for /api/
api_calls = set(re.findall(r'\"(/api/[^\"]+)\"', js))
for ac in list(api_calls)[:20]:
    print("API call:", ac)
