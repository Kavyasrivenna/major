import urllib.request
import json

for ds_id in ["t256x42ms8", "nnytj2v3n5"]:
    api_url = f"https://data.mendeley.com/api/datasets-v2/datasets/{ds_id}"
    req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode("utf-8"))
            print(f"=== {ds_id} ===")
            print("Name:", data.get("name"))
            print("Versions:", [v.get("version") for v in data.get("versions", [])])
            for v in data.get("versions", []):
                print(f"  Version {v.get('version')} files: {len(v.get('files', []))}")
                for f in v.get("files", []):
                    print(f"    - {f.get('name')} | size: {f.get('size')} | download_url: {f.get('download_url') or f.get('content_url') or f.get('downloadUrl')}")
            
            # Check zip endpoint
            zip_url = f"https://data.mendeley.com/api/datasets-v2/datasets/{ds_id}/zip"
            zreq = urllib.request.Request(zip_url, headers={"User-Agent": "Mozilla/5.0"})
            try:
                with urllib.request.urlopen(zreq, timeout=10) as zr:
                    print(f"  Zip endpoint {zip_url} -> Status: {zr.getcode()}, Content-Type: {zr.headers.get('Content-Type')}, Content-Length: {zr.headers.get('Content-Length')}")
            except Exception as ze:
                print(f"  Zip endpoint error: {ze}")
    except Exception as e:
        print(f"API Error {ds_id}: {e}")
