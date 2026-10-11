# 零成本自動化流量工廠 - 導購與聯盟行銷連結配置
AFFILIATE_LINKS = {
    "ChatGPT": "https://hihomoney.com/go-chatgpt",
    "Canva": "https://hihomoney.com/go-canva",
    "CapCut": "https://hihomoney.com/go-capcut",
    "Make": "https://hook.eu1.make.com/rmtwfknkrxm4mkdwbs3xw7ucnghpig4f"
}

def inject_affiliate_links(content):
    """自動將熱門關鍵字替換為帶有導購與變現追蹤的連結"""
    for name, link in AFFILIATE_LINKS.items():
        if name in content:
            content = content.replace(name, f"[{name}]({link})")
    return content

if __name__ == "__main__":
    test_text = "PTT 與 Dcard 網友熱推 ChatGPT 與 Canva AI 工具！"
    print("[+] 導流連結注入測試結果：")
    print(inject_affiliate_links(test_text))
