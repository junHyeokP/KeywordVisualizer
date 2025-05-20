import streamlit as st
import mylib.myTextMining as mt

def findDataColumn(csvfile, column):
    df = pd.read_csv(csvfile)
    st.dataframe(df[[column]].dropna())

def csvVisualizer(csvfile, wordcloud_capacity, bar_capacity, show_bar, show_wordcloud):
    counter = mt.analyze_word_freq(
        mt.load_corpus_from_csv(csvfile.name, "review"),
        tokenizer=mt.get_tokenizer(),
        tags=["Noun", "Adjective"],
        stopwords=mt.get_default_stopwords()
    )
    if show_bar:
        mt.visualize_barchart(counter, top_n=bar_capacity)
    if show_wordcloud:
        mt.visualize_wordcloud(counter, top_n=wordcloud_capacity)
