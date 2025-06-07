# .env 로드
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# AsyncSession: SQLAlchemy의 비동기 세션 클래스
# create_async_engine: PostgreSQL과 같은 DB에 비동기로 연결할 수 있는 엔진 생성 함수
# → 일반 SQLAlchemy 엔진(create_engine)과 다르게 asyncio 환경에 맞춤.
# SQLAlchemy의 sessionmaker는 세션(트랜잭션 단위 작업 객체)을 만들어주는 팩토리 함수

# .env 파일에 있는 환경변수를 Python 코드에서 사용할 수 있게 불러오기 위한 모듈입니다.
# os.getenv()로 .env에 정의한 변수 값을 가져옵니다.

# --------------------------------------------------------------------------


# .env 파일을 로드해서 os.environ에 등록
load_dotenv()  

DATABASE_URL = os.getenv("DATABASE_URL")

# DB와 연결되는 SQLAlchemy 비동기 엔진을 생성합니다.
# echo=True는 SQL 로그를 콘솔에 출력하게 해 줍니다 (디버깅용).
engine = create_async_engine(DATABASE_URL, echo=True)

# 세션 생성기
# FastAPI의 의존성 주입(Depends)으로 사용할 때 여기서 세션을 꺼내서 사용하게 됩니다.
# expire_on_commit=False: 기본값은 True인데, commit 이후 객체가 expire(무효화)되는 걸 막습니다.
# 즉, 커밋 후에도 데이터를 계속 쓰고 싶을 때 사용.
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency: FastAPI 라우터에서 사용
# FastAPI 라우터에서 Depends(get_db)로 사용하게 됩니다.
# 이 함수는 매 요청마다 비동기 세션을 생성 → 요청이 끝나면 자동 종료해 줍니다.
# yield는 Python의 generator 문법으로, 세션을 반환하면서도 context를 닫을 수 있게 합니다.
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session