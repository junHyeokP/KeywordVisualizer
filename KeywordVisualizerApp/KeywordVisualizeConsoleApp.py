import mylib.myTextMining as tm
from konlpy.tag import Okt

def keywordVisualize(filename) :

    # 코퍼스 로딩
    #input_filename = "daum_movie_review.csv"
    input_filename = filename
    corpus_list = tm.load_corpus_from_csv("./KeywordVisualizerApp/data/" + input_filename, "title")
    print(corpus_list[:10])

    # 빈도수 추출
    my_tokenizer = Okt().pos
    my_tags = ['Nouns', 'Adjective', 'Verbs']

    #my_tokenizer = komoran().pos
    #my_tags = ['NNG', 'NNP', 'VV']
    my_stopwords = ['하며', '입', '하고', '로써', '하여', '애', '제', '한다', '그', '이', '할', '정', '수']

    counter = tm.analyze_word_freq(corpus_list, my_tokenizer, my_tags, my_stopwords)

    #print(list(counter.items())[:20])
    #tm.visualize_barchart(counter, "다음 영화 리뷰 키워드 분석", "빈도수", "키워드")
    #tm.visualize_wordcloud(counter)

    return counter
