import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
from collections import Counter

def count_unique_tokens_streaming(input_file, model_name, chunk_size=4096):
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    token_counts = Counter()

    with open(input_file, 'r', encoding='utf-8') as f:
        for chunk in iter(lambda: f.read(chunk_size), ''):
            tokens = tokenizer.tokenize(chunk)
            token_counts.update(tokens)

    return token_counts.most_common(30)

# Usage
top_30_tokens = count_unique_tokens_streaming('textonly.txt', 'distilbert-base-uncased')
print(top_30_tokens)
