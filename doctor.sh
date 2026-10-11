#!/bin/bash
cd ~/auto_traffic_bot

echo "[*] 開始執行系統健康檢查 ($(date '+%Y-%m-%d %H:%M:%S'))"

# 檢查 Git 狀態，若有未追蹤的衝突或未提交檔案自動進行安全備份
git status --porcelain
if [ $? -ne 0 ]; then
    echo "[!] 警告：Git 狀態異常，正在嘗試重置..."
    git stash
    git pull origin main --rebase
    git stash pop
fi

# 確保 logs 資料夾存在並限制檔案大小（超過 1MB 自動歸檔清空，避免手機空間被日誌塞滿）
mkdir -p logs
if [ -f "logs/cron.log" ] && [ $(wc -c < "logs/cron.log") -gt 1048576 ]; then
    mv logs/cron.log logs/cron_old.log
    echo "[+] 日誌已達上限，已自動輪替歸檔。"
fi

echo "[+] 系統健康檢查完畢，運行正常！"
