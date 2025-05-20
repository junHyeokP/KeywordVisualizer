import pandas as pd
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from sklearn.model_selection import train_test_split

def train_model(csv_path, model_path):
    df = pd.read_csv(csv_path)
    texts = df["review"].astype(str).tolist()
    labels = df["label"].tolist()  # 라벨은 0(부정), 1(긍정)

    tokenizer = Tokenizer(num_words=10000)
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, maxlen=100)

    X_train, X_test, y_train, y_test = train_test_split(padded, labels, test_size=0.2)

    model = Sequential()
    model.add(Embedding(10000, 128))
    model.add(LSTM(64))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))
    model.save(model_path)
