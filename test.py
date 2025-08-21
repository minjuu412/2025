import streamlit as st
import random
from datetime import date

# 운세 메시지와 스타일 추천 데이터 (더 풍부하게 확장)
fortune_data = {
    "행운 가득 🍀": {
        "style": "밝은 색상의 옷 (옐로우, 화이트)",
        "tip": "화려한 액세서리로 포인트!",
        "love": "오늘은 사랑이 찾아오는 날 💕",
        "money": "작은 투자에서 큰 성과! 💰",
        "health": "컨디션이 최상이에요!",
        "color": "옐로우",
        "item": "스카프"
    },
    "조심조심 ⚡": {
        "style": "편안한 캐주얼 (진, 후드티)",
        "tip": "오늘은 무난하게 가는 게 좋아요.",
        "love": "연인과의 다툼 주의 😬",
        "money": "지출을 줄이는 게 좋아요.",
        "health": "무리하면 피로가 쌓일 수 있어요.",
        "color": "블랙",
        "item": "운동화"
    },
    "에너지 업 🔥": {
        "style": "레드, 오렌지 계열",
        "tip": "강렬한 색상으로 자신감 UP!",
        "love": "매력지수가 최고조! ❤️",
        "money": "도전적인 투자에 행운이!",
        "health": "활력이 넘치는 하루!",
        "color": "레드",
        "item": "시계"
    },
    "힐링데이 🌿": {
        "style": "파스텔톤, 편안한 원피스/셔츠",
        "tip": "자연스러운 스타일이 잘 어울려요.",
        "love": "혼자만의 시간이 필요한 날 💭",
        "money": "평온한 소비, 불필요한 지출 X",
        "health": "휴식이 필요해요.",
        "color": "그린",
        "item": "책"
    },
    "로맨틱 💕": {
        "style": "핑크톤, 로맨틱한 디테일",
        "tip": "데이트 룩으로 완벽!",
        "love": "운명 같은 인연을 만날 수 있어요 ✨",
        "money": "선물에 지출이 생길 수 있어요.",
        "health": "마음이 편안해지는 하루.",
        "color": "핑크",
        "item": "향수"
    }
}

st.title("✨ 오늘의 운세 & 스타일 추천 ✨")

# 사용자 입력
name = st.text_input("이름을 입력하세요")

gender = st.selectbox("성별을 선택하세요", ["남성", "여성", "기타"])

birthday = st.date_input(
    "생일을 선택하세요",
    min_value=date(2000, 1, 1),
    max_value=date(2025, 12, 31)
)

mood = st.radio("오늘의 기분은 어떤가요?", ["😊 좋음", "😐 보통", "😢 우울"])

if st.button("오늘의 운세 보기"):
    today = date.today()
    # 간단한 난수 기반 운세 선택
    seed = hash(name + str(birthday) + mood) % len(fortune_data)
    fortune = list(fortune_data.keys())[seed]
    
    data = fortune_data[fortune]
    
    st.subheader(f"오늘의 운세: {fortune}")
    st.write(f"👗 추천 스타일: {data['style']}")
    st.write(f"💡 스타일 팁: {data['tip']}")
    st.write(f"❤️ 사랑운: {data['love']}")
    st.write(f"💰 금전운: {data['money']}")
    st.write(f"💪 건강운: {data['health']}")
    st.write(f"🎨 행운 컬러: {data['color']}")
    st.write(f"🔮 행운 아이템: {data['item']}")
    st.success(f"{name}님({gender}), 오늘도 멋진 하루 보내세요! 🌟")
