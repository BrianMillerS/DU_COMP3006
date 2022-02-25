#!/usr/bin/env python3
"""
Script for initial exploratory data analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('max_columns', None)
pd.set_option('max_rows', None)

VD_yelp_reviews = pd.read_pickle('VD_yelp_reviews.pickle')
BD_yelp_reviews = pd.read_pickle('BD_yelp_reviews.pickle')

# make sure that the date is the index
BD_yelp_reviews = BD_yelp_reviews.set_index('date')
VD_yelp_reviews = VD_yelp_reviews.set_index('date')


# PLOT: line graph, reviews per month
plt.plot(BD_yelp_reviews['text'].resample('Q').count(), label='Blue Star Donuts')
plt.plot(VD_yelp_reviews['text'].resample('Q').count(), label = 'Voodoo Donuts')
plt.xlabel('Year')
plt.ylabel('Number of reviews')
plt.legend(loc="upper left")
plt.title('Number of Reviews per Quarter')
plt.show()


# PLOT: percent of review ratings
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


# PLOT: customer reviews over time
plt.plot(BD_yelp_reviews['stars'].resample('Q').mean(), label='Blue Star Donuts')
plt.plot(VD_yelp_reviews['stars'].resample('Q').mean(), label = 'Voodoo Donuts')
plt.xlabel('Year')
plt.ylabel('Rating')
plt.title('Average Quarterly Customer Rating')
plt.legend(loc="upper right")
plt.ylim(3,5.5)
plt.show()