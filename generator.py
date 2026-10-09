import os
import json
import datetime

def main():
    print("[*] 啟動自動化流量與內容生成核心...")
    os.makedirs("content", exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_filename = f"content/post_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    post_text = f"自動化熱門影音內容 - {timestamp}\n精選高流量話題與數據分析，全自動推播中！\n#爆紅影音帝國 #自動化流量"
    
    with open(content_filename, "w", encoding="utf-8") as f:
        f.write(post_text)
        
    print(f"[+] 成功生成新內容: {content_filename}")

if __name__ == "__main__":
    main()
