# main.py
import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="오기구인의 서울 TOP10", layout="wide")

st.title("오기구인이 좋아하는 서울 주요 관광지 — TOP 10 🧭")
st.write("Folium 지도로 서울의 주요 관광지 10곳을 표시합니다. (즐겨찾기: 오기구인)")

# 장소 데이터: 이름, 위도, 경도, 간단 설명
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

# 지도 중심: 서울 시청(대략) 또는 PLACES 평균으로 계산
avg_lat = sum(p["lat"] for p in PLACES) / len(PLACES)
avg_lon = sum(p["lon"] for p in PLACES) / len(PLACES)

m = folium.Map(location=[avg_lat, avg_lon], zoom_start=12)

# 마커 추가
for i, place in enumerate(PLACES, start=1):
    popup_html = f"<b>{i}. {place['name']}</b><br/>{place['desc']}"
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=popup_html,
        tooltip=f"{i}. {place['name']}"
    ).add_to(m)

# 클러스터 필요 시 주석 해제하고 import MarkerCluster 사용 가능
# from folium.plugins import MarkerCluster
# cluster = MarkerCluster().add_to(m)
# for place in PLACES:
#     folium.Marker(...).add_to(cluster)

st.subheader("지도 미리보기")
st.write("마커를 클릭하면 상세 정보를 볼 수 있어요.")
