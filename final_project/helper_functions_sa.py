#!/usr/bin/env python3
"""
Helper script that has the functions needed to perform sentiment analyis on Yelp review data

Author: Brian Miller (DU ID: 873601817)
Date: 03/11/2022
"""

import re
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer


def generate_wordcloud(reviews_str, stopwords):
    """Summary:
    Returns a matplotlib figure as a variable

    Args:
        reviews_str (str): single str with all the reviews text
        stopwords (list): list of strings, contains words to ommit
    """
    word_cloud = WordCloud(background_color='white', stopwords = stopwords).generate(reviews_str)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    
    return plt


def compute_n_bigrams(df, stopwords, n_bigrams):
    """ 
    Returns a pandas df of the top n bigrams from the
    yelp reviews provided.

    Args:
        df (pandas.df): pandas df of the yelp reviews
        stopwords (list): list of strings, contains words to ommit
        n_bigrams (int): number of bigrams to return
    """
    vect = CountVectorizer(stop_words=stopwords, ngram_range=(2,2))  # set up vector container
    bigrams = vect.fit_transform(df['text'])  # propagate the container or bigrams
    bigram_df = pd.DataFrame(bigrams.toarray(), columns=vect.get_feature_names())
    bigram_freq = pd.DataFrame(bigram_df.sum(axis=0)).reset_index()  # perform the counting
    bigram_freq.columns = ['bigram', 'freq']
    bigram_freq = bigram_freq.sort_values(by='freq', ascending=False)
    bigram_freq = bigram_freq.head(n_bigrams)
    
    return bigram_freq


def extract_related_words(full_text, target_word, n_results, stopwords):
    """ 
    Returns the top 10 related words from the full_text corpus. Given the corpus and
    a target word or words this function tokenizes all words and uses a 'skip-gram' neural network 
    framework to determine the probability of word relations for a given word pair. Words can be considered 
    pair if they are at max 10 words apart, 2000 unique predicted words is the search space, and words
    from the corpus that are stop words or have a frequency of 1 are dropped.
    
    Args:
        full_text (ste): concatinated single string of all reviews
        target_word (list): list of string(s) to be used as the target words
        n_results (int): number of n top results to display
        stopwords (list): list of stop words to exclude

    Returns:
        None: results are simply printed
    """

    # tokenize the full_text, each token will be a lowercase word
    reviews = sent_tokenize(full_text)
    token_clean = list()
    
    # get tokens from each review
    for review in reviews:
        eng_word = re.findall(r'[A-Za-z\-]+', review)  # see below...
        # drop all numbers
        # drop non-english letters
        # capitalization does not matter, everything will be connverted to lower anyway
        token_clean.append([i.lower() for i in eng_word if i.lower() not in stopwords])  # drop any stop words

    # call the unsupervised neural net, train the model
    model_ted = Word2Vec(sentences = token_clean, size = 2000, window = 10, min_count = 1, workers = 4, sg = 1)  # see below...
    # sentences = token_clean: which words to use as inputs
    # size = 2000: how many unique predicted words to consider (unique word associations), more words takes longer to compute
    # window = 10: the max distance allowed between the target word and the predicted word
    # min_count = 1: ignore all words with total frequency lower than this
    # workers = 4: how many worker threads to train the model
    # sg = 1: use 'skip-gram' framework (1), rather than the default CBOW: continuous bag of words model (0)
    results = model_ted.predict_output_word(target_word, topn = n_results)
    
    # print the results
    print("Target Word(s): {}".format(target_word))
    out_list = []
    for i in results:
        out_list.append(i[0])
    print("Related Words: {}".format(out_list))
