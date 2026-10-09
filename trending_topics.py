import json
import random

# 預設的高流量與熱門內容主題庫（可隨時擴充）
HOT_TOPICS = [
    {"category": "科技與AI", "keyword": "AI 自動化賺錢新模式"},
    {"category": "副業與被動收入", "keyword": "零成本架設全自動內容工廠"},
    {"category": "熱門時事", "keyword": "如何利用免費雲端工具實現自動導流"},
    {"category": "數位行銷", "keyword": "社群演算法破解與爆紅影音技巧"}
]

def get_random_topic():
    selected = random.choice(HOT_TOPICS)
    print(f"[+] 已選取今日高流量主題：【{selected['category']}】{selected['keyword']}")
    return selected

if __name__ == "__main__":
    get_random_topic()
