import streamlit as st
st.set_page_config(page_title="StackUp Lite", page_icon="💰")
lessons = [
    {"title": "What Money Is", "content": "Money is a tool we use to buy goods and services and pay for things we need. It can come in different forms, like cash, coins, or money in a bank account. Understanding how money works helps you make smarter choices with what you earn, spend, and save."},
    {"title": "Needs vs Wants", "content": "Needs are things you must have to live and stay healthy, such as food, water, housing, and basic clothing. Wants are things you enjoy having but can live without, like expensive clothes, video games, or eating out. Knowing the difference between needs and wants helps you decide what to spend your money on first."},
    {"title": "Saving Basics", "content": "Saving means putting money aside instead of spending it right away. Even small amounts can add up over time and help you afford future goals or handle unexpected expenses. A good habit is to save part of the money you receive before spending the rest."},
]
page = st.sidebar.radio("Go to", ["Home", "Learn", "About"])
if page == "Home":
  st.title("StackUp Lite") 
  st.write("Financial literacy for teens, one tier at a time")
  if st.button("Start Learning"):
    st.write("Lessons arrive in the next build session")
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
  st.title ("About StackUp")
  st.write ("StackUp teaches teens real money skills through a tiered curriculum")

