#!/usr/bin/env python3

"""
This script extracts the relevant reviews that will be needed for the analysis.

The whole Yelp review .JSON file is about 7GB (and has 8 Million reviews), thus
in order to conserve RAM I am doing the subsetting first and extracting only the 
reviews that I need.

The 7GB files was split into 5 smaller files in order for this querry process to work. 
Each piece is: loaded, querried, and output saved

The final result of this script is two .pickle files. Each pickle file contains the reviews
BD_yelp_reviews.pickle
BD_yelp_reviews.pickle
"""

import os
import pandas as pd
from IPython.display import display
# pd.set_option('max_columns', None)
# pd.set_option('max_rows', None)

# make sure im in the right dir
os.chdir("/Users/brianmiller/Desktop/DU_COMP3006/final_project")

# read in business name data
yelp_companys = pd.read_json('yelp_dataset/yelp_academic_dataset_business.json', lines=True)

# subset to get the bussiness IDs for the two companies
# VD = Voodoo Donuts
# BD = Blue star Donuts
querry_VD = yelp_companys.loc[(yelp_companys['name']=='Voodoo Doughnut - Old Town')|(yelp_companys['name']=='Voodoo Doughnut - Davis'),['name','address','city','stars','review_count','business_id']]
querry_BD = yelp_companys.loc[(yelp_companys['name']=='Blue Star Donuts'),['name','address','city','stars','review_count','business_id']]

# extract the relevant business IDs
VD_bus_IDs = querry_VD['business_id'].to_list()
BD_bus_IDs = querry_BD['business_id'].to_list()

# loop through all .json files
yelp_review_files = ["yelp_dataset/split_reviews01.json", "yelp_dataset/split_reviews02.json", "yelp_dataset/split_reviews03.json", "yelp_dataset/split_reviews04.json", "yelp_dataset/split_reviews05.json"]
VD_chunk_outputs = []
BD_chunk_outputs = []

# loop through all the files and extract the relevant reviews, append them to a list of outputs
for file in yelp_review_files:
    # load the data
    yelp_reviews_chunk = pd.read_json(file, lines=True)
    # extract the relevant reviews for those businesses
    VD_yelp_reviews_chunk = yelp_reviews_chunk[yelp_reviews_chunk['business_id'].isin(VD_bus_IDs)]
    BD_yelp_reviews_chunk = yelp_reviews_chunk[yelp_reviews_chunk['business_id'].isin(BD_bus_IDs)]

    # append outputs
    VD_chunk_outputs.append(VD_yelp_reviews_chunk)
    BD_chunk_outputs.append(BD_yelp_reviews_chunk)

# combine the outputs from all of the chunks
VD_yelp_reviews = pd.concat(VD_chunk_outputs)
BD_yelp_reviews = pd.concat(BD_chunk_outputs)

# check the dimensions of the final dfs
print(VD_yelp_reviews.shape)
print(BD_yelp_reviews.shape)

# save pandas dfs as pickle files
VD_yelp_reviews.to_pickle(path='VD_yelp_reviews.pickle')
BD_yelp_reviews.to_pickle(path='BD_yelp_reviews.pickle')

print("Script Complete.")