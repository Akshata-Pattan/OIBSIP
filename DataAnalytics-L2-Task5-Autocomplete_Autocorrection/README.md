# NLP Autocomplete & Autocorrect System

An NLP-based Autocomplete and Autocorrect system built using Python and traditional Natural Language Processing techniques.

The system predicts the next word using Bigram and Trigram language models and corrects spelling mistakes using Levenshtein Edit Distance combined with word-frequency ranking.

## 🎯 Project Objective

The objective of this project is to develop an NLP-based system that can:

- Predict likely next words for a given word or phrase.
- Provide spelling correction suggestions.
- Handle common, modern, and technical vocabulary.
- Evaluate autocorrect performance using Accuracy, Precision, and Recall.
- Provide an interactive web interface using Streamlit.

## 🛠️ Technologies Used

- Python
- NLTK
- Pandas
- Matplotlib
- WordFreq
- Streamlit
- Pickle

## 📚 Datasets / Corpora

The training data combines multiple English text sources:

- NLTK Gutenberg Corpus
- NLTK Brown Corpus
- WikiText-2
- General English vocabulary from WordFreq

Using multiple sources helps provide broader vocabulary and language coverage.

## 🧠 Methodology

### 1. Text Preprocessing

The text data is cleaned by:

- Converting text to lowercase
- Tokenizing text
- Removing non-alphabetic tokens
- Removing stopwords
- Creating cleaned training sequences

### 2. Bigram Model

The Bigram model predicts the next word based on the previous word.

Example:

```text
Input: good
Output: possible next words
