import streamlit as st
import pickle

# Load the trained NLP model
with open("nlp_autocomplete_model.pkl", "rb") as f:
    model = pickle.load(f)

bigram_model = model["bigram_model"]
trigram_model = model["trigram_model"]
combined_vocabulary = model["combined_vocabulary"]
word_frequency = model["word_frequency"]

st.set_page_config(
    page_title="NLP Autocomplete & Autocorrect",
    page_icon="✨",
    layout="centered"
)

st.title("✨ NLP Autocomplete & Autocorrect")
st.write("Enter a word or phrase to get autocomplete and spelling suggestions.")

st.success("Model loaded successfully!")
# -----------------------------
# Autocomplete Function
# -----------------------------

def autocomplete(prefix, top_n=3):
    words = prefix.lower().strip().split()

    if not words:
        return []

    # Try Trigram first
    if len(words) >= 2:
        key = (words[-2], words[-1])

        if key in trigram_model:
            predictions = [
                word
                for word, count in trigram_model[key].items()
                if word != words[-1]
            ]

            predictions.sort(
                key=lambda word: trigram_model[key][word],
                reverse=True
            )

            if predictions:
                return predictions[:top_n]

    # Fall back to Bigram
    last_word = words[-1]

    if last_word in bigram_model:
        predictions = [
            word
            for word, count in bigram_model[last_word].items()
            if word != last_word
        ]

        predictions.sort(
            key=lambda word: bigram_model[last_word][word],
            reverse=True
        )

        return predictions[:top_n]

    return []


# -----------------------------
# Levenshtein Edit Distance
# -----------------------------

def edit_distance(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    m = len(word1)
    n = len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            cost = 0 if word1[i - 1] == word2[j - 1] else 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    return dp[m][n]


# -----------------------------
# Autocorrect Function
# -----------------------------

def autocorrect(word, max_distance=2, top_n=3):
    word = word.lower().strip()

    candidates = []

    for candidate in combined_vocabulary:

        if candidate == word:
            continue

        distance = edit_distance(word, candidate)

        if distance <= max_distance:
            frequency = word_frequency.get(candidate, 0)

            candidates.append(
                (candidate, distance, frequency)
            )

    candidates.sort(
        key=lambda x: (x[1], -x[2])
    )

    return [
        candidate
        for candidate, distance, frequency in candidates[:top_n]
    ]
# -----------------------------
# User Interface
# -----------------------------

st.markdown("---")

st.subheader("🔤 Enter a word or phrase")

user_input = st.text_input(
    "Type here:",
    placeholder="Example: machine learning"
)

if st.button("✨ Generate Suggestions"):

    if not user_input.strip():
        st.warning("Please enter a word or phrase.")

    else:
        # Autocomplete
        st.markdown("### 💡 Autocomplete")

        autocomplete_results = autocomplete(user_input)

        if autocomplete_results:
            for suggestion in autocomplete_results:
                st.write(f"• {suggestion}")
        else:
            st.info("No autocomplete suggestions found.")

        # Autocorrect
        st.markdown("### ✏️ Autocorrect")

        # Correct each word individually
        input_words = user_input.lower().split()
        corrected_words = []

        for word in input_words:
            suggestions = autocorrect(word)

            if suggestions:
                corrected_words.append(suggestions[0])
            else:
                corrected_words.append(word)

        corrected_text = " ".join(corrected_words)

        st.success(f"Suggested correction: **{corrected_text}**")