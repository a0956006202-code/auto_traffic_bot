import os
import datetime
from trending_topics import get_random_topic

def generate_content():
    os.makedirs("content", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"content/post_{timestamp}.txt"
    
    topic = get_random_topic()
    
    content = f"""
========================================
發布時間：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
內容分類：{topic['category']}
核心關鍵字：{topic['keyword']}
----------------------------------------
這是一篇透過 Termux 自動化流量工廠產出的高流量優化貼文。
目標平台：全自動分發渠道
變現閉環：中華郵政導流收益專用通道
========================================
"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content.strip())
        
    print(f"[+] 成功生成自動化內容檔案：{filename}")

if __name__ == "__main__":
    generate_content()
