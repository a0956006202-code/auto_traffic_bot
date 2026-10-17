import requests
import json

# 你的自動化平台 Webhook 接收網址（請將下方網址替換為你在 Make.com / n8n 建立的 Webhook 網址）
WEBHOOK_URL = "https://hook.eu1.make.com/a61lpbhlr1shguvzjw4eqjny9hfw8mnx"

# 模擬 AI 生成的熱搜爆款文章內容（後續可串接 Gemini API 動態生成）
article_title = "【全網熱搜】2026最新熱門影視與遊戲情報解析"
article_content = """
<h2>今日熱搜焦點</h2>
<p>這是一篇由 Termux 自動化管道透過 Webhook 觸發並成功發布到 Blogger 的測試文章。</p>
<p>本系統將 24 小時持續監控熱門話題、自動排版並發布至你的賺錢部落格！</p>
<p><b>自動化引擎運行中...</b></p>
"""

payload = {
    "title": article_title,
    "content": article_content
}

print("🚀 正在透過自動化管道發送文章資料...")
response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 200:
    print("\n🎉 成功觸發自動化發布！")
    print("📌 伺服器回應：", response.text)
else:
    print("\n❌ 觸發失敗，請檢查 Webhook 網址：", response.text)
