import streamlit as st
import random

st.set_page_config(page_title="오늘의 기분 스타일 추천", page_icon="🎨", layout="centered")

st.title("🎨 오늘의 기분에 맞는 스타일 추천")

# 기분 선택
mood = st.radio(
    "오늘 기분은 어떤가요?",
    ["😊 행복해요", "😪 피곤해요", "😔 우울해요", "🤩 신나요", "😌 차분해요"]
)

# 스타일 추천 딕셔너리
style_recommendations = {
    "😊 행복해요": [
        "밝은 파스텔톤 캐주얼 룩 👕",
        "화려한 패턴 원피스 👗",
        "산뜻한 스트릿 패션 👟"
    ],
    "😪 피곤해요": [
        "편안한 오버사이즈 후드티 🧢",
        "트레이닝 세트 👖",
        "부드러운 니트웨어 🧶"
    ],
    "😔 우울해요": [
        "세련된 모노톤 스타일 ⚫⚪",
        "깔끔한 미니멀 오피스룩 👔",
        "감성적인 빈티지 룩 📸"
    ],
    "🤩 신나요": [
        "트렌디한 스트릿 패션 👟",
        "화려한 컬러 믹스 매치 🎨",
        "개성 강한 액세서리 스타일 💍"
    ],
    "😌 차분해요": [
        "심플한 원컬러 룩 🤍",
        "자연스러운 린넨 스타일 🌿",
        "미니멀 모던룩 🖤"
    ]
}

# 추천 스타일 출력
if mood:
    choice = random.choice(style_recommendations[mood])
