import os
import requests

API_KEY = os.getenv("BLOGGER_API_KEY", "AIzaSyAklwMXbHnEAlcuOwmfED5M6K0OSmo5vQI")
BLOG_URL = "http://allhotnews2026.blogspot.com/"

url = f"https://www.googleapis.com/blogger/v3/blogs/byurl?url={BLOG_URL}&key={API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    blog_data = response.json()
    print("\n✅ 成功連線到 Blogger！")
    print(f"📌 網誌名稱: {blog_data.get('name')}")
    print(f"🔑 網誌 ID (Blog ID): {blog_data.get('id')}\n")
else:
    print("\n❌ 連線失敗：", response.text)
