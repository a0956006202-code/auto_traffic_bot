from flask import Flask, request, abort
import requests

app = Flask(__name__)

ACCESS_TOKEN = "K0/w4ko3l4HYHJOqd6hfCTZ9PArR4XZAtHKN3jXoHn4N/86k+HYg5tXxmwpic6yENQCwTOUdR+xOdvblfi345A7WGwue36bQpyLxdNkjN0I62b6geyyZMdPTPkZyq7bOQuXtgBlZcYDHniGMyt1xgAdB04t89/1O/w1cDnyilFU="

@app.route("/callback", methods=['POST'])
def callback():
    json_data = request.json
    events = json_data.get('events', [])
    
    for event in events:
        if event['type'] == 'message' and event['message']['type'] == 'text':
            reply_token = event['replyToken']
            user_text = event['message']['text']
            
            # 判斷關鍵字自動回覆
            if "PPT" in user_text or "Gamma" in user_text:
                reply_message(reply_token, "嗨！這是為你準備的 2026 AI 爆款簡報製作工具（Gamma）專屬傳送門：\n👉 立即免費體驗：https://gamma.app?fp_ref=jacky2026")
                
    return 'OK', 200

def reply_message(reply_token, text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    body = {
        "replyToken": reply_token,
        "messages": [{"type": "text", "text": text}]
    }
    requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=body)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)


