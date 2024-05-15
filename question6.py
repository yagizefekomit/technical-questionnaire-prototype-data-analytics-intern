#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:33:13 2024

@author: yagizefekomit
"""

#importing libraries
import pandas as pd
import numpy as np
import statistics

df = pd.read_csv('country_vaccination_stats.csv')
df2 = pd.read_csv('country_vac_stats_filled.csv') #it's working with the created csv file at previous python file.

countries = []
len_df2 = len(df2)
# taking every country names
for i in range(len_df2):
    if not(df2.iloc[i,0] in  countries):
        countries.append(df.iloc[i, 0])
        
        
# separating the countries to calculate median
start = 0
i = 0
medians = []


for country in countries:
    isEqual = True
    while(isEqual):
        if(i == len_df2):
            median = statistics.median(df2.iloc[start:(i-1), 2])

            medians.append([country, median])
            isEqual = False
            break

        elif((df2.iloc[i,0] != country)):
            
            median = statistics.median(df2.iloc[start:i, 2])

            medians.append([country, median])
            start = i
            isEqual = False
            break

        else:
            i += 1

df_medians = pd.DataFrame(medians, columns=['country', 'median'])
df_medians_sorted = df_medians.sort_values(by='median', ascending=False)

print("top 3 countries with highest median daily vaccinations number are: ")
for i in range(3):
    print(f'{i + 1}. {df_medians_sorted.iloc[i,0]}, and the median: {df_medians_sorted.iloc[i,1]}')


