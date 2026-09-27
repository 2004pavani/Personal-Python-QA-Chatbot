from .similarity import get_answer


def ask_chatbot(user_question):
    """
    Process a user's question and return the chatbot response.
    """

    if not user_question or not user_question.strip():
        return {
            "answer": "Please enter a Python-related question.",
            "matched_question": None,
            "score": 0.0
        }

    return get_answer(user_question)


if __name__ == "__main__":

    question = input("Ask a Python question: ")

    result = ask_chatbot(question)

    print("\nBot:")
    print(result["answer"])

    if result["matched_question"]:
        print("\nMatched Question:")
        print(result["matched_question"])

    print("\nSimilarity Score:")
    print(round(result["score"], 3))