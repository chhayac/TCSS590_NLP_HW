
# coding: utf-8

# In[1]:


#please update the filepath
#filepath = 'HW1\\combined_file.txt'



import nltk
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import sys


# In[11]:


def get_tokens(filepath):
    stopset = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')
    text = open(filepath, 'r').read()
    tokens = tokenizer.tokenize(text.lower())
    tokens = [token for token in tokens if token != 'br']
    tokens = [w for w in tokens if not w in stopset]
    return tokens


# In[18]:


def get_bigrams(filepath):
    tokens = get_tokens(filepath)
    bigms = nltk.bigrams(tokens)
    return list(bigms)


# In[17]:


def get_trigrams(filepath):
    tokens = get_tokens(filepath)
    trigms = nltk.trigrams(tokens)
    return list(trigms)


# In[72]:


def build_trigram_model(filepath):
    model = defaultdict(lambda: defaultdict(lambda: 0))
    trigrams = get_trigrams(filepath)
    for w1, w2, w3 in trigrams:
        model[(w1, w2)][w3] += 1
        
    for bigram in model:
        total_count = float(sum(model[bigram].values()))
        for third_word in model[bigram]:
            model[bigram][third_word] = model[bigram][third_word] / total_count
    return model


# In[84]:


def get_unique_token_count(filepath):
    return len(set(get_tokens(filepath)))


# In[87]:


def get_third_word_prob(filepath, w1, w2, w3):
    model = build_trigram_model(filepath)
    unique_token_count = get_unique_token_count(filepath)
    total_count = float(sum(model[(w1, w2)].values()))
    model[w1, w2][w3] += 1
    return model[w1, w2][w3] / (total_count + unique_token_count)



def main():
    if len(sys.argv) < 5:
        print("Usage: <script> <filepath> <word1> <word2> <word3>")
        sys.exit(0)
    
    filepath = sys.argv[1]
    w1 = sys.argv[2]
    w2 = sys.argv[3]
    w3 = sys.argv[4]

    print("Probability of [", w3, "] appearing after [", w1, "] and [", w2, "] is",  get_third_word_prob(filepath, w1, w2, w3))
 
if __name__ == "__main__":
    main()



