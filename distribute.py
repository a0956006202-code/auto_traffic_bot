import urllib.request
import json
import os

# 使用專案配置的 Make.com Webhook 連結
WEBHOOK_URL = "https://hook.eu1.make.com/rmtwfknkrxm4mkdwbs3xw7ucnghpig4f"

def get_latest_content():
    content_dir = "content"
    if not os.path.exists(content_dir):
        return None
    files = sorted([os.path.join(content_dir, f) for f in os.listdir(content_dir) if f.endswith(".txt")])
    if not files:
        return None
    latest_file = files[-1]
    with open(latest_file, "r", encoding="utf-8") as f:
        return f.read()

def trigger_distribution():
    content = get_latest_content()
    if not content:
        print("[-] 找不到可分發的內容檔案。")
        return

    payload = {
        "source": "Termux Auto Traffic Bot",
        "destination": "中華郵政變現通道",
        "content_body": content
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = response.read().decode("utf-8")
            print(f"[+] 內容已成功透過 Webhook 分發！伺服器回應: {result}")
    except Exception as e:
        print(f"[-] Webhook 分發失敗: {e}")

if __name__ == "__main__":
    trigger_distribution()
