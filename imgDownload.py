import requests
import os

access_key = "ImJnGutQrnhFtZExcLyEKq-vj8KV_Bkt6olMI9Xdw4k"
query = "accessories"

# Create folder using query name
folder_name = query.replace("+", "_")  # folder me + na ho
os.makedirs(folder_name, exist_ok=True)

url = f"https://api.unsplash.com/search/photos?query={query}&per_page=30&client_id={access_key}"
response = requests.get(url).json()

for i, img in enumerate(response['results']):
    img_url = img['urls']['regular']
    img_data = requests.get(img_url).content
    with open(f"{folder_name}/{folder_name}_{i+1}.jpg", "wb") as f:
        f.write(img_data)
