import streamlit as st
st.set_page_config(page_title="StackUp Lite", page_icon="💰")
lessons = [
    {
        "title": "What Money Is",
        "tier": "Analyst",
        "content": "Maya earns \\$25 each week babysitting her neighbor’s kids. This week, she spends \\$8 on lunch and puts \\$17 into her bank account. Her money comes in different forms: the cash her neighbor pays her, the coins in her jar, and the balance in her bank account. She knows that money can be used to buy goods and services, but she also knows that every dollar she spends is a dollar she cannot use for something else.\n\nMoney is a tool that helps Maya make choices about what she needs, what she wants, and what she wants to save for later. But the choice is not always obvious. Maya could spend her \\$17 on a new game she has been wanting, or she could keep it in her account and get closer to her goal of buying a \\$60 pair of headphones.\n\nBefore spending money, Maya asks herself: “Is this the best use of my money right now?”",
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
        "tier": "Analyst",
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
        "tier": "Analyst",
        "content": "Maya still wants the \\$60 headphones. She already has \\$17 in her bank account, and she earns \\$25 each week babysitting. Instead of spending the entire \\$25, she puts \\$15 into her savings account and keeps \\$10 available for other things. After three more weeks of saving \\$15, she has \\$62, enough for the headphones, without giving up all of her spending money.\n\nSaving means choosing to keep some money for the future instead of spending it right away. Even small amounts can add up over time, but saving does not always mean refusing to spend. Maya could save too much and miss out on something useful today, or she could spend too much and have nothing left when she needs it.\n\nBefore spending, Maya asks herself: “Would I rather have this money now, or would saving it help me more later?”",
                "audio": "audio/Saving-basics.m4a",
                "quiz": [
            {
                "question": "What is the main benefit of Maya saving \\$15 each week?",
                "options": ["She can buy the headphones while keeping some money available for other things.", "She can spend all her money now without worrying about future expenses.", "She can avoid spending money on anything she wants until she earns more."],
                "answer": "She can buy the headphones while keeping some money available for other things.",
            },
            {
                "question": "How much money does Maya have after saving \\$15 for three more weeks?",
                "options": ["\\$57", "\\$62", "\\$45"],
                "answer": "\\$62",
            },
            {
                "question": "What does saving mean?",
                "options": ["Keeping all your money and never spending it on wants.", "Spending money now before deciding what you might need later.", "Keeping some money for the future instead of spending it right away."],
                "answer": "Keeping some money for the future instead of spending it right away.",
            },
            {
                "question": "What could happen if Maya saves too much money?",
                "options": ["She might miss out on something useful that she needs today.", "She will always have enough money for every future expense.", "She will automatically earn more money each week."],
                "answer": "She might miss out on something useful that she needs today.",
            },
            {
                "question": "What question should Maya ask herself before spending money?",
                "options": ["Can I spend all my money now and earn it back later?", "Would spending this money now help me more than saving it for later?", "Should I stop spending money until I can afford everything I want?"],
                "answer": "Would spending this money now help me more than saving it for later?",
            },
        ],
    },
    {
        "title": "Budgeting with 50/30/20",
        "tier": "Vice President",
        "content": "Ava takes home \\$200 from her weekend job and wants to manage it wisely. She tries the 50/30/20 budgeting guideline: \\$100 for needs, \\$60 for wants, and \\$40 for savings or extra debt payments. She plans to use the \\$100 for transportation and basic meals, the \\$60 for movies and other fun activities, and the \\$40 for her savings account. This gives every dollar a purpose while still leaving room for things she enjoys.\n\nBut Ava discovers that her transportation and food expenses will cost \\$110 this month instead of \\$100. Rather than abandoning her budget, she adjusts it to \\$110 for needs, \\$50 for wants, and \\$40 for savings. Her total is still \\$200, and she has protected her essential expenses without giving up saving entirely.\n\n“Should a budget follow a perfect formula, or should it change when real life changes?”",
        "tip": "Use the 50/30/20 guideline as a starting point: on \\$200, plan \\$100 for needs, \\$60 for wants, and \\$40 for savings or extra debt payments, then adjust when your real expenses require it.",
        "quiz": [
            {
                "question": "Ava takes home \\$200 and follows the 50/30/20 guideline. How should she initially divide her money?",
                "options": ["\\$100 for needs, \\$60 for wants, and \\$40 for savings or extra debt payments", "\\$100 for needs, \\$40 for wants, and \\$60 for savings or extra debt payments", "\\$120 for needs, \\$40 for wants, and \\$40 for savings or extra debt payments"],
                "answer": "\\$100 for needs, \\$60 for wants, and \\$40 for savings or extra debt payments",
            },
            {
                "question": "Ava's needs rise from \\$100 to \\$110. Which adjustment did she make so she could keep saving \\$40 and keep her total at \\$200?",
                "options": ["Increase needs to \\$110, keep wants at \\$60, and reduce savings to \\$30", "Increase needs to \\$110, reduce wants to \\$50, and keep savings at \\$40", "Increase needs to \\$120, reduce wants to \\$40, and keep savings at \\$40"],
                "answer": "Increase needs to \\$110, reduce wants to \\$50, and keep savings at \\$40",
            },
            {
                "question": "Why is the 50/30/20 method considered a guideline rather than a strict rule?",
                "options": ["Everyone should spend the same percentage on wants regardless of income", "Saving should only happen when all wants have already been purchased", "Actual expenses and financial priorities can change how money should be divided"],
                "answer": "Actual expenses and financial priorities can change how money should be divided",
            },
            {
                "question": "Which expense would generally fit into Ava's wants category?",
                "options": ["Basic meals she needs throughout the week", "A movie ticket she buys for entertainment", "Transportation she needs to get to school"],
                "answer": "A movie ticket she buys for entertainment",
            },
            {
                "question": "What is the main purpose of creating a budget?",
                "options": ["To plan spending, cover important expenses, and make progress toward financial goals", "To avoid spending money on wants until every possible future expense is covered", "To make sure every month uses exactly the same spending amounts and percentages"],
                "answer": "To plan spending, cover important expenses, and make progress toward financial goals",
            },
        ],
    },
    {
        "title": "Banks and Interest",
        "tier": "Vice President",
        "content": "Noah has \\$500 saved from his summer job. He keeps \\$150 in his checking account for everyday purchases and places \\$350 in a savings account for a future laptop. He learns that checking accounts are generally designed for regular transactions, while savings accounts help him set money aside. His bank also pays interest on his savings. At an annual interest rate of 2%, for example, his unchanged \\$350 balance would earn roughly \\$7 over one year, before taxes.\n\nNoah initially thinks the account with the highest interest rate must be the best choice. However, he notices that another account charges a \\$4 monthly fee under certain balance conditions. That fee could total \\$48 over a year, potentially wiping out the benefit of earning more interest. He also learns that eligible deposits at FDIC-insured banks are generally insured up to \\$250,000 per depositor, per bank, per ownership category, while federally insured credit unions have NCUA share insurance.\n\n“Should Noah choose a bank based only on interest, or consider the fees and protections too?”",
        "tip": "Compare a bank account's interest, fees, access, and federal insurance coverage before deciding where to keep your money.",
        "quiz": [
            {
                "question": "What is the main purpose of a checking account?",
                "options": ["To hold money for several years without making regular transactions", "To manage everyday spending, payments, and deposits", "To earn the highest possible interest on money you will not need soon"],
                "answer": "To manage everyday spending, payments, and deposits",
            },
            {
                "question": "If Noah keeps \\$350 in savings for one year at an annual interest rate of 2%, for example, approximately how much interest would he earn if the balance stays unchanged?",
                "options": ["\\$7", "\\$14", "\\$35"],
                "answer": "\\$7",
            },
            {
                "question": "What does interest generally represent in a savings account?",
                "options": ["A monthly charge for keeping money at a financial institution", "A guaranteed increase in savings regardless of the account's terms", "Money the financial institution pays for the use of deposited funds"],
                "answer": "Money the financial institution pays for the use of deposited funds",
            },
            {
                "question": "Which statement correctly describes deposit insurance?",
                "options": ["The FDIC insures every investment purchased through a bank up to \\$250,000", "The NCUA and FDIC insure all money held at any financial institution, regardless of its status", "The FDIC protects eligible deposits at insured banks, while the NCUA protects eligible deposits at federally insured credit unions"],
                "answer": "The FDIC protects eligible deposits at insured banks, while the NCUA protects eligible deposits at federally insured credit unions",
            },
            {
                "question": "Why should Noah compare account fees as well as interest rates?",
                "options": ["Fees can reduce or outweigh the interest an account earns", "Fees always increase when an account pays more interest", "Interest rates matter only when the account has a monthly fee"],
                "answer": "Fees can reduce or outweigh the interest an account earns",
            },
        ],
    },
    {
        "title": "Credit and Debt",
        "tier": "Vice President",
        "content": "Kira has \\$300 in her checking account that she is saving for upcoming expenses. She also wants headphones that cost \\$300. She could use her debit card, which takes money directly from her bank account, or a credit card, which lets her borrow money and repay it later. Kira chooses credit because the card only requires a \\$15 minimum payment each month. The card has an annual percentage rate (APR) of 24%, for example, meaning interest may be charged if she carries a balance.\n\nWhen her bill arrives, Kira realizes that the \\$15 minimum is not the full cost of the headphones. Paying only the minimum can make repayment take much longer and increase the total amount she pays. If her card offers a purchase grace period, paying the full statement balance by the due date can help her avoid interest on eligible purchases. She also learns that payment history has a major impact on many credit scores.\n\nKira hears a rule of thumb from Tim Metcalf, financial advisor: “Don't pay interest except for real estate.” However, this is not a universal rule; some student loans used to finance a degree may be worthwhile depending on their costs and the borrower's future plans.\n\n“Is borrowing always a bad choice, or does the cost and purpose of the debt matter?”",
        "tip": "Avoid unnecessary interest and try to pay more than the minimum. One advisor's rule of thumb, from Tim Metcalf, financial advisor: “Don't pay interest except for real estate,” although education loans may sometimes be worth considering.",
        "quiz": [
            {
                "question": "What is the main difference between a debit card and a credit card?",
                "options": ["A debit card uses money from your bank account, while a credit card lets you borrow money and repay it later", "A debit card lets you borrow money, while a credit card immediately withdraws money from checking", "A debit card and a credit card both withdraw money directly from your bank account at purchase"],
                "answer": "A debit card uses money from your bank account, while a credit card lets you borrow money and repay it later",
            },
            {
                "question": "What does a credit card's APR of 24%, for example, tell Kira?",
                "options": ["She must pay exactly 24% of the purchase price as a one-time fee", "It is an annual borrowing rate that can affect the cost of carrying a balance", "She will pay 24% interest on every purchase even when she qualifies for a grace period and pays in full"],
                "answer": "It is an annual borrowing rate that can affect the cost of carrying a balance",
            },
            {
                "question": "Why can paying only the minimum payment become a problem?",
                "options": ["It automatically causes a late payment on the next billing cycle", "It prevents the borrower from making any additional payments", "It can leave a balance that takes longer to repay and may accumulate more interest"],
                "answer": "It can leave a balance that takes longer to repay and may accumulate more interest",
            },
            {
                "question": "Which action generally has the greatest impact on building a strong credit score?",
                "options": ["Making loan and credit payments on time, every time", "Applying for several credit cards within a short period", "Keeping a balance on every credit card from month to month"],
                "answer": "Making loan and credit payments on time, every time",
            },
            {
                "question": "What is the most reasonable way to interpret the advisor's rule of thumb about paying interest?",
                "options": ["All forms of borrowing are harmful, regardless of their purpose or cost", "Borrowing for real estate is always beneficial, regardless of the interest rate", "Avoid unnecessary interest, but consider the purpose, cost, and repayment plan before deciding whether certain debt is worthwhile"],
                "answer": "Avoid unnecessary interest, but consider the purpose, cost, and repayment plan before deciding whether certain debt is worthwhile",
            },
        ],
    },
]
if "completed" not in st.session_state:
    st.session_state["completed"] = []
