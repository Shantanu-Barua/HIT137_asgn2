import os
import pandas as pd

# Set the path to the folder containing CSV files
csv_folder = 'path_to_your_unzipped_folder'
output_file = 'combined_text.txt'

# Collect text from all CSV files
all_texts = []

for file in os.listdir(csv_folder):
    if file.endswith('.csv'):
        file_path = os.path.join(csv_folder, file)
        df = pd.read_csv(file_path)

        # Assuming the column with large texts is named 'text'
        all_texts.extend(df['text'].tolist())

# Write to a single text file
with open(output_file, 'w', encoding='utf-8') as f:
    for text in all_texts:
        f.write(text + '\n')

#----fetch .csv---