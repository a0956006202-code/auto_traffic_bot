import datetime
import os

def update_monetization_report():
    report_path = "monetization_status.md"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 計算目前的內容產出總數
    content_dir = "content"
    content_count = len(os.listdir(content_dir)) if os.path.exists(content_dir) else 0
    
    report_content = f"""# 自動化流量與變現狀態報表
- **最後更新時間**: {now}
- **金流接收帳戶**: 中華郵政 (700) - 高雄籬仔內郵局 (0041398)
- **帳號**: 0902544
- **戶名**: 蕭*凡又
- **目前累積內容產出數**: {content_count} 篇
- **系統運作狀態**: 正常運行中 (Termux Background Crontab Active)
- **變現管道狀態**: 準備就緒，等待高流量導流轉換
"""
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print(f"[+] 收益追蹤報表已更新：{report_path}")

if __name__ == "__main__":
    update_monetization_report()
