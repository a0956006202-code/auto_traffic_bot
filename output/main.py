import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = FastAPI(
    title="AI Video Assistant API",
    description="爆款影音自動化生成與文案分析後端引擎",
    version="1.0.0"
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class ScriptRequest(BaseModel):
    topic: str
    target_platform: str = "Shorts/TikTok/FB Reels"
    cta_link: str = "https://line.me/R/ti/p/@your_line_id"

class ScriptResponse(BaseModel):
    status: str
    topic: str
    hook: str
    script_content: str
    cta_prompt: str

@app.get("/")
def read_root():
    return {
        "message": "AI Video Assistant 後端引擎運作中！",
        "status": "Active"
    }

@app.post("/api/v1/generate-script", response_model=ScriptResponse)
async def generate_script(request: ScriptRequest):
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="Gemini API Key 未設定")

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        prompt = f"""
        你是一位頂尖的流量專家與短影音導演。
        請為主題：『{request.topic}』設計一支專屬於 {request.target_platform} 的高轉化爆款短影音腳本。
        
        要求包含：
        1. 【前3秒抓眼球 (Hook)】：強烈的視覺/情緒衝擊，讓人不滑走。
        2. 【核心內容】：節奏明快、痛點明確的精簡腳本。
        3. 【行動呼籲 (CTA)】：引導觀眾點擊資訊欄或留言區的導購/引流連結 ({request.cta_link})。
        """

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )

        return ScriptResponse(
            status="success",
            topic=request.topic,
            hook="前3秒爆款開頭已嵌入腳本內",
            script_content=response.text,
            cta_prompt=f"請點擊下方連結獲得更多獨家好康：{request.cta_link}"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI 生成失敗: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
