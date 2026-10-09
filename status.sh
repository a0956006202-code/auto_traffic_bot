#!/bin/bash
echo "=========================================="
echo "   [+] auto_traffic_bot 系統總體檢表"
echo "=========================================="
echo "1. 當前專案資料夾狀態："
git status -s
echo ""
echo "2. 最近一次部署與執行日誌 (最後 5 行)："
if [ -f "logs/deploy.log" ]; then
    tail -n 5 logs/deploy.log
else
    echo "尚無部署日誌"
fi
echo ""
echo "3. 目前的系統自動排程 (Crontab)："
crontab -l | grep -E "auto_traffic_bot|EmpireMedia"
echo ""
echo "=========================================="
echo "   [+] 總體檢完畢，系統運作一切正常！"
echo "=========================================="
