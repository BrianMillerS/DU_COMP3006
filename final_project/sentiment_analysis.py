#!/usr/bin/env python3
"""
Script for sentiment analysis
Author: Brian Miller (DU ID: 873601817)
Date: 
"""

import re
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import FreqDist
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import CountVectorizer

# pandas options
pd.set_option('max_columns', None)
pd.set_option('max_rows', None)

# load the data
VD_yelp_reviews = pd.read_pickle('VD_yelp_reviews.pickle')
BD_yelp_reviews = pd.read_pickle('BD_yelp_reviews.pickle')

# make sure that the date is the index
VD_yelp_reviews = VD_yelp_reviews.set_index('date')
BD_yelp_reviews = BD_yelp_reviews.set_index('date')

# subset to just the reviews that were in english
# print("Language counts for Blue Star:")
# print(BD_yelp_reviews.language.value_counts())
# print("Language counts for Voodoo:")
# print(VD_yelp_reviews.language.value_counts())
VD_yelp_reviews = VD_yelp_reviews[VD_yelp_reviews['language'] == 'en']
BD_yelp_reviews = BD_yelp_reviews[BD_yelp_reviews['language'] == 'en']

# load stopwords from the nltk.corpus
my_file = open("stopwords/english", "r")
stop_words = my_file.read().splitlines()

# make word clouds for both companies
full_text = ' '.join(BD_yelp_reviews['text'])
cloud_no_stopword = WordCloud(background_color='white', stopwords = stop_words).generate(full_text)
plt.imshow(cloud_no_stopword, interpolation='bilinear')
plt.axis('off')
plt.show()

# plot the 20 most common words
lower_full_text = full_text.lower()
word_tokens = word_tokenize(lower_full_text)
tokens = list()
for word in word_tokens:
    if word.isalpha() and word not in stop_words:
        tokens.append(word)
token_dist = FreqDist(tokens)
dist = pd.DataFrame(token_dist.most_common(20),columns=['Word', 'Frequency'])

vect = CountVectorizer(stop_words=stop_words, ngram_range=(2,2))
bigrams = vect.fit_transform(VD_yelp_reviews['text'])
bigram_df = pd.DataFrame(bigrams.toarray(), columns=vect.get_feature_names())
bigram_frequency = pd.DataFrame(bigram_df.sum(axis=0)).reset_index()
bigram_frequency.columns = ['bigram', 'frequency']
bigram_frequency = bigram_frequency.sort_values(by='frequency', ascending=False).head(20)

# only grab the good reviews (4 or 5 stars)
DF_good_reviews = BD_yelp_reviews[BD_yelp_reviews['stars'] > 3]
good_reviews_text = ' '.join(DF_good_reviews['text'])

# split the long string into sentences
sentences_good = sent_tokenize(good_reviews_text)
good_token_clean = list()
# get tokens for each sentence
for sentence in sentences_good:
    eng_word = re.findall(r'[A-Za-z\-]+', sentence)
    good_token_clean.append([i.lower() for i in eng_word if i.lower() not in stop_words])

# call the NN algo
model_ted = Word2Vec(sentences=good_token_clean, size=500, window=10, min_count=1, workers=4, sg=0)
res = model_ted.predict_output_word(['donuts'], topn=10)
print(res)