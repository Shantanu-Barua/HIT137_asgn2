import pandas as pd
from collections import Counter
import csv


def count_words(input_file, output_csv):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Count word occurrences
    words = text.split()
    word_counts = Counter(words)
    
    # Top 30 most common words
    top_30_words = word_counts.most_common(30)
    
    # Save csv
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Word', 'Count'])
        writer.writerows(top_30_words)

count_words('single.txt', 'top_30_comm_words.csv')

# Github link https://github.com/Shantanu-Barua/HIT137_asgn2.git 