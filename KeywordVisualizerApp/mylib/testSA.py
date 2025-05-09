import SentimentAnalyzer as sa

#sa.SentimentAnalyzer()

sa_tokenizer_file = "./model/movie_sa_tokenizer.pkl" # 최근 저장 모델
sa_model_file = "./model/movie_sa_best_model.keras" # 최종 모델

movie_sa = sa.SentimentAnalyzer_DeepL(sa_tokenizer_file, sa_model_file)

reviews = [
    '이 영화 개꿀잼 ㅋㅋㅋ',
    '하품만 나온다',
    '이 영화 핵노잼 ㅠㅠ',
    '이딴게 영화냐 ㅉㅉ',
    '와 개쩐다',
    '감독 뭐하는 놈이냐',
    '정말 세계관 최강자들의 영화다'
]

for review in reviews:
    result, prob = movie_sa.sentiment_analysis(review)
    print(f'{review} --> {result}({prob:.2f})\n')