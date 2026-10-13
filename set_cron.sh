#!/data/data/com.termux/files/usr/bin/bash
(crontab -l 2>/dev/null | grep -v 'auto_traffic_bot'; \
 echo "0 0 * * * ~/auto_traffic_bot/output/fb_post.sh '🔥 Must Watch! Trending Clip #1'" ; \
 echo "0 8 * * * ~/auto_traffic_bot/output/fb_post.sh '🌐 Best Viral Video #2'" ; \
 echo "0 16 * * * ~/auto_traffic_bot/output/fb_post.sh '✨ Amazing Highlights #3'" ; \
 echo "30 12 * * * ~/auto_traffic_bot/output/line_post.sh '🎬【午間限定】爆款影音與獨家 VIP 優惠'" ; \
 echo "30 20 * * * ~/auto_traffic_bot/output/line_post.sh '✨【夜間精選】熱門數位內容自動導購'" ; \
 echo "0 */6 * * * python3 ~/auto_traffic_bot/guardian.py >> ~/auto_traffic_bot/logs/guardian.log 2>&1") | crontab -
