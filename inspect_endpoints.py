import urllib.request
import re

url = "https://data.mendeley.com/datasets/t256x42ms8/1"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode("utf-8")

# Let's find all URLs or endpoints mentioned in the html
endpoints = set(re.findall(r'\"([^\"]*t256x42ms8[^\"]*)\"', html))
for ep in endpoints:
    print("t256x42ms8 match:", ep)

# Also check for .zip or direct files
files = set(re.findall(r'\"([^\"]*\.zip[^\"]*)\"', html, re.IGNORECASE))
print("Zip matches:", files)

# Let's search for 'distribution' in schema.org JSON-LD
dist = re.findall(r'\"distribution\":\s*(\[[^\]]+\])', html)
print("Distribution:", dist)
