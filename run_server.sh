#!/bin/bash

PORT=8000

# 현재 포트를 사용 중인 프로세스 확인
PID=$(lsof -ti :$PORT)

# 포트 사용 중이면 프로세스 종료
if [ -n "$PID" ]; then
  echo "🛑 포트 $PORT 사용 중 프로세스 종료 (PID: $PID)"
  kill -9 $PID
fi

# FastAPI 서버 실행
echo "🚀 FastAPI 서버 시작 at http://localhost:$PORT"
uvicorn app.main:app --reload --port $PORT
