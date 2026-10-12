#!/data/data/com.termux/files/usr/bin/bash
MESSAGE="${1:-Trending Video | Best Clips of the Day}"

# 全球化吸粉文案與多國熱門標籤
GLOBAL_CTA="

👉 Follow '數位影音' for daily viral videos!
#Viral #Trending #Reels #Shorts #Foryou #VideoOfTheDay #Fyp"

FULL_MSG="${MESSAGE}${GLOBAL_CTA}"

# 執行發文並紀錄日誌
/data/data/com.termux/files/usr/bin/fbpost "$FULL_MSG" >> ~/auto_traffic_bot/logs/fb_schedule.log 2>&1
