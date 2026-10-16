import urllib.request

for ds_id in ["nnytj2v3n5-1", "t256x42ms8-1"]:
    url = f"https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/{ds_id}.zip"
    print(f"Testing URL: {url}")
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=10) as r:
            size_mb = int(r.headers.get("Content-Length", 0)) / (1024 * 1024)
            print(f"  SUCCESS! Status: {r.getcode()}, Size: {size_mb:.2f} MB, Content-Type: {r.headers.get('Content-Type')}")
    except Exception as e:
        print(f"  HEAD failed: {e}. Trying GET first 1KB...")
        try:
            req2 = urllib.request.Request(url, headers={"Range": "bytes=0-1024"})
            with urllib.request.urlopen(req2, timeout=10) as r2:
                print(f"  GET Range SUCCESS! Status: {r2.getcode()}, Content-Length: {r2.headers.get('Content-Length')}")
        except Exception as e2:
            print(f"  GET Range failed: {e2}")
