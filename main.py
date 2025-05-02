from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "애순이가 정상 작동 중입니다."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)