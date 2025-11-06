# app.py
import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="🌟 오늘의 별자리 오하이사 운세", page_icon="🌠", layout="centered")

st.title("🌟 오늘의 별자리 오하이사 운세 🔮")
st.write("오늘은 어떤 하루가 될까? 🤔")
st.write("별자리를 선택하면 **오하이사 운세 순위✨**랑 **행운의 행동🍀**을 알려줄게!")

# 12별자리 리스트
zodiacs = [
    "양자리 ♈", "황소자리 ♉", "쌍둥이자리 ♊", "게자리 ♋",
    "사자자리 ♌", "처녀자리 ♍", "천칭자리 ♎", "전갈자리 ♏",
    "사수자리 ♐", "염소자리 ♑", "물병자리 ♒", "물고기자리 ♓"
]

# 행운 행동 예시 리스트
lucky_actions = [
    "오늘은 친구에게 먼저 인사하기 👋",
    "좋아하는 노래를 들으며 기분 업! 🎧",
    "책상 정리 깔끔하게 하기 🧹",
    "달콤한 간식 하나 먹기 🍫",
    "하늘 보면서 심호흡 3번 🌤️",
    "오늘 하루 감사한 일 3가지 적기 ✍️",
    "새로운 사람에게 웃으며 인사하기 😊",
    "공부 25분 집중 + 5분 스트레칭 💪",
    "물 자주 마시기 💧",
    "하루 목표 1개만 꼭 달성하기 🎯",
    "부모님께 고맙다고 말하기 💌",
    "SNS 쉬고 자기 시간 가지기 📵"
]

# 사용자 입력
selected = st.selectbox("⭐ 나의 별자리는?", zodiacs, index=0)

# 실행 버튼
if st.button("오늘의 운세 보기 🔮"):
    st.divider()

    # 오늘 날짜 기준으로 시드 고정 (매일 바뀌는 운세)
    today = date.today()
    random.seed(selected + str(today))
    rank = random.randint(1, 12)

    # 운세 메시지
    if rank <= 3:
        mood = "✨ 대박 운세! 오늘 완전 텐션 오를 각이야 🔥"
        emoji = "😆"
    elif rank <= 6:
        mood = "😊 꽤 괜찮은 하루가 될 거야! 즐겁게 보내자 🌈"
        emoji = "🌞"
    elif rank <= 9:
        mood = "🙂 무난무난~ 평범하지만 너답게 꾸며봐 🎧"
        emoji = "☕"
    else:
        mood = "😴 살짝 다운될 수도 있지만 괜찮아! 천천히 가면 돼 🍀"
        emoji = "🌙"

    st.subheader(f"{selected}의 오늘 오하이사 운세는... 🎉 **{rank}등!** {emoji}")
    st.write(mood)
    st.divider()

    # 행운 행동 추천
    action = random.choice(lucky_actions)
    st.markdown(f"💫 **오늘의 행운 행동:** {action}")
    st.info("작은 행동 하나가 기분을 바꿔줄지도 몰라! 오늘도 파이팅 💪")

st.write("---")
st.caption("🪄 오하이사 운세는 재미로 보는 거야! 진짜 운은 너의 손에 달려있어 ✨")
