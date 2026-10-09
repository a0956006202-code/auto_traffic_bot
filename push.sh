#!/bin/bash
cd ~/auto_traffic_bot
git add .
git commit -m "auto: update traffic content factory $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main
echo "[+] 成功同步至 GitHub 遠端倉庫！"
./notify.sh
