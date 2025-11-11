# main.py
import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="오기구인의 서울 TOP10", layout="wide")

# --- 지도 데이터 설정 ---
PLACES = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.579884, "lon": 126.9768,
     "desc": "조선의 대표 궁궐. 광화문과 함께 서울의 상징."},
    {"name": "창덕궁 (Changdeokgung Palace & Huwon)", "lat": 37.57944, "lon": 126.99278,
     "desc": "유네스코 세계유산으로 유명한 궁궐과 후원."},
    {"name": "남산서울타워 (N Seoul Tower / Namsan Tower)", "lat": 37.551170, "lon": 126.988228,
     "desc": "서울 전망 명소 — 야경이 특히 유명."},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.582178, "lon": 126.983498,
     "desc": "한옥이 모여 있는 전통 마을, 골목 산책 추천."},
    {"name": "인사동 (Insadong)", "lat": 37.573, "lon": 126.986, 
     "desc": "전통 공예 & 기념품 골목, 찻집과 갤러리."},
    {"name": "명동 (Myeong-dong)", "lat": 37.564, "lon": 126.985,
     "desc": "쇼핑과 스트리트푸드의 중심지."},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.5669, "lon": 127.0094,
     "desc": "자하 하디드가 설계한 미래형 디자인 랜드마크."},
    {"name": "홍대 (Hongdae / Hongik University area)", "lat": 37.55528, "lon": 126.92333,
     "desc": "젊음의 거리, 버스킹과 카페, 밤문화."},
    {"name": "롯데월드타워 (Lotte World Tower & Seoul Sky)", "lat": 37.511234, "lon": 127.09803,
     "desc": "초고층 전망대와 쇼핑몰 — 잠실 지역."},
    {"name": "남대문시장 (Namdaemun Market)", "lat": 37.5557, "lon": 126.9768,
     "desc": "전통 재래시장 — 길거리 음식과 저렴한 쇼핑."}
]

# 지도 중심 설정 (평균 좌표)
avg_lat = sum(p["lat"] for p in PLACES) / len(PLACES)
avg_lon = sum(p["lon"] for p in PLACES) / len(PLACES)

# Folium 지도 생성
m = folium.Map(location=[avg_lat, avg_lon], zoom_start=12)

# 마커 추가
for i, place in enumerate(PLACES, start=1):
    popup_html = f"<b>{i}. {place['name']}</b><br/>{place['desc']}"
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=popup_html,
        tooltip=f"{i}. {place['name']}"
    ).add_to(m)

# --- Streamlit 출력 (시작하자마자 지도 표시) ---
st.title("🗺️ 오기구인이 좋아하는 서울 관광지 TOP10")

# 바로 지도 출력
st_folium(m, width=1200, height=700)

# --- 사이드바 ---
st.sidebar.title("목록 & 코드 다운로드")
st.sidebar.write("오기구인의 TOP10 장소:")
for i, p in enumerate(PLACES, start=1):
    st.sidebar.markdown(f"**{i}. {p['name']}**  \n{p['desc']}")

# 코드 보기 / 다운로드 버튼
st.sidebar.markdown("---")
st.sidebar.subheader("코드 & requirements.txt")

# main.py 코드 표시 및 다운로드
with open(__file__, "r", encoding="utf-8") as f:
    app_code = f.read()
st.sidebar.download_button("📄 main.py 다운로드", data=app_code, file_name="main.py")

# requirements.txt 표시 및 다운로드
requirements_txt = """streamlit
folium
streamlit-folium
"""
st.sidebar.download_button("🧾 requirements.txt 다운로드", data=requirements_txt, file_name="requirements.txt")

