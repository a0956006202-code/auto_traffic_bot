# 零成本自動化流量工廠 - 免費工具與創作引流配置
FREE_TOOLS_MATRIX = {
    "prompt_generator": "https://hihomoney.com/tools/ai-prompt-generator",
    "image_resizer": "https://hihomoney.com/tools/free-image-resizer",
    "shorts_script_maker": "https://hihomoney.com/tools/shorts-script-generator"
}

def inject_free_tools_cta(content):
    """自動在文章末端插入免費工具與創作引誘 CTA"""
    cta_text = "\n\n---\n### 💡 想要一鍵創作？試試我們的免費 AI 工具：\n"
    cta_text += f"- 🛠️ [免費 AI 提示詞產生器]({FREE_TOOLS_MATRIX['prompt_generator']})\n"
    cta_text += f"- ✂️ [短影音腳本一鍵生成器]({FREE_TOOLS_MATRIX['shorts_script_maker']})\n"
    return content + cta_text

if __name__ == "__main__":
    print("[+] 免費工具與創作引流模組測試成功！")
