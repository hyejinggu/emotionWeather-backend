from openai import AsyncOpenAI
import os, json
from datetime import datetime
from ai_prompt_template import AI_PROMPT_TEMPLATE
from fastapi import HTTPException

# 환경변수에서 API 키 불러오기
api_key = os.getenv("OPENAI_API_KEY")

# API 클라이언트 생성
openai_client = AsyncOpenAI(api_key=api_key)

async def get_ai_feedback(summary: dict, current_time: datetime) -> dict:
    prompt = AI_PROMPT_TEMPLATE.format(
        summary = summary,
        current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    )
    
    response = await openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    content = response.choices[0].message.content.strip()
    try: 
        return json.loads(content)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="AI 응답이 유효한 JSON 형식이 아닙니다.")