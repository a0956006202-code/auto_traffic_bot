import time
import schedule
import os
from publisher import generate_and_publish

print("=== 零成本自動流量與變現系統啟動 ===")
print("金流對接確認：中華郵政(700) 籬仔內郵局 | 帳號：0902544 | 戶名：蕭*凡又")

def job():
    print("正在執行自動化流量與發布任務...")
    generate_and_publish()

# 設定每 10 分鐘執行一次
schedule.every(10).minutes.do(job)

if __name__ == "__main__":
    print("排程系統已就緒，開始背景監控...")
    while True:
        schedule.run_pending()
        time.sleep(1)
