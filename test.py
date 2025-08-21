import streamlit as st
import random
from datetime import date

# 운세 메시지와 스타일 추천 데이터
fortune_data = {
    "행운 가득 🍀": {
        "style": "밝은 색상의 옷 (옐로우, 화이트)",
        "tip": "화려한 액세서리로 포인트!"
    },
    "조심조심 ⚡": {
        "style": "편안한 캐주얼 (진, 후드티)",
        "tip": "오늘은 무난하게 가는 게 좋아요."
    },
    "에너지 업 🔥": {
        "style": "레드, 오렌지 계열",
        "tip": "강렬한 색상으로 자신감 UP!"
    },
    "힐링데이 🌿": {
        "style": "파스텔톤, 편안한 원피스/셔츠",
        "tip": "자연스러운 스타일이 잘 어울려요."
    },
    "로맨틱 💕": {
        "style": "핑크톤, 로맨틱한 디테일",
        "tip": "데이트 룩으로 완벽!"
    }
}

st.title("✨ 오늘의 운세 & 스타일 추천 ✨")

# 사용자 입력
name = st.text_input("이름을 입력하세요")
birthday = st.date_input("생일을 선택하세요")

if st.button("오늘의 운세 보기"):
    today = date.today()
    # 간단한 난수 기반 운세 선택 (이름+날짜 조합으로 고정되도록)
    seed = hash(name + str(today)) % len(fortune_data)
    fortune = list(fortune_data.keys())[seed]
    
    st.subheader(f"오늘의 운세: {fortune}")
    st.write(f"👗 추천 스타일: {fortune_data[fortune]['style']}")
    st.write(f"💡 팁: {fortune_data[fortune]['tip']}")
