import re

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# --------------------------------------------------
# Load Knowledge Base
# --------------------------------------------------

knowledge_base = pd.read_csv(
    "data/python_knowledge_professional.csv"
)


# --------------------------------------------------
# Prepare TF-IDF Search Text
# --------------------------------------------------

knowledge_base["search_text"] = (
    knowledge_base["question"].fillna("")
    + " "
    + knowledge_base["keywords"].fillna("")
)


# --------------------------------------------------
# TF-IDF Vectorizer
# --------------------------------------------------

vectorizer = TfidfVectorizer(
    stop_words="english"
)

knowledge_vectors = vectorizer.fit_transform(
    knowledge_base["search_text"]
)


# --------------------------------------------------
# Similarity Threshold
# --------------------------------------------------

SIMILARITY_THRESHOLD = 0.30


# --------------------------------------------------
# Generic Words
# --------------------------------------------------

GENERIC_WORDS = {
    "python",
    "what",
    "how",
    "why",
    "where",
    "when",
    "who",
    "used",
    "use",
    "using",
    "can",
    "could",
    "would",
    "should",
    "does",
    "do",
    "is",
    "are",
    "the",
    "in",
    "of",
    "for",
    "to",
    "and",
    "a",
    "an",
    "you",
    "your",
    "i",
    "it",
    "me",
    "tell",
    "explain",
    "work",
    "works",
    "working"
}


# --------------------------------------------------
# Normalize Words
# --------------------------------------------------

def normalize_word(word):
    """
    Convert simple plural words to singular forms.

    Examples:
        dictionaries -> dictionary
        functions -> function
        lists -> list
    """

    word = word.lower().strip()

    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"

    if (
        word.endswith("s")
        and len(word) > 3
        and not word.endswith("ss")
    ):
        return word[:-1]

    return word


# --------------------------------------------------
# Extract Important Words
# --------------------------------------------------

def extract_keywords(text):
    """
    Extract meaningful normalized words.
    """

    words = re.findall(
        r"\b\w+\b",
        str(text).lower()
    )

    keywords = set()

    for word in words:

        word = normalize_word(word)

        if word not in GENERIC_WORDS:
            keywords.add(word)

    return keywords


# --------------------------------------------------
# Find Keyword Matches
# --------------------------------------------------

def find_keyword_matches(user_question):

    user_keywords = extract_keywords(
        user_question
    )

    matches = []

    for index, row in knowledge_base.iterrows():

        question_keywords = extract_keywords(
            row["question"]
        )

        row_keywords = extract_keywords(
            row["keywords"]
        )

        all_keywords = (
            question_keywords
            | row_keywords
        )

        overlap = (
            user_keywords
            & all_keywords
        )

        if overlap:

            matches.append({
                "index": index,
                "overlap": overlap,
                "overlap_count": len(overlap)
            })

    return matches


# --------------------------------------------------
# Get Answer
# --------------------------------------------------

def get_answer(user_question):
    """
    Find the most relevant answer from the
    Python knowledge base.
    """

    user_keywords = extract_keywords(
        user_question
    )


    # --------------------------------------------------
    # Special Case: General Python Question
    # --------------------------------------------------

    if not user_keywords:

        python_rows = knowledge_base[
            knowledge_base["question"]
            .str.lower()
            .str.contains(
                "what is python",
                regex=False
            )
        ]

        if not python_rows.empty:

            row = python_rows.iloc[0]

            return {
                "answer": row["answer"],
                "matched_question": row["question"],
                "category": row["category"],
                "example": row["example"],
                "score": 1.0
            }


    # --------------------------------------------------
    # Find Exact Keyword Matches
    # --------------------------------------------------

    keyword_matches = find_keyword_matches(
        user_question
    )


    # --------------------------------------------------
    # Strong Keyword Match
    # --------------------------------------------------

    if keyword_matches:

        # Find the maximum number of matching
        # meaningful keywords.

        maximum_overlap = max(
            match["overlap_count"]
            for match in keyword_matches
        )

        strongest_matches = [
            match
            for match in keyword_matches
            if match["overlap_count"]
            == maximum_overlap
        ]


        # --------------------------------------------------
        # Use TF-IDF to choose among strongest matches
        # --------------------------------------------------

        user_vector = vectorizer.transform(
            [user_question]
        )

        tfidf_scores = cosine_similarity(
            user_vector,
            knowledge_vectors
        )[0]


        best_match = max(
            strongest_matches,
            key=lambda match:
            tfidf_scores[match["index"]]
        )

        best_index = best_match["index"]

        best_score = tfidf_scores[
            best_index
        ]

        matched_row = knowledge_base.iloc[
            best_index
        ]


        # --------------------------------------------------
        # Keyword Match Protection
        # --------------------------------------------------

        # If the user has a strong topic keyword match,
        # accept the answer even if TF-IDF is relatively
        # low.

        if maximum_overlap >= 1:

            return {
                "answer": matched_row["answer"],
                "matched_question": matched_row["question"],
                "category": matched_row["category"],
                "example": matched_row["example"],
                "score": best_score
            }


    # --------------------------------------------------
    # TF-IDF Fallback
    # --------------------------------------------------

    user_vector = vectorizer.transform(
        [user_question]
    )

    similarity_scores = cosine_similarity(
        user_vector,
        knowledge_vectors
    )[0]

    best_index = similarity_scores.argmax()

    best_score = similarity_scores[
        best_index
    ]


    if best_score >= SIMILARITY_THRESHOLD:

        matched_row = knowledge_base.iloc[
            best_index
        ]

        return {
            "answer": matched_row["answer"],
            "matched_question": matched_row["question"],
            "category": matched_row["category"],
            "example": matched_row["example"],
            "score": best_score
        }


    # --------------------------------------------------
    # No Suitable Answer
    # --------------------------------------------------

    return {
        "answer": (
            "Sorry, I couldn't find a suitable answer "
            "in my Python knowledge base."
        ),
        "matched_question": None,
        "category": None,
        "example": None,
        "score": best_score
    }


# --------------------------------------------------
# Direct Test
# --------------------------------------------------

if __name__ == "__main__":

    test_question = (
        "How are dictionaries used in Python?"
    )

    result = get_answer(
        test_question
    )

    print("User Question:")
    print(test_question)

    print("\nAnswer:")
    print(result["answer"])

    print("\nCategory:")
    print(result["category"])

    print("\nMatched Question:")
    print(result["matched_question"])

    print("\nExample:")
    print(result["example"])

    print("\nSimilarity Score:")
    print(round(result["score"], 3))