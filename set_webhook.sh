#!/bin/bash
if [ -z "$1" ]; then
    echo "👉 請輸入 Make.com 或 n8n 的 Webhook 網址"
    echo "用法: ./set_webhook.sh https://hook.eu1.make.com/your_token"
    exit 1
fi

sed -i "s|WEBHOOK_URL = .*|WEBHOOK_URL = \"$1\"|" publisher.py
echo "=========================================="
echo "[+] Webhook 網址已成功更新為: $1"
echo "[+] 測試發送最新影片通知中..."
python3 publisher.py
echo "=========================================="
