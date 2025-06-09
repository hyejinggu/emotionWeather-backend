from openai import AsyncOpenAI
import os

# 환경변수에서 API 키 불러오기
api_key = os.getenv("OPENAI_API_KEY")

# API 클라이언트 생성
openai_client = AsyncOpenAI(api_key=api_key)

async def get_ai_feedback(summary: dict) -> str:
    prompt = f"다음은 감정 데이터 요약입니다. 분석해 주세요: \n{summary}"
    response = await openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()