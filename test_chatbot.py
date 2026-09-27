from src.similarity import get_answer


# --------------------------------------------------
# Test Questions
# --------------------------------------------------

test_questions = [

    # Basic Python
    "What is Python?",

    # Different wording
    "Can you tell me about Python lists?",

    # Functions
    "Why do we use functions in Python?",

    # OOP
    "Explain inheritance in Python",

    # Advanced Python
    "What is a decorator?",

    # Libraries
    "What is Pandas used for?",

    # File Handling
    "How can I read a file in Python?",

    # Collections
    "How are dictionaries used in Python?",

    # Invalid / unrelated question
    "Who invented Java?",

    # Completely unrelated question
    "What is the capital of India?"
]


# --------------------------------------------------
# Test Header
# --------------------------------------------------

print("=" * 70)
print("PERSONAL PYTHON QUESTION-ANSWERING CHATBOT")
print("CHATBOT TESTING")
print("=" * 70)


# --------------------------------------------------
# Run Tests
# --------------------------------------------------

for number, question in enumerate(
    test_questions,
    start=1
):

    result = get_answer(question)

    print(f"\nTEST {number}")
    print("-" * 70)

    print("User Question:")
    print(question)

    print("\nBot Answer:")
    print(result["answer"])

    print("\nCategory:")
    print(result["category"])

    print("\nMatched Question:")
    print(result["matched_question"])

    print("\nSimilarity Score:")
    print(round(result["score"], 3))

    print("-" * 70)