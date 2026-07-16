from ingestion import load_pdf
import re

def clean_text(text):
    text = text.strip()
    text = text.replace('\n', ' ')

    return text

def retrieve_text(file_path):
    pdf_data = load_pdf(file_path)
    cleaned_text = []
    for page in pdf_data:
        cleaned_text.append(clean_text(page["content"]))

    return cleaned_text




