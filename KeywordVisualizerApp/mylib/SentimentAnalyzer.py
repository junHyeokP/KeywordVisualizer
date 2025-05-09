import joblib
from konlpy.tag import Okt
import tensorflow as tf
import numpy as np
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences


# 하나(ex: 알라딘 책 리뷰)를 기준으로 여러 사이트의 리뷰를 데이터로 삼아서 분석할 것

# windows 환경에서 tensorflow와 streamlit은 공존하기 힘들다는 걸 알았다.
# pip로 tensorflow와 streamlit을 깔았더니
# 두 라이브러리 모두 protobuf에 의존적인 라이브러리들이라 서로 원하는 버전이 달라 protobuf를 다운그레이드하면 하나가 요구하는 protobuf 버전이 안맞는 등 모두의 요구사항을 맞출 수 없는 모순이 생겼다.
# 단순하게 말하자면, OS의 문제다.
# Linux 환경을 기준으로 만들어져서 그렇다. 
# 이 문제 때문에 해결 방법을 탐색 하느라 약 1시간 30분을 날려먹었다. 
# https://alwaysmoveforward.tistory.com/37 <- 참고 블로그

# 현재 이민수씨가 보내준 가상환경으로 streamlit을 실행시키는 것엔 성공했다(전엔 실행 전에 오류가 뜨거나 창은 뜨는데 그자리에서 오류가 뜨는 등 버전 충돌때문에 안됐었다).

# 딥러닝 모델 불러오는 코드 

class SentimentAnalyzer_DeepL :
    def __init__(self, toeknizer_file, sa_model_file) :
            self.tokenizer = joblib.load(tokenizer_file)
            self.model = load_model(sa_model_file)
            self.ktokenizer = Okt().morphs

    def sentiment_analysis(self, review):
        morphs = [word for word in self.ktokenizer(review)] # 형태소 분석
        sequences = self.tokenizer.texts_to_sequences([morphs]) # Integer Encoding
        X = pad_sequences(sequences, maxlen=self.model.input_shape[1]) # Padding
        preds = self.model.predict(X)
        label = ['부정', '긍정']
        max_index = np.argmax(preds[0])
        result = label[max_index]
        return result, preds[0][max_index]



#class SentimentAnalyzer2_ML :
#    def my_tokenizer(self, text) :
#        t = Okt()
#        my_tags = {'Nouns', 'Verb', 'Adjective'} 
#        return [word for word, tag in t.pos(text) if tag in my_tags]
    
#    def sentiment_analysis(self, review):
#        tokens = self.my_tokenizer(review)
#        tokens = " ".join(tokens)
#        print(tokens)
        # 특징 벡터 추출
#        #X = tv.transform(tokens)
#        X = tv.transform([tokens])
#        
        # 예측
#        prediction = perc.predict(X)
        
        # 예측 결과 출력
#        result = '긍정' if prediction >= 0.5 else '부정'
#        return result

    
