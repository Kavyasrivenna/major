import urllib.request
import pandas as pd
import io

url = "https://huggingface.co/datasets/mikehemberger/indian-medicinal-plants/resolve/main/data/train-00000-of-00001-8ae6149dbfccbff8.parquet"
print("Downloading 20MB parquet file into memory to inspect...")
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=30) as r:
    data = r.read()

print(f"Downloaded: {len(data)/(1024*1024):.2f} MB")
df = pd.read_parquet(io.BytesIO(data))
print("Dataframe shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Unique labels count:", df['label'].nunique() if 'label' in df.columns else 'No label col')
if 'label' in df.columns:
    print("Labels sample:", df['label'].value_counts()[:15].to_dict())
print("Sample row keys in image col:", type(df['image'].iloc[0]) if 'image' in df.columns else 'No image col')
