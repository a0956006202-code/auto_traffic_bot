import json

def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

if __name__ == '__main__':
    config = load_config()
    print("=== 零成本 AI 自動化流量變現管線啟動 ===")
    print(f"收款銀行: {config['payout_method']} ({config['bank_code']})")
    print(f"分局: {config['branch']}")
    print(f"戶名: {config['account_info']['name']}")
    print("狀態: 上游 AI 流量導流與自動化排程準備就緒！")
}
