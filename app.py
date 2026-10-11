import streamlit as st
st.set_page_config(page_title="StackUp Lite", page_icon="💰")
lessons = [
    {
        "title": "What Money Is",
        "content": "Maya earns \\$25 each week babysitting her neighbor’s kids. This week, she spends \\$8 on lunch and puts \\$17 into her bank account. Her money comes in different forms: the cash her neighbor pays her, the coins in her jar, and the balance in her bank account. She knows that money can be used to buy goods and services, but she also knows that every dollar she spends is a dollar she cannot use for something else.\n\nMoney is a tool that helps Maya make choices about what she needs, what she wants, and what she wants to save for later. But the choice is not always obvious. Maya could spend her \\$17 on a new game she has been wanting, or she could keep it in her account and get closer to her goal of buying a \\$60 pair of headphones.\n\nBefore spending money, Maya asks herself: “Is this the best use of my money right now?”",
",
                "audio": "audio/What-money-is.m4a",
        "quiz": [
            {
                "question": "Which statement best explains the role of money?",
                "options": ["A way to track what people own", "A tool for buying goods and services", "A reward for completing work"],
                "answer": "A tool for buying goods and services",
            },
            {
                "question": "Which example represents money in a bank account?",
                "options": ["A \\$20 bill in your wallet", "A receipt from a store", "A balance shown by your bank"],
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
        "content": "Jordan just got \\$60 for his birthday. He needs new shoes because his current ones are falling apart, but he also really wants a new video game that costs \\$60. Jordan finds a pair of shoes that works for him for \\$40, leaving him with \\$20. If Jordan had bought the game first, he wouldn’t have had enough money left for the shoes he needed.\n\nNeeds are things you require for everyday life, such as food, water, housing, and basic clothing. Wants are things you would enjoy having but can live without, such as video games, expensive headphones, or eating out.\n\nBut sometimes the line between a need and a want isn’t so clear. Jordan needs shoes, but does he need \\$150 designer shoes? The shoes themselves are a need, while the expensive brand is a want. Understanding the difference can help you take care of your needs while making smarter choices about your wants.",
        "tip": "Pay for your needs first, then use what’s left for your wants. Before buying something you want, make sure you have enough money for the things you actually need.",
                "audio": "audio/Needs-vs-wants.m4a",
        "quiz": [
            {
                "question": "What should Jordan prioritize when deciding how to spend his \\$60?",
                "options": ["Buying the video game because it costs exactly \\$60", "Buying the most expensive shoes because they are more useful", "Buying the shoes because they are a need"],
                "answer": "Buying the shoes because they are a need",
            },
            {
                "question": "Why could \\$150 designer shoes be considered partly a want?",
                "options": ["Because all shoes that cost more than \\$100 are wants", "Because Jordan does not need shoes at all", "Because Jordan needs shoes, but does not need the expensive brand"],
                "answer": "Because Jordan needs shoes, but does not need the expensive brand",
            },
            {
                "question": "Sort it: Jordan buys a \\$60 video game because he really wants to play it.",
                "options": ["Need", "Want"],
                "answer": "Want",
            },
            {
                "question": "Sort it: Jordan's shoes are falling apart, so he buys a basic pair for \\$40.",
                "options": ["Need", "Want"],
                "answer": "Need",
            },
            {
                "question": "What is the main lesson Jordan should learn from this situation?",
                "options": ["Take care of your needs first, then spend what remains on your wants", "Avoid buying wants until you have enough money for more expensive needs", "Buy wants first if you have enough money at the moment"],
                "answer": "Take care of your needs first, then spend what remains on your wants",
            },
        ],
    },
    {
        "title": "Saving Basics",
        "content": "Maya still wants the \\$60 headphones. She already has \\$17 in her bank account, and she earns \\$25 each week babysitting. Instead of spending the entire $25, she puts \\$15 into her savings account and keeps \\$10 available for other things. After three more weeks of saving \\$15, she has \\$62, enough for the headphones, without giving up all of her spending money.\n\Saving means choosing to keep some money for the future instead of spending it right away. Even small amounts can add up over time, but saving does not always mean refusing to spend. Maya could save too much and miss out on something useful today, or she could spend too much and have nothing left when she needs it.\n\nBefore spending, Maya asks herself: “Would I rather have this money now, or would saving it help me more later?”
",
                "audio": "audio/Saving-basics.m4a",
        "quiz": [],
    },
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
            if "audio" in lesson:
                st.audio(lesson["audio"], format="audio/mp4")
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

