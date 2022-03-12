#!/usr/bin/env python3
"""
Script for exploratory data analysis of Yelp Reviews
Author: Brian Miller (DU ID: 873601817)
Date: 03/11/2022

USAGE:
python3 eda.py
"""

import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# read in data
VD_yelp_reviews = pd.read_pickle('VD_yelp_reviews.pickle')
BD_yelp_reviews = pd.read_pickle('BD_yelp_reviews.pickle')

# make sure that the date is the index
BD_yelp_reviews = BD_yelp_reviews.set_index('date')
VD_yelp_reviews = VD_yelp_reviews.set_index('date')

# SUMMARY STATISTICS:
print("Number of reviews for Voodoo Donuts: {}".format(VD_yelp_reviews.shape[0]))
print("Number of reviews for Blue Star Donuts: {}".format(BD_yelp_reviews.shape[0]))
print("Number of unique restaurants for Voodoo Donuts: {}".format(len(VD_yelp_reviews['business_id'].value_counts())))
print("Number of unqiue restaurants for Blue Star Donuts: {}".format(len(BD_yelp_reviews['business_id'].value_counts())))

print("\nColumns in the pandas df:")
print(list(VD_yelp_reviews.columns))

print("\nExample: First two rows of Voodoo Donuts reviews:")
print(VD_yelp_reviews.head(2))

# PLOT: line graph, number of reviews per quarter
plt.plot(BD_yelp_reviews['text'].resample('Q').count(), label='Blue Star Donuts')
plt.plot(VD_yelp_reviews['text'].resample('Q').count(), label = 'Voodoo Donuts')
plt.xlabel('Year')
plt.ylabel('Number of reviews')
plt.legend(loc="upper left")
plt.title('Number of Reviews per Quarter')
plt.show()


# PLOT: bar chart, distribution of star ratings per company
star_counts_df = pd.DataFrame()
star_counts_df['VD'] = VD_yelp_reviews['stars'].value_counts(normalize=True) * 100  # get the star counts
star_counts_df['BD'] = BD_yelp_reviews['stars'].value_counts(normalize=True) * 100
star_counts_df = star_counts_df.reindex([5,4,3,2,1])  # order the star counts columns
star_counts_df['stars'] = star_counts_df.index
# plot
star_counts_df.plot(x="stars", y=["BD", "VD"], kind="bar",figsize=(9,8))
plt.title('Distribution of Customer Ratings')
plt.xlabel('Rating')
plt.ylabel('Percent')
plt.xticks(rotation=0)
plt.legend(labels=["Blue Star Donuts",'Voodoo Donuts'])
plt.show()


# PLOT: line graph, average quarterly customer star rating
plt.plot(BD_yelp_reviews['stars'].resample('Q').mean(), label='Blue Star Donuts')
plt.plot(VD_yelp_reviews['stars'].resample('Q').mean(), label = 'Voodoo Donuts')
plt.xlabel('Year')
plt.ylabel('Rating')
plt.title('Average Quarterly Customer Rating')
plt.legend(loc="upper right")
plt.ylim(3,5.5)
plt.show()


# PLOT: line graph, review sentiment score per quarter
# calculate sentiment score information for each review
analyzer = SentimentIntensityAnalyzer()
# compound is the outputed sentiment score [-1 to 1]: -1 is the most negative, 1 is the most positive, 0 is neutral
BD_yelp_reviews['sentiment_score'] = [analyzer.polarity_scores(x)['compound'] for x in BD_yelp_reviews['text']] 
VD_yelp_reviews['sentiment_score'] = [analyzer.polarity_scores(x)['compound'] for x in VD_yelp_reviews['text']]
# plot
plt.plot(BD_yelp_reviews['sentiment_score'].resample('Q').mean(), label='Blue Star Donuts')
plt.plot(VD_yelp_reviews['sentiment_score'].resample('Q').mean(), label = 'Voodoo Donuts')
plt.xlabel('Year')
plt.ylabel('Average Sentiment Score')
plt.legend(loc="upper left")
plt.title('Average Quarterly Sentiment Score')
plt.ylim(0.4,1)
plt.show()