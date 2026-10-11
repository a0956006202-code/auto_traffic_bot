#!/bin/bash
echo "=== 啟動零成本自動流量與變現系統 ==="
pkill -f main.py
nohup python3 main.py > bot.log 2>&1 &
python3 monitor.py
echo "系統已成功在背景常駐運行！"
