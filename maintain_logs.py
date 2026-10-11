import os

def clean_logs():
    log_file = "bot.log"
    if os.path.exists(log_file):
        size_mb = os.path.getsize(log_file) / (1024 * 1024)
        if size_mb > 10:  # 如果日誌大於 10MB 則自動備份並清空
            os.rename(log_file, "bot_old.log")
            print(f"[系統維護] 日誌超過 {size_mb:.2f}MB，已自動執行輪替清理。")
        else:
            print(f"[系統維護] 日誌大小正常 ({size_mb:.2f}MB)，無需清理。")
    else:
        print("[系統維護] 尚無日誌檔。")

if __name__ == "__main__":
    clean_logs()
