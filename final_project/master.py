#!/usr/bin/env python3
import os
import pandas as pd
from matplotlib import pyplot as plt
pd.set_option('max_columns', None)

# make sure im in the right dir
os.chdir("/Users/brianmiller/Desktop/DU_COMP3006/final_project")

# read in data
df_7am = pd.read_excel("7am_googlemaps_data.xlsx")
df_8am = pd.read_excel("8am_googlemaps_data.xlsx")

# combine the dataframes
df = pd.concat([df_7am, df_8am]) 

# extract the date and time as separate columns
df['datetime_utc'] = pd.to_datetime(df['datetime_utc'])  # convert the 'datetime_utc' column to pandas datetime format
df['date'] = df['datetime_utc'].dt.date
df['time'] = df['datetime_utc'].dt.time
df['date'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['date'].dt.day_name()

# set the row names to be a specific column, implace makes the change permanent
# df.set_index('date', inplace=True)

# subset the df to the columns we will analyze, rename columns
df = df[['duration(minutes)', 'duration_min(minutes)', 'duration_max(minutes)', 'time', 'day_of_week', 'date', 'datetime_utc']]
df.rename(columns={"duration(minutes)": "eta", "duration_min(minutes)": "eta_min", "duration_max(minutes)": "eta_max", "datetime_utc":'datetime'}, inplace=True)

# subset to 2017
mask = (df['date'] >= '2018-01-01') & (df['date'] <= '2018-12-31')
df = df.loc[mask]
print(df)

# generate scatterplot
groups = df.groupby("time")
for name, group in groups:
    plt.plot(group["date"], group["eta_max"], marker="o", linestyle="", label=name)
plt.legend()
plt.show()