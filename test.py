import sys
import os
from sklearn.feature_extraction.text import CountVectorizer
from nltk import ngrams
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
import heapq
import operator

data_directory_path = sys.argv[1]
positive_data_path = os.path.join(data_directory_path, 'pos')
negative_data_path = os.path.join(data_directory_path, 'neg')

stop_words = CountVectorizer(' ', stop_words='english').get_stop_words()

def get_text(directory_path):
    texts = []
    file_paths = os.listdir(directory_path)
    for file_path in file_paths:
        file = open(os.path.join(directory_path, file_path), 'r')
        text = file.read()
        file.close()
        texts.append(text)
    return ' '.join(texts)

def normalize_case(str):
    if (len(str) == 1):
        return str.upper() # stuff like I
    else:
        return str.lower()

def get_tokens(directory_path):
    stopset = set(stopwords.words('english'))
    text = get_text(directory_path)
    text = text.replace('<br>', '\n').replace('<br />', '\n').replace('<br/>', '\n').replace('U. S.', 'US')
    tokens = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+", text)
    tokens = [w for w in tokens if not w in stopset]
    return [normalize_case(token) for token in tokens if token not in stop_words and token != '.']

def get_ngrams(tokens, n):
    n_grams = ngrams(tokens, n)
    freq = {}
    for gram in n_grams:
        freq[gram] = (freq[gram] + 1) if gram in freq else 1

    return freq

def print_grams(s, grams):
    print(s)

    for i in range(len(grams)):
        gram = grams[i]
        print (gram[0], ': ', gram[1])


positive_tokens = get_tokens(positive_data_path)
negative_tokens = get_tokens(negative_data_path)
all_tokens = positive_tokens + negative_tokens

all_unigrams = get_ngrams(all_tokens, 1)
vocabulary_size = len(all_unigrams)
print ('Number of word tokens: ', sum(all_unigrams.values()))
print ('Number of unique words: ', vocabulary_size)

positive_bigrams = get_ngrams(positive_tokens, 2)
print_grams('Top 10 positive bigrams', heapq.nlargest(10, positive_bigrams.items(), key=operator.itemgetter(1)))

negative_bigrams = get_ngrams(negative_tokens, 2)
print_grams('Top 10 negative bigrams', heapq.nlargest(10, negative_bigrams.items(), key=operator.itemgetter(1)))

positive_trigrams = get_ngrams(positive_tokens, 3)
print_grams('Top 10 positive trigrams', heapq.nlargest(10, positive_trigrams.items(), key=operator.itemgetter(1)))

negative_trigrams = get_ngrams(negative_tokens, 3)
print_grams('Top 10 negative trigrams', heapq.nlargest(10, negative_trigrams.items(), key=operator.itemgetter(1)))

all_trigrams = get_ngrams(all_tokens, 3)
all_trigrams_number = sum(all_trigrams.values())

def calculate_probability(w1, w2, w3):
    n_w1 = normalize_case(w1)
    n_w2 = normalize_case(w2)
    n_w3 = normalize_case(w3)
    trigram = (n_w1, n_w2, n_w3)
    trigram_count = all_trigrams[trigram] if trigram in all_trigrams else 0
    return (trigram_count + 1) / (all_trigrams_number + vocabulary_size)

def print_probability(w1, w2, w3):
    print ((w1, w2, w3), ': ', calculate_probability(w1, w2, w3))

print_probability('hell', 'lot', 'better')
print_probability('SOUND', 'OF', 'MUSIC')
print_probability('I', 'highly', 'recommend')
print_probability('thoroughly', 'bored', 'looking')
print_probability('The', 'special', 'effects')
print_probability('ruben', 'santiago', 'hudson')
