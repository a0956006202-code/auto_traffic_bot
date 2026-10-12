#!/data/data/com.termux/files/usr/bin/bash
MESSAGE="${1:-Trending Video | Best Clips of the Day}"
GLOBAL_CTA=" 👉 Follow '數位影音' for daily viral videos! #Viral #Trending #Reels #Shorts #Foryou #VideoOfTheDay #Fyp"

# 清除危險的換行字元，組合乾淨字串
FULL_MSG="${MESSAGE}${GLOBAL_CTA}"

# 執行發文並寫入日誌
/data/data/com.termux/files/usr/bin/fbpost "$FULL_MSG" >> ~/auto_traffic_bot/logs/fb_schedule.log 2>&1
