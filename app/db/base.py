# Base는 SQLAlchemy에서 모든 테이블 모델의 부모 클래스
# SQLAlchemy에서는 모델 클래스들을 등록할 수 있는 공통 부모 클래스가 필요합니다.
# 그래야 나중에 Base.metadata.create_all()로 모든 테이블을 자동 생성하거나, ORM에서 테이블 간 관계를 설정할 수 있습니다.

from sqlalchemy.orm import declarative_base

Base = declarative_base()


