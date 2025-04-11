import pandas as pd
import numpy as np
import streamlit as st
import KeywordVisualizeConsoleApp as kvc
import mylib.myTextMining as mt

@st.cache_data
def csvVisualizer(csvfile, wordcloud_capacity, bar_capacity, st_bar, st_wordcloud) :
    counter = kvc.keywordVisualize(csvfile.name)

    if st_bar is True :
        mt.visualize_barchart(counter, csvfile.name, '','', bar_capacity)   

    if st_wordcloud is True :
        mt.visualize_wordcloud(counter, wordcloud_capacity)    
    #return None

def findDataColumn(csvfile, st_column) :

    data_df = pd.read_csv(csvfile)

    st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)

def inputKeyword(keyword) :
    kvc.keywordVisualize(keyword)

   