import urllib.request
import re
import json

def parse_mendeley(dataset_id):
    url = f"https://data.mendeley.com/datasets/{dataset_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            html = r.read().decode("utf-8")
            print(f"=== {dataset_id} ===")
            
            # Find script tags containing dataset details or files
            scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
            for s in scripts:
                if 'downloadUrl' in s or 'directDownloadUrl' in s or 'files' in s:
                    print("Found candidate script with len:", len(s))
                    for m in re.finditer(r'\"(?:directDownloadUrl|downloadUrl|url)\":\s*\"([^\"]+)\"', s):
                        print("  Download link:", m.group(1))
                    for m in re.finditer(r'\"fileName\":\s*\"([^\"]+)\"', s):
                        print("  File name:", m.group(1))
                    for m in re.finditer(r'\"size\":\s*(\d+)', s):
                        print("  Size:", m.group(1))

            # Also check any a tags
            for m in re.finditer(r'href="([^"]*(?:zip|tar|download|direct)[^"]*)"', html, re.IGNORECASE):
                print("  href match:", m.group(1))
    except Exception as e:
        print(f"Error {dataset_id}: {e}")

if __name__ == "__main__":
    parse_mendeley("t256x42ms8/1")
    parse_mendeley("nnytj2v3n5/1")
