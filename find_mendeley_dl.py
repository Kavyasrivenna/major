import urllib.request
import re

url = "https://data.mendeley.com/datasets/t256x42ms8/1"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode("utf-8")

scripts = re.findall(r'src="([^"]+\.js)"', html)
print("Scripts found:", len(scripts))
for s in scripts:
    print(" ", s)
    # fetch script and search for download endpoint
    try:
        s_url = s if s.startswith("http") else "https://data.mendeley.com" + s
        s_req = urllib.request.Request(s_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(s_req, timeout=10) as sr:
            js = sr.read().decode("utf-8")
            matches = re.findall(r'/(?:api|public-files|download|zip)/[^\s"\'`\)]+', js)
            if matches:
                print("   Found endpoints:", matches[:5])
    except Exception as e:
        print("   Err:", e)
