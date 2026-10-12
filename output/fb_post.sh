#!/bin/bash
# 使用方式: ./fb_post.sh "你想發布的貼文內容"

MESSAGE="${1:-預設自動發文內容}"

curl -s -X POST "https://hook.eu1.make.com/vrjxbyrgwg37vth1rblad8kqderlrp1b" \
     -H "Content-Type: application/json" \
     -d "{\"text\": \"$MESSAGE\"}"

echo -e "\n[+] 貼文請求已發送！"
