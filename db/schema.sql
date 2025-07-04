CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE qr_group (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    group_name VARCHAR(100),
    qr_image TEXT
);

CREATE TABLE user_session (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    qr_group_id UUID NOT NULL,
    joined_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ai_feedback (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    qr_group_id UUID NOT NULL,
    generated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    summary_json JSON NOT NULL,
    openai_prompt TEXT,
    response_text TEXT
);

CREATE TABLE emotion_entry (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_session_id UUID NOT NULL,
    emotion TEXT NOT NULL,
    time_type TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    target_time TIMESTAMP
);
