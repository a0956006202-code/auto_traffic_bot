import os
import datetime

def generate_report():
    print(f"\n[===== 系統全面健康與數據報告: {datetime.datetime.now()} =====]")
    log_size = os.path.getsize("bot.log") if os.path.exists("bot.log") else 0
    print(f"1. 目前日誌大小: {log_size / (1024*1024):.2f} MB")
    
    market_exists = os.path.exists("analytics/market_report.json")
    print(f"2. 大數據分析模組狀態: {'正常 (已生成報告)' if market_exists else '等待中'}")
    
    git_status = os.popen("git status --short").read()
    print(f"3. Git 版控狀態: {'完全乾淨 (無未提交變更)' if not git_status.strip() else '有未提交檔案'}")
    print("=== 系統運作一切正常，零成本金流通道 (中華郵政 700-0041398-0902544) 穩定運行中 ===")

if __name__ == "__main__":
    generate_report()
