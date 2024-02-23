import pandas as pd


df = pd.concat(
    map(pd.read_csv, ['Python-day1.csv', 'Python-day2.csv','Python-day3.csv', 'Python-day4.csv',
                      'Python-day5.csv', 'Python-day6.csv','Python-day7.csv', 'Python-day8.csv',
                      'Python-day9.csv', 'Python-day10.csv','Python-day11.csv', 'Python-day12.csv',
                      'Python-day13.csv']), ignore_index=True)


df.to_csv('py.csv', index=False)

print("Merged data saved as 'merged_data.csv'")
