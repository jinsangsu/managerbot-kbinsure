# 베이스 이미지: Python 3.10
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY main.py /app/
COPY requirements.txt /app/

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 환경변수로 PORT 설정
ENV PORT=8080

# FastAPI 앱 실행 (포트는 Fly.io가 자동 할당)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]