import streamlit as st
st.title('프린세스 메이커')
a=st.text_input('부부가 공에 올라가면?')
st.selectbox('닭이 옷사러 가서 하는말은?',['꼭끼오'}
if st.button('인사말 생성'):
  st.write(a+'쁑')
