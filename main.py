
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "애순이가 정상 작동 중입니다."}
