# app.py
import streamlit as st

st.set_page_config(page_title="MBTI별 진로 추천", page_icon="🎯", layout="centered")

MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 각 MBTI에 대해 진로 2개씩: title, 적합 학과(목록), 어울리는 성격 설명
MBTI_CAREERS = {
    "ISTJ": [
        {"title":"공무원 / 행정직","departments":["행정학과","법학과","경영학과"], "personality":"책임감 강하고 규칙 잘 지키는 사람에게 딱! 절차와 안정감을 좋아하면 편해요. ✅", "emoji":"🏛️"},
        {"title":"회계사 / 재무직","departments":["회계학과","경영학과","세무학과"], "personality":"디테일 강하고 숫자 꼼꼼한 사람에게 적합. 계획 세워서 실행하는 걸 좋아해요. 💹", "emoji":"📊"}
    ],
    "ISFJ": [
        {"title":"간호사 / 의료복지","departments":["간호학과","보건학과","사회복지학과"], "personality":"배려심 많고 꾸준히 돌보는 걸 좋아하는 사람에게 좋아요. 따뜻한 손길이 강점! 💖", "emoji":"🩺"},
        {"title":"초등교사 / 교육 관련","departments":["교육학과","아동학과","특수교육과"], "personality":"섬세하고 인내심 있는 성격이면 아이들과 잘 맞아요. 안정적인 환경 선호! 🍎", "emoji":"🎒"}
    ],
    "INFJ": [
        {"title":"상담심리사 / 임상심리","departments":["심리학과","상담학과"], "personality":"사람의 내면을 이해하고 돕는 걸 좋아하는 사람에게 최고. 공감 능력 큰 장점이에요. 🧠", "emoji":"💬"},
        {"title":"콘텐츠 기획 / 에디터","departments":["문예창작/국어국문","미디어학과","커뮤니케이션학과"], "personality":"창의적으로 의미 있는 작업을 선호하고, 가치 중심으로 일할 때 힘나요. ✍️", "emoji":"📝"}
    ],
    "INTJ": [
        {"title":"연구원 / 데이터 사이언티스트","departments":["컴퓨터공학","통계학","수학과"], "personality":"논리적 사고와 계획을 잘 세우는 사람에게 적합. 문제 해결을 즐기면 굿! 🔬", "emoji":"🧪"},
        {"title":"전략 컨설턴트 / 기획","departments":["경영학과","경제학과","산업공학과"], "personality":"큰 그림 보고 전략 세우는 걸 좋아하는 사람에게 추천. 목표지향적 성격 좋음. ♟️", "emoji":"📈"}
    ],
    "ISTP": [
        {"title":"기계·설비 엔지니어","departments":["기계공학과","전기공학과","메카트로닉스"], "personality":"손으로 직접 만들고 고치는 걸 좋아하는 실용주의자에게 딱! 🔧", "emoji":"⚙️"},
        {"title":"응급구조사 / 소방관","departments":["응급구조학과","소방안전학과","체육학과"], "personality":"상황 판단 빠르고 실전에서 행동 잘하는 사람에게 어울려요. 긴장감 있는 환경 OK면 좋아요. 🚨", "emoji":"🚒"}
    ],
    "ISFP": [
        {"title":"디자이너 (그래픽 / 패션)","departments":["시각디자인과","패션디자인과","예술대"], "personality":"감각적이고 표현을 좋아하는 사람에게 추천. 자유롭게 창작하는 걸 즐기면 최고! 🎨", "emoji":"👗"},
        {"title":"원예·동물 관련 직업","departments":["생명과학과","원예학과","동물자원학과"], "personality":"자연과 생명을 돌보는 걸 좋아하는 사람에게 잘 맞아요. 차분하고 따뜻한 성향 환영! 🌿", "emoji":"🌼"}
    ],
    "INFP": [
        {"title":"작가 / 문예창작","departments":["국어국문학과","문예창작과","철학과"], "personality":"내면 세계가 풍부하고 표현으로 풀어낼 줄 아는 사람에게 좋아요. 감성 충만✅", "emoji":"📚"},
        {"title":"NGO / 사회운동가","departments":["사회복지학과","국제학과","사회학과"], "personality":"가치 중심으로 사람이나 사회를 돕고 싶어하는 사람에게 적합해요. 이상주의 강점! ✨", "emoji":"🤝"}
    ],
    "INTP": [
        {"title":"소프트웨어 개발자 / 연구자","departments":["컴퓨터공학과","전산학과","전자공학과"], "personality":"개념적 사고와 호기심이 많은 사람에게 좋아요. 혼자 깊게 파는 걸 즐긴다면 최고! 💻", "emoji":"🧩"},
        {"title":"학술 연구 / 이론물리 등","departments":["물리학과","수학과","철학과"], "personality":"논리적 분석과 이론 탐구를 즐기는 타입이면 잘 맞아요. 고독을 즐기는 편이면 편함. 🔭", "emoji":"🔬"}
    ],
    "ESTP": [
        {"title":"영업 / 스타트업 운영","departments":["경영학과","마케팅학과","창업학부"], "personality":"사람 만나서 설득하고 즉각 행동하는 걸 좋아하면 딱! 리스크 감수 잘하는 편. 🗣️", "emoji":"💼"},
        {"title":"이벤트·무대 스태프 / 방송 제작","departments":["미디어학과","방송연예과","공연예술과"], "personality":"현장감 있는 일을 즐기고 순간 판단 빠른 사람에게 추천해요. 에너지가 넘침! 🎤", "emoji":"🎬"}
    ],
    "ESFP": [
        {"title":"연예·공연·크리에이터","departments":["공연예술학과","미디어학과","디지털콘텐츠과"], "personality":"사람들과 함께 즐기고 표현하는 걸 좋아하는 사람에게 최적! 무대 체질이면 굿👍", "emoji":"🎭"},
        {"title":"카페·서비스 업종 / 호텔리어","departments":["관광학과","조리학과","호텔경영학과"], "personality":"밝고 사교적이며 즉각 고객 반응에 즐거움을 느끼는 타입에게 잘 맞아요. 🍰", "emoji":"☕"}
    ],
    "ENFP": [
        {"title":"광고·브랜딩 기획","departments":["광고홍보학과","미디어커뮤니케이션","디자인학과"], "personality":"아이디어가 풍부하고 사람 마음을 움직이는 걸 좋아하면 최고! 창의력 폭발 ⚡", "emoji":"🎨"},
        {"title":"교육 기획 / 코칭","departments":["교육학과","상담학과","심리학과"], "personality":"사람을 응원하고 동기를 부여하는 걸 좋아하는 성격이면 딱이야. 열정적이고 사교적! 🌟", "emoji":"📣"}
    ],
    "ENTP": [
        {"title":"창업가 / 신사업 개발","departments":["경영학과","산업공학과","융합전공"], "personality":"새로운 아이디어로 실험하고 도전하는 걸 즐기는 유형. 빠른 변화 좋아함 🚀", "emoji":"🧠"},
        {"title":"변호사 / 논쟁적 직업","departments":["법학과","정책학과"], "personality":"논리적이고 토론을 즐기는 사람에게 잘 맞아요. 설득력과 창의적 사고 강점! ⚖️", "emoji":"🗡️"}
    ],
    "ESTJ": [
        {"title":"관리자 / 운영 매니저","departments":["경영학과","산업경영학과","행정학과"], "personality":"조직을 정리하고 이끌어가는 걸 좋아하는 리더형에게 추천. 책임감과 실무력 강함. 🧾", "emoji":"📋"},
        {"title":"회계·재무 관리자","departments":["회계학과","금융학과"], "personality":"규칙과 절차를 중시하고 체계적으로 관리하는 것을 잘하는 스타일이면 좋아요. 💼", "emoji":"🏦"}
    ],
    "ESFJ": [
        {"title":"간호·보건 행정","departments":["간호학과","보건행정학과","사회복지학과"], "personality":"사람을 돕고 관리하는 걸 즐기는 친절한 타입에게 추천. 팀워크 잘함! 🤗", "emoji":"🩹"},
        {"title":"HR·인사 담당","departments":["경영학과","심리학과","인적자원학과"], "personality":"사람 관계를 잘 관리하고 지원하는 역할에서 빛나는 타입이에요. 섬세한 소통력 굿. 🧑‍🤝‍🧑", "emoji":"💼"}
    ],
    "ENFJ": [
        {"title":"컨설턴트 / 교육 강사","departments":["교육학과","심리학과","경영학과"], "personality":"사람을 이끌고 성장시키는 걸 좋아하는 카리스마형. 팀을 응집시키는 능력 최고! 🌱", "emoji":"🎓"},
        {"title":"홍보·커뮤니케이션 전문가","departments":["홍보학과","미디어학과","커뮤니케이션학과"], "personality":"사람 앞에서 말하고 조정하는 걸 잘하는 사회적 리더형에게 추천해요. 📢", "emoji":"📣"}
    ],
    "ENTJ": [
        {"title":"기업 임원·전략기획","departments":["경영학과","경제학과","산업공학과"], "personality":"목표 지향적이고 리더십이 강한 타입에게 딱. 조직을 이끌고 전략 짜는 걸 좋아하면 굿! 🏆", "emoji":"🏢"},
        {"title":"투자은행(IB)/벤처캐피탈","departments":["금융학과","경영학과","경제학과"], "personality":"결단력 있고 분석적으로 큰 결정을 내리는 일을 즐기는 타입에게 추천해요. 숫자와 전략에 강함. 💸", "emoji":"💼"}
    ]
}

