#!/usr/bin/env python3
"""
Script for sentiment analysis
"""

import pandas as pd
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

pd.set_option('max_columns', None)
pd.set_option('max_rows', 10)

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

from nltk.tokenize import word_tokenize
from nltk import FreqDist

lower_full_text = full_text.lower()
word_tokens = word_tokenize(lower_full_text)
tokens = list()
for word in word_tokens:
    if word.isalpha() and word not in stop_words:
        tokens.append(word)
token_dist = FreqDist(tokens)
dist = pd.DataFrame(token_dist.most_common(20),columns=['Word', 'Frequency'])

