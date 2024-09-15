from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

def extract_entities_biobert(input_file, model_name="dmis-lab/biobert-base-cased-v1.1", max_length=512):
    # Load the BioBERT tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)

    # Initialize the NER pipeline
    nlp_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

    # Read the input text
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Tokenize the text into chunks within the model's max length
    tokens = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=max_length, return_overflowing_tokens=True)

    diseases = []
    drugs = []

    # Process each chunk
    input_ids = tokens['input_ids']
    
    # Run NER pipeline on each chunk
    for i in range(len(input_ids)):
        chunk_input = tokenizer.decode(input_ids[i], skip_special_tokens=True)
        entities = nlp_pipeline(chunk_input)

        # Process entities and merge subword tokens if necessary
        for ent in entities:
            word = ent['word']
            if word.startswith("##"):
                continue  # Skip subword tokens (you can modify this if you need different handling)
            if ent['entity'] == 'B-DISEASE':
                diseases.append(word)
            elif ent['entity'] == 'B-CHEMICAL':
                drugs.append(word)

    return diseases, drugs

# Usage
diseases, drugs = extract_entities_biobert('textonly.txt')
print(f"Total diseases found: {len(diseases)}")
print(f"Total drugs found: {len(drugs)}")

# Github link https://github.com/Shantanu-Barua/HIT137_asgn2.git 