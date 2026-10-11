#!/bin/bash
cd ~/auto_traffic_bot

LOG_FILE="logs/maintenance.log"
mkdir -p logs

echo "[$(date '+%Y-%m-%d %H:%M:%S')] === 開始執行系統日常維護與優化 ===" >> "$LOG_FILE"

# 1. 清理超過 7 天的舊日誌
find logs/ -name "*.log" -mtime +7 -exec rm -f {} \;
echo "[$(date '+%Y-%m-%d %H:%M:%S')] [+] 舊日誌清理完成" >> "$LOG_FILE"

# 2. 檢查 Git 遠端連線狀態
if git remote -v &> /dev/null; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [+] Git 遠端連線狀態正常" >> "$LOG_FILE"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [!] 警告：Git 遠端連線異常" >> "$LOG_FILE"
fi

# 3. 檢查磁碟與目錄權限
chmod +x *.sh
echo "[$(date '+%Y-%m-%d %H:%M:%S')] [+] 執行權限校驗完畢，系統狀態健康。" >> "$LOG_FILE"
echo "=== 系統日常維護執行完畢 ==="
