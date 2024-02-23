import pandas as pd
import re

reg = "[0-9]*\d{5}$"
df = pd.read_csv('dbda.csv')

for index, row in df.iterrows():
    matches = re.findall(reg, row['Name (Original Name)'])
    if matches:
        df.at[index, 'id'] = matches[0]
    else:
        df.at[index, 'id'] = None


df.dropna(subset=['id'], inplace=True)
df.drop(df.columns[[0,1,4,5,6,7]],axis=1,inplace=True)
print(df)

