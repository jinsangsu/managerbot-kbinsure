from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GPT API Key는 환경변수로부터 불러옴
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/managerbot")
async def chat_with_managerbot(req: Request):
    data = await req.json()
    messages = data.get("messages", [])
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
        )
        reply = response.choices[0].message.content
        return {"reply": reply}
    except Exception as e:
        print("🔥 GPT 호출 오류:", str(e))
        return {"reply": "애순이가 지금은 답변을 드릴 수 없어요. (서버 오류일 수 있어요.)"}