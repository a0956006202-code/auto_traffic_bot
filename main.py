import time
import schedule
import datetime
from publisher import publish_content
from analytics.analyzer import analyze_market
from monitor import check_health

def job():
    print(f"\n[===== 定時任務執行中: {datetime.datetime.now()} =====]")
    analyze_market()
    publish_content()
    check_health()

# 測試立即執行一次
job()

# 設定每 10 分鐘自動執行
schedule.every(10).minutes.do(job)

print("=== 零成本自動流量與變現系統 (結合大數據分析) 已啟動 24 小時常駐排程 ===")
while True:
    schedule.run_pending()
    time.sleep(1)
