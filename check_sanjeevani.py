import urllib.request
import json

# Check sanjeevani-ds class_indices.json
url_ci = "https://huggingface.co/datasets/sanjeevani-ds/medicinal_leaves/raw/main/Models/class_indices.json"
req = urllib.request.Request(url_ci, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        class_indices = json.loads(r.read().decode("utf-8"))
        print("sanjeevani-ds classes:", json.dumps(class_indices, indent=2))
except Exception as e:
    print("sanjeevani-ds class_indices error:", e)

# Also check file structure of sanjeevani-ds
url_tree = "https://huggingface.co/api/datasets/sanjeevani-ds/medicinal_leaves"
req2 = urllib.request.Request(url_tree, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req2, timeout=10) as r2:
        info = json.loads(r2.read().decode("utf-8"))
        siblings = [f['rfilename'] for f in info.get('siblings', [])]
        print(f"Total files in sanjeevani-ds: {len(siblings)}")
        sample_images = [f for f in siblings if f.endswith(('.jpg', '.png', '.jpeg'))]
        print(f"Total image files: {len(sample_images)}")
        print("Sample image paths:")
        for s in sample_images[:10]:
            print("  ", s)
except Exception as e:
    print("sanjeevani-ds tree error:", e)
