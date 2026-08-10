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

---

## 🔄 Data Preprocessing

The text data is preprocessed before training the language models.

The preprocessing steps include:

1. Converting text to lowercase.
2. Tokenizing the text.
3. Removing non-alphabetic tokens.
4. Removing English stopwords.
5. Creating cleaned training sequences.
6. Combining the cleaned sequences from all three corpora.

The preprocessing helps create consistent and useful text data for building the autocomplete models.

---

## 🔤 Bigram Language Model

A Bigram model predicts the next word based on the previous word.

For example:

```text
Input:
good

Possible next words:
morning
day
sir

---

## 🔡 Trigram Language Model

A Trigram model predicts the next word based on the previous two words.

For example:

```text
Input:
good morning

Possible next words:
sir
said
dear

---

## 💡 Autocomplete

The autocomplete system first checks whether the entered phrase has a matching Trigram context.

If a Trigram prediction is not available, the system falls back to the Bigram model.

The overall process is:

```text
User Input
    ↓
Check Trigram Context
    ↓
Trigram Suggestions
    ↓
If unavailable
    ↓
Bigram Suggestions
    ↓
Top 3 Predictions

The system is designed to accept different words and phrases entered by the user rather than relying only on predefined test inputs.

---

## ✏️ Autocorrect

The autocorrect component identifies possible corrections for misspelled words.

It uses **Levenshtein Edit Distance** to measure how many character-level changes are required to transform one word into another.

Candidate words are ranked using:

1. Edit distance
2. Word frequency

A smaller edit distance indicates a closer spelling match, while word frequency helps select the more commonly occurring candidate when multiple candidates have similar distances.

### Example

```text
Misspelled:
acommodate

Suggested correction:
accommodate

Other tested examples include:

```text
freind      → friend
definately  → definitely
enviroment  → environment
goverment   → government
occured     → occurred
recieve     → receive
seperate    → separate
pythn       → python
computr     → computer
softwre     → software
machne      → machine
inteligence → intelligence
artifical   → artificial
instagrm    → instagram
whatsap     → whatsapp

---

## 📊 Autocorrect Evaluation

The autocorrect system was evaluated using a test set of 20 intentionally misspelled words.

The evaluation compares the top predicted correction with the expected correct spelling.

### Final Evaluation Results

| Metric | Result |
|---|---:|
| Correct Predictions | 16 / 20 |
| Total Test Words | 20 |
| Accuracy | **80%** |
| Precision | **80%** |
| Recall | **80%** |

The system correctly predicted the expected correction for 16 out of 20 evaluation words.

---

## 📈 Performance Comparison

During development, different autocorrect approaches were evaluated.

| Approach | Accuracy |
|---|---:|
| Basic Edit-Distance Approach | 65% |
| Frequency-Aware Autocorrect | 70% |
| Expanded Multi-Corpus Approach | **80%** |

The expanded multi-corpus approach provided broader vocabulary coverage and improved the final evaluation result.

---

## 📉 Accuracy Visualization

A comparison graph was created to visualize the performance of the different autocorrect approaches.

The graph compares:

- Basic Edit Distance
- Frequency-Aware Autocorrect
- Expanded Multi-Corpus Autocorrect

The final expanded multi-corpus approach achieved the highest accuracy in the evaluation.

---

## 🌐 Streamlit Web Application

The trained NLP system was integrated into a Streamlit web application.

The application provides an interactive interface where users can enter different words or phrases.

### The application provides:

- 🔤 Autocomplete suggestions
- ✏️ Autocorrect suggestions
- 💡 Top next-word predictions
- 🌐 Interactive browser-based interface

The trained models are saved using Pickle so that the application does not need to rebuild the complete training process every time it starts.

---

## 🖥️ Running the Application

### Install the required packages

```bash
pip install -r requirements.txt

### Run the Streamlit application

```bash
streamlit run app.py

---

## 👩‍💻 Author

**Akshata**

B.E. Artificial Intelligence and Machine Learning

PDA College of Engineering, Kalaburagi

---

## 📌 Project Information

**Internship:** Oasis Infobyte Internship  
**Task:** Task 5 – NLP Autocomplete and Autocorrect  
**Domain:** Natural Language Processing (NLP)  
**Technology:** Python, NLTK, Streamlit

---
