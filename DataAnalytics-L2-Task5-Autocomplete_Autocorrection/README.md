# ✨ NLP Autocomplete & Autocorrect System

An NLP-based **Autocomplete and Autocorrect System** developed using Python and traditional Natural Language Processing techniques.

The system predicts likely next words using **Bigram and Trigram language models** and provides spelling corrections using **Levenshtein Edit Distance** combined with word-frequency ranking.

A **Streamlit web application** was also developed to provide an interactive interface where users can enter different words or phrases and receive autocomplete and autocorrect suggestions.

---

## 🎯 Project Objective

The main objective of this project is to develop an NLP-based system capable of:

- Predicting the next word for a given word or phrase.
- Providing spelling correction suggestions.
- Supporting a broad range of English vocabulary.
- Handling modern and technical words.
- Using word frequency to improve candidate ranking.
- Evaluating autocorrect performance using Accuracy, Precision, and Recall.
- Providing an interactive web-based interface using Streamlit.

---

## 🧠 Project Overview

The system consists of two major components:

### 1. Autocomplete

The autocomplete component predicts the next word using:

- Bigram Language Model
- Trigram Language Model
- Word-frequency-based ranking

The system first attempts to use a Trigram context. If a suitable Trigram prediction is unavailable, it falls back to a Bigram prediction.

### 2. Autocorrect

The autocorrect component identifies possible corrections for misspelled words using:

- Levenshtein Edit Distance
- Vocabulary matching
- Word-frequency ranking

Candidates with smaller edit distances are preferred, while word frequency is used to rank candidates with similar distances.

---

## 📚 Training Data and Corpora

The final system uses multiple text sources to improve vocabulary and language coverage.

### Gutenberg Corpus

The NLTK Gutenberg corpus provides literary English text from multiple books.

### Brown Corpus

The NLTK Brown corpus provides general English text from different categories and writing styles.

### WikiText-2

WikiText-2 provides modern English text and helps improve contemporary language coverage.

### General English Vocabulary

A 50,000-word general English vocabulary is added using the `wordfreq` package.

### Combined Training Data

The final training data combines:

```text
Gutenberg
+
Brown
+
WikiText-2
+
General English Vocabulary
