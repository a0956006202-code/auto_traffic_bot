#!/bin/bash
cd ~/auto_traffic_bot

echo "=========================================="
echo "      AUTO TRAFFIC BOT - 系統狀態總覽      "
echo "=========================================="
echo "1. Git 遠端同步狀態："
git remote -v
echo ""
echo "2. 最近一次 Git 提交紀錄："
git log -1 --oneline
echo ""
echo "3. 目前背景排程 (Crontab) 清單："
crontab -l
echo ""
echo "4. 系統日誌目錄檔案大小："
du -sh logs/ 2>/dev/null || echo "尚無日誌目錄"
echo ""
echo "5. 檔案完整性檢查："
ls -la
echo "=========================================="
echo "[+] 系統狀態檢查完畢！"