def tier_done(tier_name):
    count = 0
    for lesson in lessons:
        if lesson["tier"] == tier_name:
            count = count + 1
            if lesson["title"] not in st.session_state["completed"]:
                return False
    return count > 0
unlocked = ["Analyst"]
if tier_done("Analyst"):
    unlocked.append("Vice President")
if tier_done("Vice President"):
    unlocked.append("Managing Director")
page = st.sidebar.radio("Go to", ["Home", "Learn", "About"])
demo = st.sidebar.checkbox("Demo mode: unlock all tiers")
if demo:
    unlocked = ["Analyst", "Vice President", "Managing Director"]
if page == "Home":
    st.title("StackUp Lite")
    st.write("Financial literacy for teens, one tier at a time")
    if st.button("Start Learning"):
        st.write("Open Learn in the sidebar to start your first lesson")
elif page == "Learn":
    st.title("Learn")
    tier_choice = st.selectbox("Choose a tier", unlocked)
    titles = []
    for lesson in lessons:
        if lesson["tier"] == tier_choice:
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
                    if score == len(lesson["quiz"]):
                        if lesson["title"] not in st.session_state["completed"]:
                            st.session_state["completed"].append(lesson["title"])
            else:
                st.write("Quiz coming soon.")
else:
    st.title("About StackUp")
    st.write("StackUp teaches teens real money skills through a tiered curriculum")
done = len(st.session_state["completed"])
total = len(lessons)
fraction = done / total
st.sidebar.progress(fraction)
st.sidebar.write("Progress: " + str(done) + " of " + str(total) + " lessons")

