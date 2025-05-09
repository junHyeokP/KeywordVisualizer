import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import mylib.STVisualizer as stv

csv_file = st.sidebar.file_uploader('파일선택')
/
st_column = st.sidebar.text_input('데이터가 있는 컬럼명')
st_btn = st.sidebar.button('데이터 파일 확인', (True))

if st_btn is True :
    stv.findDataColumn(csv_file, st_column)

#csv_file = st.file_uploader('파일선택')
#st.write(csv_file)

#st_keyword = st.text_input('검색', None, placeholder = '검색할 키워드를 입력해주세요.')
st.write("단어 빈도수 시각화") 


with st.sidebar.form('option') :
    
    st.write('설정')

    st_bar = st.checkbox('빈도수 그래프',(True))
    bar_capacity = st.slider('단어 수', 10, 50)

    st_wordcloud = st.checkbox('워드클라우드', (True))
    wordcloud_capacity = st.slider('단어 수', 20, 500)

    submitted = st.form_submit_button("분석시작", icon="🚨")

if submitted :
    data_load_state = st.text('교수님의 streamlit 강의가 필요했었는데...')
    if csv_file is None :
        data_load_state.text("분석할 파일을 탐지하지 못했습니다.")
    else :    
        stv.csvVisualizer(csv_file, wordcloud_capacity, bar_capacity, st_bar, st_wordcloud)
        data_load_state.text(f"분석이 완료되었습니다.")         