import os
import time
import subprocess
import datetime
import publisher

def job():
    print(f"[*] 執行自動化排程任務：{datetime.datetime.now()}")
    # 1. 呼叫影片生成
    subprocess.run(['python3', 'video_generator.py'])
    
    # 2. 呼叫雲端社群發布模組
    try:
        publisher.publish_latest_video()
    except Exception as e:
        print(f"[!] 發布模組執行例外: {e}")
    
    # 3. 自動 Git 同步
    subprocess.run(['git', 'add', 'output/'])
    subprocess.run(['git', 'commit', '-m', f'Auto-generated video {datetime.datetime.now()}'])
    subprocess.run(['git', 'push'])
    print("[+] 帝國自動化管線批次任務完整執行完畢！")

if __name__ == '__main__':
    print("[+] 整合型全自動流量帝國排程引擎已啟動...")
    while True:
        job()
        time.sleep(3600)  # 每小時循環一次
