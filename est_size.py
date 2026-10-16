import urllib.request
import urllib.parse
import json

url = "https://huggingface.co/api/datasets/sanjeevani-ds/medicinal_leaves"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=10) as r:
    info = json.loads(r.read().decode("utf-8"))
    siblings = info.get('siblings', [])

output_folder_files = [f['rfilename'] for f in siblings if f['rfilename'].startswith('Output folder/')]
print(f"Total files in Output folder: {len(output_folder_files)}")

sizes = []
for fname in output_folder_files[:10]:
    quoted = urllib.parse.quote(fname)
    f_url = f"https://huggingface.co/datasets/sanjeevani-ds/medicinal_leaves/resolve/main/{quoted}"
    f_req = urllib.request.Request(f_url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(f_req, timeout=5) as fr:
            sz = int(fr.headers.get("Content-Length", 0))
            sizes.append(sz)
    except Exception as e:
        print("err:", e)

if sizes:
    avg_size = sum(sizes) / len(sizes)
    est_total_mb = (avg_size * len(output_folder_files)) / (1024 * 1024)
    print(f"Sample avg size: {avg_size/1024:.1f} KB")
    print(f"Estimated total size for {len(output_folder_files)} images: {est_total_mb:.1f} MB")
