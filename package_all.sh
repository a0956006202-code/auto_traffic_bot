echo "=== 開始執行全系統最後總封存 ==="
python3 maintain_logs.py
cd ~
tar -czf auto_traffic_bot_final.tar.gz --exclude='__pycache__' --exclude='.git' auto_traffic_bot
ls -lh auto_traffic_bot_final.tar.gz
echo "=== 全系統架構封存完畢，準備迎接長期自動變現！ ==="
