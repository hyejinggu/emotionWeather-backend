# Emotion Weather (감정 날씨 프로젝트) ☁️😊

사용자들이 공유한 QR 링크를 통해 감정 데이터를 수집하고,
AI 기반 분석 시스템이 기상 용어를 활용하여 감정 상태를 체계적이고 흥미롭게 해석 및 예측합니다.
따뜻한 피드백과 이모지 시각화를 통해 사용자 간 감정 공유와 커뮤니티 내 정서적 통찰을 제공합니다.

---

## 🌟 Features

- QR 생성 및 링크 공유 기능
- 감정 입력 (현재 / 몇 시간 후) 인터페이스
- 감정 데이터를 PostgreSQL에 저장
- OpenAI API를 활용한 감정 피드백 생성
- 같은 QR 그룹 사용자들의 감정을 기반으로 결과 요약 및 시각화

---

## 🛠 Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: JavaScript (Vanilla JS or React)
- **Database**: PostgreSQL
- **AI**: OpenAI API (GPT)
- **Deployment (예정)**: Railway / Vercel / Render 등

---

## 🚀 Getting Started

### 1. 클론 및 폴더 이동
```bash
git clone https://github.com/hyejinggu/emotion-weather.git
cd emotion-weather
```

### 2. 가상 환경 생성 및 활성화
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 서버 실행
```bash
uvicorn main:app --reload
```

---

## 📘 API 문서

- Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🗓️ Roadmap / TODO

- [ ] 감정 입력 API 구현
- [ ] PostgreSQL 연결 및 데이터 저장
- [ ] QR 코드 기반 그룹 기능
- [ ] OpenAI API 통신 및 응답 파싱
- [ ] 결과 요약 페이지 구현
- [ ] 프로젝트 배포


---

## 🙋‍♀️ About

이 프로젝트는 혼자서 진행하는 작은 실험이자,  
FastAPI와 OpenAI를 활용한 감정 데이터 기반 웹서비스 개발 연습용 프로젝트입니다.