#!/bin/bash
echo "=== 系統運行狀態檢查 ==="
echo "【背景行程檢查】"
ps aux | grep main.py | grep -v grep
echo "【日誌檔案大小與內容摘要】"
python3 monitor.py
echo "=== 最近 5 筆運行日誌 ==="
if [ -f "bot.log" ]; then
    tail -n 5 bot.log
else
    echo "目前尚無日誌檔案。"
fi
