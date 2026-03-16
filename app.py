import streamlit as st
from auth import register_user, login_user
from src.tutor_engine import get_context
from src.quiz_generator import generate_question
from src.evaluator import evaluate
from src.evaluator import tutor_explain
from ui.dashboard import show_dashboard
def show_chart():
    import pandas as pd
import re
import base64

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "landing"
    
st.markdown("""
<style>
.logout-btn button{
    background: linear-gradient(135deg,#5f6cff,#7a86ff);
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

def set_background():

    with open("data/background.png", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    bg_css = f"""
    <style>

    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .block-container {{
        background-color: rgba(0,0,0,0.65);
        padding: 2rem;
        border-radius: 12px;
        # background: transparent;
    }}

    </style>
    """

    st.markdown(bg_css, unsafe_allow_html=True)

def load_css():
    with open("ui/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Capitra - Finance Tutor",
    page_icon="data/logo.png",
    layout="wide"
)

load_css()
set_background()

# ---------------- LANDING PAGE ----------------

if st.session_state.page == "landing":

    col1, col2, col3 = st.columns([1,2,0.5])

    with col1:
        st.image("data/logo1.png", width=100)

    with col2:
        st.title("Capitra - Finance AI Tutor")

    with col3:
        if st.button("Login"):
            st.session_state.page = "login"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("AI Powered Finance Learning Platform")

    st.write(
        "Generate finance quizzes, get AI explanations, and track your learning performance."
    )

    st.markdown("## Platform Features")

    st.markdown("""
    <style>
    .feature-card {
        background: rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        backdrop-filter: blur(6px);
        transition: 0.3s;
    }
    .feature-card:hover{
        transform: scale(1.05);
        background: rgba(255,255,255,0.12);
    }
    .feature-icon{
        font-size:40px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>AI Quiz Generator</h3>
            <p>Automatically generate finance quizzes based on topics like ROI, Mutual Funds and Portfolio Management.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3>AI Finance Tutor</h3>
            <p>Ask any finance question and get AI-generated explanations with contextual knowledge.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <h3>Performance Dashboard</h3>
            <p>Track quiz scores, weak topics and learning progress through an interactive dashboard.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
#  -------- HOW CAPITRA WORKS --------

    st.markdown("<h2 style='text-align:left;'>How Capitra Works</h2>", unsafe_allow_html=True)

    step1, step2, step3 = st.columns(3)

    with step1:
        st.markdown("### 1️⃣ Enter Topic")
        st.write("Choose a finance topic like ROI, Bonds, ETFs or Mutual Funds.")

    with step2:
        st.markdown("### 2️⃣ Take AI Quiz")
        st.write("Capitra generates personalized questions based on finance knowledge.")

    with step3:
        st.markdown("### 3️⃣ Improve Skills")
        st.write("Get explanations and track your performance in the dashboard.")

    st.markdown("---")

    st.markdown(
    """
    <div style="text-align:center; font-size:14px; opacity:0.8;">
    Capitra • AI Powered Finance Learning Platform <br>
    Built with Streamlit, LLMs and Vector Databases
    </div>
    """,
    unsafe_allow_html=True
    )

    st.stop()

# signup page
if not st.session_state.logged_in and st.session_state.page == "signup":

    st.image("data/logo1.png", width=100)

    st.title("Create Your Capitra Account")

    username = st.text_input("Username", key="signup_username")

    email = st.text_input("Email ID", key="signup_email")

    password = st.text_input("Password", type="password", key="signup_password")

    if st.button("Sign Up"):

        if register_user(username, email, password):
            st.success("Account created successfully")
            st.session_state.page = "login"
            st.rerun()

        else:
            st.error("Email already exists")

    st.markdown("---")

    if st.button("Already have an account? Login"):
        st.session_state.page = "login"
        st.rerun()

    st.stop()

# login page
if not st.session_state.logged_in and st.session_state.page == "login":

    st.image("data/logo1.png", width=100)

    st.title("Login to Capitra")

    email = st.text_input("Email ID", key="login_email")

    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):

        if login_user(email, password):
            st.session_state.logged_in = True
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid Email or Password")

    st.markdown("---")

    if st.button("Don't have an account? Sign Up"):
        st.session_state.page = "signup"
        st.rerun()

    st.stop()


col1, col2, col3 = st.columns([1,2,0.5])

with col1:
    st.image("data/logo1.png", width=100)

with col2:
    st.title("Capitra - Finance AI Tutor")

with col3:
    if st.session_state.logged_in:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.rerun()
    else:
        if st.button("Login"):
            st.session_state.page = "login"
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)


if "scores" not in st.session_state:
    st.session_state.scores = []

if "weak_topics" not in st.session_state:
    st.session_state.weak_topics = []

# Layout
left, separator, right = st.columns([2,0.05,1])

with left:

    topic = st.text_input("Enter Finance Topic")

    difficulty = st.selectbox(
        "Select Difficulty",
        ["Beginner","Intermediate","Advanced"]
    )

    if st.button("Generate Question"):

        if not st.session_state.logged_in:
            st.info("Login to unlock personalized AI finance quizzes and tracking.")
        else:
            context = get_context(topic)
            question = generate_question(context, difficulty)
        
        context = get_context(topic)
        question = generate_question(context, difficulty)

        st.session_state.question = question
        st.session_state.context = context
        st.session_state.topic = topic

    if "question" in st.session_state:

        st.subheader("Quiz:")
        st.subheader("Question:")

        st.info(st.session_state.question)

        answer = st.text_input("Enter your Answer")

        if st.button("Submit Answer"):
            if not st.session_state.logged_in:
                st.warning("Please login to submit answers.")
                st.stop()

            result = evaluate(
                st.session_state.question,
                answer,
                st.session_state.context
            )

            st.subheader("AI Evaluation")

            st.write(result)

    try:
        if "result" in locals():

            score_match = re.search(r"\d+", result)

            if score_match:
                score = int(score_match.group())

                st.session_state.scores.append(score)

                if score < 5:
                    st.session_state.weak_topics.append(
                        st.session_state.topic
                    )

        if score_match:
            score = int(score_match.group())

            st.session_state.scores.append(score)

            if score < 5:
                st.session_state.weak_topics.append(
                    st.session_state.topic
                )

    except:
        pass

with separator:
    st.markdown(
        "<div style='border-left:2px solid gray;height:300px'></div>",
        unsafe_allow_html=True
    )

with right:

    show_dashboard(
        st.session_state.scores,
        st.session_state.weak_topics
    )

# Chat tutor
st.divider()

st.subheader("Ask Finance AI Tutor")

user_question = st.text_input("Ask any finance question to your personal AI tutor")

if st.button("Ask AI"):

    if not st.session_state.logged_in:
        # st.warning("Please login to use AI Tutor.")
        st.info("Login to unlock personalized AI finance quizzes and tracking.")
        st.stop()

    context = get_context(user_question)

    response = tutor_explain(user_question, context)

    st.write(response)

# Visualization
st.divider()

st.subheader("Investment Comparison")

data = {
    "Investment Type":["Bonds","Stocks","ETF","Mutual Funds"],
    "Average Return":[6,12,10,7]
}

df = pd.DataFrame(data)

st.bar_chart(df.set_index("Investment Type"))