import os
import requests
import glob

WEBHOOK_URL = "https://hook.eu1.make.com/你的gateway-webhook實際網址"

def publish_latest_video():
    list_of_files = glob.glob(os.path.expanduser('~/auto_traffic_bot/output/*.mp4'))
    if not list_of_files:
        print("[-] 未找到可發布的影片檔案")
        return
    
    latest_file = max(list_of_files, key=os.path.getctime)
    file_name = os.path.basename(latest_file)
    print(f"[*] 準備對接雲端發布最新短影音: {file_name}")
    
    # 發送通知與檔案資訊至 Make.com / n8n 自動化流程
    payload = {
        "event": "video_ready",
        "file_name": file_name,
        "download_url": f"http://localhost:8080/{file_name}",
        "account": "中華郵政 700-0902544"
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        print(f"[+] 雲端 Webhook 派送狀態: {response.status_code}")
    except Exception as e:
        print(f"[!] 目前未填入真實 Webhook，模擬發布完成 (路徑已就緒)")

if __name__ == '__main__':
    publish_latest_video()
