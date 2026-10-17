import os
import requests

API_KEY = os.getenv("BLOGGER_API_KEY", "AIzaSyAklwMXbHnEAlcuOwmfED5M6K0OSmo5vQI")
BLOG_ID = "8936181457979764166"

# 測試文章內容
title = "【AI自動化測試】全網熱搜爆款情報站正式上線！"
content = """
<h2>歡迎來到全網熱搜爆款精選！</h2>
<p>本站將持續為您帶來最新、最熱門的影視劇透、熱門小說推薦以及流行遊戲情報。</p>
<p><i>本篇文章由 AI 管道自動建立並驗證測試。</i></p>
"""

# 注意：使用 API Key 進行發表需要適當的授權範疇或設定，如果遇到權限限制，我們將串接 OAuth 或 n8n 自動化流程
url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/?key={API_KEY}"
payload = {
    "kind": "blogger#post",
    "title": title,
    "content": content
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    post_data = response.json()
    print("\n🎉 文章發布成功！")
    print(f"🔗 文章網址: {post_data.get('url')}\n")
else:
    print("\nℹ️ 狀態回傳：", response.text)
