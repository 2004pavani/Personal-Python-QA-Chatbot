# 🐍 Personal Python Question-Answering Chatbot

A personal Python learning assistant that answers Python programming questions using a predefined Python knowledge base and NLP-based question matching.

The application combines **TF-IDF vectorization**, **cosine similarity**, keyword-based matching, and **Streamlit** to provide an interactive learning experience.

---

## 📌 Project Overview

The Personal Python Question-Answering Chatbot is designed to help users learn Python by:

- Asking Python programming questions in natural language
- Finding the most relevant answer from a curated Python knowledge base
- Exploring Python concepts by topic
- Displaying examples along with answers
- Showing the matched knowledge-base question and similarity information
- Rejecting questions that are outside the available Python knowledge base

The chatbot does not depend on an external LLM or paid API. Its responses are generated from the project's predefined knowledge base.

---

## ✨ Features

### 💬 Natural-Language Question Answering
Users can ask questions such as:

- What is Python?
- What is a list in Python?
- Why do we use functions?
- What is inheritance?
- What is a decorator?
- What is Pandas?
- How do I read a file in Python?

### 📚 Topic Exploration

The Streamlit interface provides topic-based exploration:

- 🐍 Basics
- 🔢 Data Types
- 📝 Strings
- 📦 Collections
- ⚙️ Functions
- 🏗️ OOP
- ⚠️ Exceptions
- 📁 File Handling
- 🚀 Advanced Python
- 📊 Libraries

### 🧠 NLP-Based Matching

The chatbot uses:

- TF-IDF Vectorization
- Cosine Similarity
- Keyword matching
- Word normalization
- Similarity/confidence checking

### 💻 Python Examples

Relevant Python code examples are displayed with answers.

### 🛡️ Out-of-Scope Question Handling

Questions outside the Python knowledge base are rejected instead of returning an unrelated answer.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │ Python Knowledge Base   │
                    │        CSV File          │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     similarity.py       │
                    │                         │
                    │ • Keyword Matching      │
                    │ • TF-IDF Vectorization  │
                    │ • Cosine Similarity     │
                    │ • Answer Selection      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       chatbot.py        │
                    │   Chatbot Logic Layer   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │         app.py          │
                    │     Streamlit UI        │
                    └─────────────────────────┘
```

---

## 🧠 How the Chatbot Works

### Step 1 — Knowledge Base

Python questions, answers, keywords, categories, and examples are stored in:

```text
data/python_knowledge_professional.csv
```

The dataset contains curated Python programming knowledge organized into categories.

### Step 2 — Keyword Processing

The user's question is processed to identify meaningful words.

Simple word normalization is applied so that related forms such as:

```text
lists → list
functions → function
dictionaries → dictionary
```

can be matched more effectively.

### Step 3 — TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts the knowledge-base questions and keywords into numerical vectors.

### Step 4 — Cosine Similarity

Cosine similarity is used to measure how closely the user's question matches the knowledge-base entries.

### Step 5 — Answer Selection

The chatbot combines meaningful keyword matching with similarity-based matching to identify the most relevant knowledge-base entry.

### Step 6 — Response

The application returns:

- Answer
- Category
- Example
- Matched question
- Similarity information

If a suitable Python answer cannot be found, the chatbot displays an out-of-scope message.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Knowledge-base CSV processing |
| Scikit-learn | TF-IDF and cosine similarity |
| Streamlit | Interactive web interface |
| CSV | Python knowledge-base storage |

---

## 📂 Project Structure

```text
Personal-Python-QA-Chatbot/
│
├── data/
│   └── python_knowledge_professional.csv
│
├── src/
│   ├── __init__.py
│   ├── chatbot.py
│   └── similarity.py
│
├── app.py
├── test_chatbot.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd Personal-Python-QA-Chatbot
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Testing

The project includes a test script covering both valid Python questions and unrelated questions.

Run:

```bash
python test_chatbot.py
```

Example test cases include:

```text
What is Python?
Can you tell me about Python lists?
Why do we use functions in Python?
Explain inheritance in Python
What is a decorator?
What is Pandas used for?
How can I read a file in Python?
How are dictionaries used in Python?
Who invented Java?
What is the capital of India?
```

The chatbot should provide answers for supported Python questions and reject questions outside its knowledge base.

---

## 📊 Example Workflow

```text
User:
"What is inheritance in Python?"

            ↓

Keyword Processing

            ↓

TF-IDF Vectorization

            ↓

Cosine Similarity

            ↓

Best Knowledge-Base Match

            ↓

Category:
OOP

            ↓

Answer + Python Example
```

---

## 🎯 Knowledge Base Topics

The professional knowledge base covers areas including:

- Python Basics
- Data Types
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
- Operators
- Conditional Statements
- Loops
- Functions
- OOP
- Exception Handling
- File Handling
- Modules
- Advanced Python
- Built-in Functions
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

## 🔒 Scope

This chatbot is designed specifically for questions covered by its predefined Python knowledge base.

It is not intended to:

- Generate arbitrary answers outside the knowledge base
- Replace a general-purpose AI assistant
- Execute user-provided Python code
- Access external websites or APIs for answers

---

## 🚀 Future Enhancements

Possible future improvements include:

- Conversation history
- Voice-based questions
- More Python knowledge-base entries
- Fuzzy matching
- Improved semantic search
- User progress tracking
- Quiz mode
- Code execution sandbox
- Advanced NLP models
- Dark/light UI themes
- Deployment with a public URL

---

## 👩‍💻 Author

**Pavani Baji**

Personal Python Question-Answering Chatbot  
Built using Python, NLP techniques, and Streamlit.
