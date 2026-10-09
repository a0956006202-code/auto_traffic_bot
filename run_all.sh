#!/bin/bash
cd ~/auto_traffic_bot

echo "=========================================="
echo "    AUTO TRAFFIC BOT - 執行完整工作流程    "
echo "=========================================="

echo "[1/4] 開始生成內容..."
python3 generator.py

echo "[2/4] 執行 Git 自動同步..."
./push.sh

echo "[3/4] 發送雲端 Webhook 通知..."
./notify.sh

echo "[4/4] 執行系統健康診斷..."
./status.sh

echo "=========================================="
echo "[+] 本次自動化流程全數執行完畢！"
echo "=========================================="
