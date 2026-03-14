import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise RuntimeError("Missing GROQ_API_KEY environment variable")

client = Groq(api_key=groq_api_key)

def generate_question(context, difficulty):

    prompt = f"""
    Generate a {difficulty} finance quiz question from this content:

    {context}

    Only output the question.
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return completion.choices[0].message.content