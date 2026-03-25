# Finance Quiz / Tutor Bot (GAI-23)

---

## Project Overview

The **Finance Quiz/Tutor Bot** is an AI-powered educational application designed to enhance learning in the finance domain. The system interacts with users through quizzes based on **Investment Reports**, evaluates their responses using a **Large Language Model (LLM)**, and provides detailed explanations to improve understanding.

This project aims to create a **personalized learning experience** by identifying knowledge gaps and reinforcing key financial concepts through contextual feedback.

---

## Problem Statement

Develop an interactive AI-driven educational bot that:

1. Conducts finance-related quizzes
2. Evaluates user responses intelligently
3. Provides detailed explanations for incorrect answers
4. Helps users improve their understanding of investment concepts

---

## Features

1. **AI-Powered Evaluation** – Uses LLM to assess user answers
2. **Finance-Based Quizzes** – Questions derived from investment reports
3. **Contextual Explanations** – Detailed feedback for incorrect answers
4. **Personalized Learning Loop** – Helps users improve over time
5. **Interactive Chat Interface** – Smooth user interaction

---

## Tech Stack

1. **Programming Language**: Python
2. **Frontend/UI**: Python, HTML, CSS (Gradio-based UI)
3. **Backend**: Groq API (LLaMA 3.1 - 8B Instant)
4. **Database**: FAISS (Vector Database)
5. **Embeddings**: Custom Embedding Function (generate_embedding)

---

## System Architecture (High-Level)

1. User interacts with chatbot UI
2. Question is generated from finance/investment data
3. User submits answer
4. Relevant context is retrieved using FAISS
5. LLM evaluates the response
6. System provides:

   1. Score/feedback
   2. Correct answer
   3. Explanation with context
7. Learning loop continues

---

## Project Structure

```bash
financebot/
│── app.py                    # Main Gradio application (UI + flow control)
│── chatbot.py               # Handles quiz flow, evaluation, and explanations
│
├── src/
│   │── embeddings.py        # Generates embeddings for text data
│   │── vector_db.py         # FAISS vector database (build + search functions)
│
├── data/
│   │── finance_data.csv     # Investment reports / finance dataset
│
├── vector_db/
│   │── faiss_index/         # Stored FAISS index files (if persisted)
│
├── .env                     # Environment variables (API keys like GROQ_API_KEY)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## Installation & Setup

### Clone Repository

```bash
git clone https://github.com/Matrixuse/financebot.git
cd financebot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add API Key

Add your Groq API key in the `.env` file:

```env
GROQ_API_KEY="your_api_key_here"
```

---

### Run Application

```bash
python app.py
```

---

## Usage

1. Open the chatbot interface in your browser
2. Answer finance-related questions
3. Get:

   1. Instant feedback
   2. Correct answers
   3. Detailed explanations

---

## Future Enhancements

1. Advanced analytics dashboard
2. More real-world financial datasets
3. Improved personalization using user history
4. Deployment on cloud (Hugging Face / AWS)

---

## Team Members

| No. | Name                 | Enrollment No |
| --- | -------------------- | ------------- |
| 1   | JAYENDRA VERMA       | EN22IT301043  |
| 2   | HANSRAJ SINGH RAJPUT | EN24CA5030055 |
| 3   | ASHISH NAGDA         | EN24CA5030026 |
| 4   | NAMAN SHARMA         | EN22IT301058  |
| 5   | ATUL MANDLOI         | EN24CA5030031 |
| 6   | HITENDRA SAMEDIYA    | EN24CA5030067 |

---

## Subject

Generative AI (Gen AI)

---

## GitHub Repository

https://github.com/Matrixuse/financebot

---

## Conclusion

The Finance Quiz/Tutor Bot leverages Generative AI to transform traditional learning into an interactive, intelligent, and adaptive experience, helping users build strong financial knowledge through continuous feedback and assessment.

---


