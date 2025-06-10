# Emotion Weather ☁️😊

**Emotion Weather** is an interactive emotion tracking project that collects user sentiment through QR code sharing.  
By leveraging AI, it analyzes collective emotional trends using weather metaphors — offering engaging and meaningful emotional feedback and visualizations.

사용자들이 공유한 QR 링크를 통해 감정 데이터를 수집하고, <br>
AI 기반 분석 시스템이 기상 용어를 활용하여 감정 상태를 체계적이고 흥미롭게 해석 및 예측합니다. <br>
따뜻한 피드백과 이모지 시각화를 통해 사용자 간 감정 공유와 커뮤니티 내 정서적 통찰을 제공합니다.

---

## 🌟 Features

- Generate QR codes for group sharing
- Input your current or future emotional state (via emoji)
- Store all emotion data in PostgreSQL
- Generate warm, empathetic feedback using the OpenAI API
- Summarize and visualize group-wide emotional trends

---

## 🛠 Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: JavaScript (Vanilla JS or React)
- **Database**: PostgreSQL
- **AI**: OpenAI API (GPT)
- **Deployment (Planned)**: Railway / Vercel / Render 등

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/hyejinggu/emotion-weather.git
cd emotion-weather
```

### 2. Set up a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the development server
```bash
uvicorn main:app --reload
```

---

## 📘 API Docs

- Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🗓️ Roadmap / TODO

- [ ] Build emotion input API
- [ ] Connect PostgreSQL and persist data
- [ ] Implement QR-based group management
- [ ] Integrate OpenAI API and parse responses
- [ ] Create the group emotion summary page
- [ ] Deploy the project


---

## 🙋‍♀️ About

This is a personal side project and a learning experiment
to explore how FastAPI and OpenAI can be combined to create
a meaningful, emotion-aware web experience.
