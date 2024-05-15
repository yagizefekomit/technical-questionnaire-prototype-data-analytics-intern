# importing libraries
import pandas as pd
import numpy as np

# loading the dataset
df = pd.read_csv("country_vaccination_stats.csv")

#Finding missing values
is_null_values = df['daily_vaccinations'].isnull()
countries_has_missing_values = []

for i in range(len(df)):
    if(is_null_values[i] == True):
        the_row = df.loc[i]
        countries_has_missing_values.append(the_row['country'])

df1 = df.dropna(subset=['daily_vaccinations'])

# find the min_value for every country from dropna dataset
country_values = []

for country in countries_has_missing_values:
    min_value = max(df1['daily_vaccinations'])
    
    for i in range(len(df1)):
        x = df1.iloc[i,0]
        if(x == country):

            if(df1.iloc[i,2] < min_value):
                min_value = df1.iloc[i,2]
    
    country_values.append([country, min_value])

df_country_val = pd.DataFrame(country_values, columns=['country', 'min_value'])
#df_country_val.to_csv('countries_min_vals.csv', index=False)

for i in range(len(df)):
    if(np.isnan(df.iloc[i,2])):
        
        for j in range(len(df_country_val)):
            if(df.iloc[i,0] == df_country_val.iloc[j, 0]):
                df.iloc[i,2] = df_country_val.iloc[j,1]

# creating .csv file
df.to_csv('country_vac_stats_filled.csv', index=False)