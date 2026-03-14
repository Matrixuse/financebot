import os
from groq import Groq
from dotenv import load_dotenv

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise RuntimeError("Missing GROQ_API_KEY environment variable")

client = Groq(api_key=groq_api_key)

def evaluate(question, user_answer, context):

    prompt = f"""
    Question: {question}

    User Answer: {user_answer}

    Context: {context}

    Evaluate the answer.

    Provide:
    Score out of 10
    Correct explanation
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return completion.choices[0].message.content

def tutor_explain(question, context):

    prompt = f"""
    A student asked this finance question:

    {question}

    Use this knowledge:

    {context}

    Explain the concept clearly in simple terms.
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return completion.choices[0].message.content