def render_career_block(c):
    # c: dict with title, departments, personality, emoji
    st.markdown(f"### {c['emoji']} {c['title']}")
    st.write(f"**추천 학과:** {', '.join(c['departments'])}")
    st.write(f"**어떤 성격이 잘 맞을까?** {c['personality']}")
    st.divider()

def main():
    st.title("🎯 MBTI로 보는 맞춤 진로 추천")
    st.write("너의 MBTI 하나만 골라봐! 그 유형에 어울리는 진로 2개랑, 어떤 학과가 적합한지, 어떤 성격이 잘 맞는지도 알려줄게 — 학생들이 보기 편하게 쉽게 썼어. 😄")

    mbti = st.selectbox("MBTI를 선택하세요", MBTI_LIST, index=10)  # ENFP 기본 선택
    st.write("---")

    st.subheader(f"🔎 {mbti} 유형에게 어울리는 진로")
    careers = MBTI_CAREERS.get(mbti, [])
    if not careers:
        st.info("아직 데이터가 없네... 다른 유형 골라볼래? 😅")
        return

    for c in careers:
        render_career_block(c)

    st.info("참고: 추천은 일반적 성향을 바탕으로 한 제안이야. 너의 흥미와 경험을 더해 최종 선택하자! 필요하면 특정 직업 더 자세히 설명해줄게 🙂")

    st.write("---")
    st.caption("Made with ❤️ — 진로는 방향성 제안이니, 궁금한 진로가 있으면 더 물어봐줘!")

if __name__ == "__main__":
    main()
