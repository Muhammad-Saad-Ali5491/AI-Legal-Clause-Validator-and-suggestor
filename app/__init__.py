# app/__init__.py

"""
AI Legal Validator App Package

This package contains:
- utils.py: Core functions (text extraction, clause classification, suggestion, etc.)
- routes.py: Streamlit frontend logic
"""

import os
import spacy
import google.generativeai as genai
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load all models once when the package is imported
nlp = spacy.load("en_core_web_sm")
tokenizer = AutoTokenizer.from_pretrained("Anery/legalbert_clause_combined")
hf_model = AutoModelForSequenceClassification.from_pretrained("Anery/legalbert_clause_combined")

# Load Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AIzaSyD9ZaIB9w7wL4UsAhOuBdjNecL6DbP4DOc"))
gemini_model = genai.GenerativeModel("gemma-3n-e4b-it")

print("✅ app package initialized with SpaCy, LegalBERT, and Gemini")
