import pandas as pd


df = pd.concat(
    map(pd.read_csv, ['CJ_O_13-day1.csv', 'CJ_O_13-day2.csv','CJ_O_13-day3.csv', 'CJ_O_13-day4.csv',
                      'CJ_O_13-day5.csv', 'CJ_O_13-day6.csv','CJ_O_13-day7.csv', 'CJ_O_13-day8.csv',
                      'CJ_O_13-day9.csv', 'CJ_O_13-day10.csv','CJ_O_13-day11.csv', 'CJ_O_13-day12.csv',
                      'CJ_O_13-day13.csv', 'CJ_O_13-day14.csv','CJ_O_13-day15.csv']), ignore_index=True)


df.to_csv('cj.csv', index=False)

print("Merged data saved as 'merged_data.csv'")
