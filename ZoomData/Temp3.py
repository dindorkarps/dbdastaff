import pandas as pd

# merging two csv files
df = pd.concat(
    map(pd.read_csv, ['CJ.csv', 'PY.csv']), ignore_index=True)
print(df)