import pandas as pd
import ast

# Load the first CSV file
input_file = "Task 2\uncleaned_data\project-4-at-2025-01-25-19-23-97ad5844.csv"
# Read the CSV file
data = pd.read_csv(input_file)

def process_label(label):
    # Convert the string representation of list to actual list
    label_list = ast.literal_eval(label)
    # Extract 'text' and 'labels', rename them to 'word' and 'label'
    processed = [{'word': item['text'], 'label': item['labels'][0]} for item in label_list]
    return str(processed)

# Extract necessary columns: Sentences and labels (POS tags)
data['label'] = data['label'].apply(process_label)
processed_data = data[['Sentences', 'label']]

# Rename 'label' to 'POS tags' for clarity
processed_data.rename(columns={'label': 'POS tags'}, inplace=True)

processed_data
processed_data.to_csv("Task 2/cleaned_data/NLP_Anntn1.csv")