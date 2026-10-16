import urllib.request
import json

hf_datasets = [
    "sanjeevani-ds/medicinal_leaves",
    "funkepal/medicinal_plant_images",
    "binu1515/Indian_medicinal_plant_image_dataset",
    "purabp1249/med_leaves"
]

for ds in hf_datasets:
    url = f"https://huggingface.co/api/datasets/{ds}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            info = json.loads(r.read().decode("utf-8"))
            siblings = info.get("siblings", [])
            print(f"=== {ds} (files: {len(siblings)}) ===")
            for f in siblings[:5]:
                fname = f.get('rfilename')
                f_url = f"https://huggingface.co/datasets/{ds}/resolve/main/{fname}"
                f_req = urllib.request.Request(f_url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
                try:
                    with urllib.request.urlopen(f_req, timeout=6) as fr:
                        size_mb = int(fr.headers.get("Content-Length", 0)) / (1024 * 1024)
                        print(f"   {fname}: {size_mb:.2f} MB")
                except Exception as fe:
                    print(f"   {fname}: {fe}")
    except Exception as e:
        print(f"Error {ds}: {e}")
