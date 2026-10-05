import streamlit as st
st.set_page_config(page_title="StackUp Lite", page_icon="💰")
lessons = [
    {
        "title": "What Money Is",
        "content": "YOUR EXISTING CONTENT",
        "quiz": [
            {
                "question": "YOUR QUESTION",
                "options": ["CHOICE A", "CHOICE B", "CHOICE C"],
                "answer": "CHOICE B",
            },
            {
                "question": "YOUR SECOND QUESTION",
                "options": ["CHOICE A", "CHOICE B", "CHOICE C"],
                "answer": "CHOICE A",
            },
        ],
    },
    # Needs vs Wants and Saving Basics follow the same pattern
]
page = st.sidebar.radio("Go to", ["Home", "Learn", "About"])
if page == "Home":
    st.title("StackUp Lite")
    st.write("Financial literacy for teens, one tier at a time")
    if st.button("Start Learning"):
        st.write("Open Learn in the sidebar to start your first lesson")
elif page == "Learn":
    st.title("Learn")
    titles = []
    for lesson in lessons:
        titles.append(lesson["title"])
    choice = st.selectbox("Choose a lesson", titles)
    for lesson in lessons:
        if lesson["title"] == choice:
            st.header(lesson["title"])
            st.write(lesson["content"])
else:
    st.title("About StackUp")
    st.write("StackUp teaches teens real money skills through a tiered curriculum")

