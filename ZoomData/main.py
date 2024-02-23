

import pandas as pd
import re

reg = "[0-9]*\d{5}$"
df = pd.read_csv('dbda.csv')

for index, row in df.iterrows():
    s = str(re.findall(reg, row['Name (Original Name)']))
    df.at[index, 'id'] = s

print(df)

