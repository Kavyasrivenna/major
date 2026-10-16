import urllib.request
import json

datasets_to_check = [
    "sydney31/Indian_Medicinal_Plants_and_Leaf_Dataset_Large",
    "purabp1249/med_leaves",
    "mikehemberger/indian-medicinal-plants"
]

for ds in datasets_to_check:
    url = f"https://huggingface.co/api/datasets/{ds}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            info = json.loads(r.read().decode("utf-8"))
            print(f"=== {ds} ===")
            print("Description:", info.get("description", "")[:200])
            siblings = info.get("siblings", [])
            print(f"Files count: {len(siblings)}")
            for f in siblings[:12]:
                print(f"  - {f.get('rfilename')}")
    except Exception as e:
        print(f"Error {ds}: {e}")
