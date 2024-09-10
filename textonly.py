import pandas as pd
import glob as gl

# Get all CSV files in the directory
csv_files = gl.glob('*.csv')

combined_df = pd.DataFrame()

# Combine all CSV files into one DataFrame
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    combined_df = pd.concat([combined_df, df])


column_to_save = combined_df['SHORT-TEXT'] 

# Save the selected column to a .txt file
column_to_save.to_csv('textonly.txt', sep=',', index=False, header=False)
