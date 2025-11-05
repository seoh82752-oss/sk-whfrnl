import streamlit as st
st.title('프린세스 메이커')
a=st.text_input('부부가 공에 올라가면?')
if st.button('인사말 생성'):
  st.write(a+'쁑')
