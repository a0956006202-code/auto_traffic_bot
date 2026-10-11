import os
import time
import subprocess
import datetime

def job():
    print(f"[*] 執行自動化排程任務：{datetime.datetime.now()}")
    # 呼叫影片生成
    subprocess.run(['python3', 'video_generator.py'])
    
    # 自動 Git 同步
    subprocess.run(['git', 'add', 'output/'])
    subprocess.run(['git', 'commit', '-m', f'Auto-generated video {datetime.datetime.now()}'])
    subprocess.run(['git', 'push'])
    print("[+] 自動化批次任務完成！")

if __name__ == '__main__':
    # 示範每隔 1 小時自動循環執行一次（實戰中可調整間隔）
    print("[+] 帝國自動化排程引擎已啟動...")
    while True:
        job()
        time.sleep(3600)  # 3600秒 = 1小時
