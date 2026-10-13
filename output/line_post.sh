#!/data/data/com.termux/files/usr/bin/bash
MESSAGE="${1:-🔥 精選爆款數位內容與專屬福利}"
LINE_CTA="

👉 點擊領取 VIP 獨家內容 / 自動下單優惠：
https://line.me/R/ti/p/@your_line_id"

FULL_MSG="${MESSAGE}${LINE_CTA}"

# 發送請求給 Make.com 的 LINE Webhook 觸發端點
curl -X POST -H "Content-Type: application/json" \
     -d "{\"message\": \"$FULL_MSG\"}" \
     https://hook.eu1.make.com/YOUR_LINE_WEBHOOK_ID >> ~/auto_traffic_bot/logs/line_schedule.log 2>&1

echo "[+] LINE 廣播與自動變現請求已發送！" >> ~/auto_traffic_bot/logs/line_schedule.log
