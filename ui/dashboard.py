import streamlit as st

def show_dashboard(scores, weak_topics):

    st.subheader("Performance Dashboard")

    col1, col2, col3 = st.columns(3)

    avg = round(sum(scores)/len(scores),2) if scores else 0
    accuracy = round((sum(scores)/(len(scores)*10))*100,2) if scores else 0

    with col1:
        st.metric("Average Score", avg)

    with col2:
        st.metric("Questions Attempted", len(scores))

    with col3:
        st.metric("Accuracy %", f"{accuracy}%")

    st.subheader("Weak Topics")

    for topic in weak_topics:
        st.warning(topic)