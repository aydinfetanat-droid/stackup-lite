import streamlit as st
st.set_page_config(page_title="StackUp Lite", page_icon="💰")
lessons = [
    {
        "title": "What Money Is",
        "content": "Money is a tool we use to buy goods and services and pay for things we need. It can come in different forms, like cash, coins, or money in a bank account. Understanding how money works helps you make smarter choices with what you earn, spend, and save.",
        "quiz": [
            {
                "question": "Which statement best explains the role of money?",
                "options": ["A way to track what people own", "A tool for buying goods and services", "A reward for completing work"],
                "answer": "A tool for buying goods and services",
            },
            {
                "question": "Which example represents money in a bank account?",
                "options": ["A $20 bill in your wallet", "A receipt from a store", "A balance shown by your bank"],
                "answer": "A balance shown by your bank",
            },
            {
                "question": "Why might understanding money help someone make better financial choices?",
                "options": ["It helps them decide how to earn, spend, and save", "It lets them avoid paying for things they need", "It guarantees they will always have enough money"],
                "answer": "It helps them decide how to earn, spend, and save",
            },
            {
                "question": "Which of the following is NOT a form of money described in the lesson?",
                "options": ["Coins", "Cash", "A product you want to purchase"],
                "answer": "A product you want to purchase",
            },
            {
                "question": "Someone receives money and decides whether to spend it now or keep some for later. Which idea from the lesson does this best demonstrate?",
                "options": ["Making choices about spending and saving", "Choosing between different currencies", "Comparing different products"],
                "answer": "Making choices about spending and saving",
            },
        ],
    },
    {
        "title": "Needs vs Wants",
        "content": "Needs are things you must have to live and stay healthy, such as food, water, housing, and basic clothing. Wants are things you enjoy having but can live without, like expensive clothes, video games, or eating out. Knowing the difference between needs and wants helps you decide what to spend your money on first.",
        "quiz": [],
    },
    {
        "title": "Saving Basics",
        "content": "Saving means putting money aside instead of spending it right away. Even small amounts can add up over time and help you afford future goals or handle unexpected expenses. A good habit is to save part of the money you receive before spending the rest.",
        "quiz": [],
    },
]
    # Needs vs Wants and Saving Basics follow the same pattern
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
            if len(lesson["quiz"]) > 0:
                st.subheader("Quiz")
                answers = []
                for q in lesson["quiz"]:
                    picked = st.radio(q["question"], q["options"], index=None, key=lesson["title"] + q["question"])
                    answers.append(picked)
                if st.button("Check answers"):
                    score = 0
                    for i in range(len(lesson["quiz"])):
                        q = lesson["quiz"][i]
                        if answers[i] == q["answer"]:
                            score = score + 1
                            st.success("Question " + str(i + 1) + ": correct!")
                        else:
                            st.error("Question " + str(i + 1) + ": the answer is " + q["answer"])
                    st.write("You got " + str(score) + " out of " + str(len(lesson["quiz"])) + ".")
            else:
                st.write("Quiz coming soon.")
else:
    st.title("About StackUp")
    st.write("StackUp teaches teens real money skills through a tiered curriculum")

