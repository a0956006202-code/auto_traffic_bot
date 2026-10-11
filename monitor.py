import os
import time

LOG_PATH = "bot.log"

def check_health():
    if os.path.exists(LOG_PATH):
        size_mb = os.path.getsize(LOG_PATH) / (1024 * 1024)
        print(f"目前日誌大小: {size_mb:.2f} MB")
        # 如果日誌超過 10MB 自動進行輪替備份，避免佔滿容量
        if size_mb > 10:
            os.rename(LOG_PATH, LOG_PATH + ".bak")
            print("日誌檔案過大，已自動完成備份輪替。")
    else:
        print("警告：找不到對應的日誌檔案！")

if __name__ == "__main__":
    check_health()
