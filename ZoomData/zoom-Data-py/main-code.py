import os
import re
import pathlib
import pandas as pd
reg="[0-9]*\d{5}$"

# directory = r'D:\Project_Hakethon\hack23\csv\data'
directory=os.path.join( "D:\\", "Project_Hakethon", "hack23","csv","data" )

file_names = []

if os.path.exists(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_names.append(filename)
for name in file_names:
    # print(name)
    data_path = os.path.join(directory, name)
    table1 = pd.read_csv(data_path, nrows=1, skiprows=0)
    row_index = 0
    column2 = 'Topic'
    column2_data = table1.loc[row_index, [column2]]
    courseName=column2_data[column2]
    df = pd.read_csv(data_path,skiprows=3)
    for index, row in df.iterrows():
        matches = re.findall(reg, row['Name (Original Name)'])
        if matches:
            df.at[index, 'id'] = matches[0]
            df.at[index, 'courseName'] = courseName
        else:
            df.at[index, 'id'] = None
            df.at[index, 'courseName'] = None
df.dropna(subset=['id'], inplace=True)
df.drop(df.columns[[0,1,4,5,6,7]],axis=1,inplace=True)
print(df)
# df.to_csv("new_data1.csv",index=False)



