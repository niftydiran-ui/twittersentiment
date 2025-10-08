from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout

def build_lstm(vocab_size, embedding_dim=100, input_length=100):
    model = Sequential([
        Embedding(vocab_size, embedding_dim, input_length=input_length),
        LSTM(128, dropout=0.2, recurrent_dropout=0.2),
        Dense(3, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
