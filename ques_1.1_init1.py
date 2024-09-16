import pandas as pd
import glob as gl

csv_files = gl.glob('*.csv')

combined_df = pd.DataFrame()

for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    combined_df = pd.concat([combined_df, df])

# print(combined_df)
print(list(combined_df))


combined_df.to_csv('single.txt', sep=',', index=False)

# Github link https://github.com/Shantanu-Barua/HIT137_asgn2.git #