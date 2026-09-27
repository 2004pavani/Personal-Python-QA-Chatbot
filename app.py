import pandas as pd
import streamlit as st

from src.chatbot import ask_chatbot


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Personal Python Assistant",
    page_icon="🐍",
    layout="wide"
)


# --------------------------------------------------
# Load Knowledge Base
# --------------------------------------------------

knowledge_base = pd.read_csv(
    "data/python_knowledge_professional.csv"
)


# --------------------------------------------------
# Custom Styling
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #666666;
        margin-bottom: 30px;
    }

    .topic-card {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #dddddd;
        text-align: center;
        background-color: #fafafa;
        margin-bottom: 10px;
    }

    .answer-box {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #dddddd;
        background-color: #fafafa;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🐍 Personal Python Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your Python learning companion powered by NLP'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Topic Configuration
# --------------------------------------------------

topics = [
    ("🐍", "Basics"),
    ("🔢", "Data Types"),
    ("📝", "Strings"),
    ("📦", "Collections"),
    ("⚙️", "Functions"),
    ("🏗️", "OOP"),
    ("⚠️", "Exceptions"),
    ("📁", "File Handling"),
    ("🚀", "Advanced Python"),
    ("📊", "Libraries")
]


# Map UI topics to categories in the knowledge base
topic_categories = {

    "Basics": [
        "Python Basics",
        "Operators",
        "Conditional Statements",
        "Loops"
    ],

    "Data Types": [
        "Data Types"
    ],

    "Strings": [
        "Strings"
    ],

    "Collections": [
        "Lists",
        "Tuples",
        "Sets",
        "Dictionaries"
    ],

    "Functions": [
        "Functions"
    ],

    "OOP": [
        "OOP"
    ],

    "Exceptions": [
        "Exception Handling"
    ],

    "File Handling": [
        "File Handling"
    ],

    "Advanced Python": [
        "Modules",
        "Advanced Python",
        "Built-in Functions"
    ],

    "Libraries": [
        "NumPy",
        "Pandas",
        "Matplotlib",
        "Scikit-learn"
    ]
}


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None


# --------------------------------------------------
# Explore Topics
# --------------------------------------------------

st.subheader("📚 Explore Python Topics")


# Display topics in rows of five
for row_start in range(0, len(topics), 5):

    columns = st.columns(5)

    for column, topic in zip(
        columns,
        topics[row_start:row_start + 5]
    ):

        icon, topic_name = topic

        with column:

            if st.button(
                f"{icon}  {topic_name}",
                key=f"topic_{topic_name}",
                use_container_width=True
            ):

                st.session_state.selected_topic = topic_name
                st.session_state.selected_question = None


# --------------------------------------------------
# Display Selected Topic
# --------------------------------------------------

if st.session_state.selected_topic:

    selected_topic = st.session_state.selected_topic

    st.divider()

    st.subheader(
        f"📖 {selected_topic} Topics"
    )

    categories = topic_categories[selected_topic]

    filtered_questions = knowledge_base[
        knowledge_base["category"].isin(categories)
    ]

    if not filtered_questions.empty:

        st.write(
            f"Explore {len(filtered_questions)} "
            f"questions from this topic:"
        )

        # Display questions
        for index, row in filtered_questions.iterrows():

            question = row["question"]

            if st.button(
                f"❓ {question}",
                key=f"question_{index}"
            ):

                st.session_state.selected_question = question


# --------------------------------------------------
# Answer Selected Topic Question
# --------------------------------------------------

if st.session_state.selected_question:

    selected_question = st.session_state.selected_question

    result = ask_chatbot(selected_question)

    st.subheader("🤖 Answer")

    st.markdown(
        f"""
        <div class="answer-box">
            {result["answer"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    if result["matched_question"]:

        st.subheader("📌 Topic")

        st.info(
            f"**{result['category']}**"
        )

        if result["example"]:

            st.subheader("💻 Example")

            st.code(
                result["example"],
                language="python"
            )

        with st.expander(
            "🔎 Matching Information"
        ):

            st.write(
                "**Matched Question:**"
            )

            st.write(
                result["matched_question"]
            )

            st.write(
                "**Similarity Score:**"
            )

            st.progress(
                min(float(result["score"]), 1.0)
            )

            st.write(
                f"{result['score']:.3f}"
            )


st.divider()


# --------------------------------------------------
# Ask Your Own Question
# --------------------------------------------------

st.subheader("💬 Ask a Python Question")

user_question = st.text_input(
    "Enter your question:",
    placeholder="Example: What is inheritance in Python?",
    key="user_question"
)


# --------------------------------------------------
# Ask Button
# --------------------------------------------------

if st.button(
    "🤖 Ask Python Assistant",
    type="primary"
):

    if not user_question.strip():

        st.warning(
            "Please enter a Python-related question."
        )

    else:

        result = ask_chatbot(user_question)

        st.subheader("🤖 Answer")

        st.markdown(
            f"""
            <div class="answer-box">
                {result["answer"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        if result["matched_question"]:

            st.subheader("📌 Topic")

            st.info(
                f"**{result['category']}**"
            )

            if result["example"]:

                st.subheader("💻 Example")

                st.code(
                    result["example"],
                    language="python"
                )

            with st.expander(
                "🔎 Matching Information"
            ):

                st.write(
                    "**Matched Question:**"
                )

                st.write(
                    result["matched_question"]
                )

                st.write(
                    "**Similarity Score:**"
                )

                st.progress(
                    min(float(result["score"]), 1.0)
                )

                st.write(
                    f"{result['score']:.3f}"
                )

        else:

            st.warning(
                "Try asking a question related to "
                "Python programming."
            )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Personal Python Assistant • "
    "Built with Python, TF-IDF, Cosine Similarity and Streamlit"
)