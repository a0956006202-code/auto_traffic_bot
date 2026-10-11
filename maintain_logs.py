# ==========================================
# 零成本自動化流量與變現工廠 - 日誌與磁碟自動維護中樞
# ==========================================

import os
import glob
import datetime

def clean_old_logs():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_dir = os.path.expanduser("~/auto_traffic_bot/logs")
    
    if os.path.exists(log_dir):
        # 清理超過 7 天的舊 log 檔案
        for log_file in glob.glob(os.path.join(log_dir, "*.log")):
            file_time = datetime.datetime.fromtimestamp(os.path.getmtime(log_file))
            if (datetime.datetime.now() - file_time).days > 7:
                os.remove(log_file)
                print(f"[{now}] 已自動清理過期日誌: {log_file}")
    
    print(f"[{now}] 報告長官：磁碟與日誌維護已完成，空間保持最優化狀態！")

if __name__ == "__main__":
    clean_old_logs()
