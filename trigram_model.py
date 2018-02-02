
# coding: utf-8

import nltk
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import sys
import glob


def get_combined_text(dataset_path):
    text = b""
    dataset_path += "\\*\\*.txt"
    read_files = glob.glob(dataset_path)
    for f in read_files:
        with open(f, "rb") as infile:
            text += infile.read()
            text += b" "
    return text
            


def get_tokens(dataset_path):
    stopset = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')
    text = str(get_combined_text(dataset_path))
    tokens = tokenizer.tokenize(text.lower())
    tokens = [token for token in tokens if token != 'br']
    tokens = [w for w in tokens if not w in stopset]
    return tokens



def get_trigrams(tokens):
    trigms = nltk.trigrams(tokens)
    return list(trigms)


# In[72]:


def build_trigram_model(tokens):
    model = defaultdict(lambda: defaultdict(lambda: 0))
    trigrams = get_trigrams(tokens)
    for w1, w2, w3 in trigrams:
        model[(w1, w2)][w3] += 1
        
    for bigram in model:
        total_count = float(sum(model[bigram].values()))
        for third_word in model[bigram]:
            model[bigram][third_word] = model[bigram][third_word] / total_count
    return model



def get_unique_token_count(tokens):
    return len(set(tokens))


def get_third_word_prob(dataset_path, w1, w2, w3):
    tokens = get_tokens(dataset_path)
    model = build_trigram_model(tokens)
    unique_token_count = get_unique_token_count(tokens)
    total_count = float(sum(model[(w1, w2)].values()))
    model[w1, w2][w3] += 1
    return model[w1, w2][w3] / (total_count + unique_token_count)



def main():
    if len(sys.argv) < 5:
        print("Usage: <script> <dataset_path> <word1> <word2> <word3>")
        sys.exit(0)
    
    dataset_path = sys.argv[1]
    w1 = sys.argv[2]
    w2 = sys.argv[3]
    w3 = sys.argv[4]

    print("Probability of [", w3, "] appearing after [", w1, "] and [", w2, "] is",  get_third_word_prob(dataset_path, w1, w2, w3))
 
if __name__ == "__main__":
    main()



