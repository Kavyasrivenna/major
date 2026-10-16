import urllib.request
import json

# Check med.zip
url_med_zip = "https://huggingface.co/datasets/sydney31/Indian_Medicinal_Plants_and_Leaf_Dataset_Large/resolve/main/med.zip"
req = urllib.request.Request(url_med_zip, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        size_mb = int(r.headers.get("Content-Length", 0)) / (1024 * 1024)
        print(f"med.zip size: {size_mb:.2f} MB, Status: {r.getcode()}")
except Exception as e:
    print(f"med.zip check error: {e}")

# Check mikehemberger/indian-medicinal-plants parquet
url_p = "https://huggingface.co/datasets/mikehemberger/indian-medicinal-plants/resolve/main/data/train-00000-of-00001-8ae6149dbfccbff8.parquet"
req_p = urllib.request.Request(url_p, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req_p, timeout=10) as r:
        size_mb = int(r.headers.get("Content-Length", 0)) / (1024 * 1024)
        print(f"indian-medicinal-plants parquet size: {size_mb:.2f} MB, Status: {r.getcode()}")
except Exception as e:
    print(f"parquet check error: {e}")
