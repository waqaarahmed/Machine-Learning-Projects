import pickle
import random
import json
import nltk
#nltk.download('punkt')
#nltk.download('wordnet')

import numpy as np
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()
intent = json.loads(open('intent.json').read())

words = []
classes = []
documents = []
letter_ignore = ['?', ',', '!', '.']

for i in intent['intent']:
    for p in i['pattern']:
        word_list = nltk.word_tokenize(p)
        words.extend(word_list)
        documents.append((word_list, i['tags']))
        if i['tags'] not in classes:
            classes.append(i['tags'])

words = [lemmatizer.lemmatize(w) for w in words if w not in letter_ignore]
words = sorted(set(words))
classes = sorted(set(classes))
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(words, open('classes.pkl', 'wb'))