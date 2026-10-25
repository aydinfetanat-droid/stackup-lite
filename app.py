import streamlit as st
st.set_page_config(page_title="StackUp Lite", page_icon="💰", initial_sidebar_state="expanded")
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
        "audio": "audio/budgeting-50-30-20.m4a",
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
        "audio": "audio/banks-and-interest.m4a",
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
        "audio": "audio/credit-and-debt.m4a",
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
    {
        "title": "Compound Growth",
        "tier": "Managing Director",
        "content": "Jordan starts with \\$1,000 in a hypothetical investment and learns how compound growth works. He uses a 10% annual growth rate for easy math and assumes he reinvests every gain. After the first year, his \\$1,000 becomes \\$1,100. In the second year, he earns 10% of \\$1,100, bringing his balance to \\$1,210. In the third year, he earns \\$121, reaching \\$1,331. His money grows because each year's gains can earn additional gains in later years. He also learns the Rule of 72: dividing 72 by 10 means his money could double in about 7.2 years if it grew at a steady 10% rate.\n\nJordan is excited and thinks he can count on this growth every year. However, he discovers that investment returns change, and some years can bring losses. The 10% rate is just a convenient example, and real returns vary from year to year. Starting early gives money more time to compound, but it does not guarantee a profit.\n\n“Is it better to start building good investing habits early, or wait until you have more money?”",
        "tip": "Tim Metcalf, financial advisor, offers the reminder “Invest early and often,” but remember that 10% is just an easy-math example, real returns vary from year to year, and no return is guaranteed.",
        "audio": "audio/compound-growth.m4a",
        "quiz": [
            {
                "question": "Jordan starts with \\$1,000 and earns 10% annually, reinvesting his gains; how much does he have after three years?",
                "options": ["\\$1,331", "\\$1,310", "\\$1,321"],
                "answer": "\\$1,331",
            },
            {
                "question": "After Jordan's first year, his balance reaches \\$1,100; if it grows another 10% in the second year, what is his new balance?",
                "options": ["\\$1,200", "\\$1,210", "\\$1,110"],
                "answer": "\\$1,210",
            },
            {
                "question": "What makes compound growth different from earning money only on the original amount?",
                "options": ["It adds the same dollar amount every year, regardless of the balance.", "It increases the original amount only when new money is deposited.", "It allows earlier gains to earn additional gains over time."],
                "answer": "It allows earlier gains to earn additional gains over time.",
            },
            {
                "question": "Why should Jordan avoid assuming his investment will earn 10% every year?",
                "options": ["Investment returns vary, and an investment can lose value in some years.", "Compound growth stops whenever the balance reaches \\$1,000 in gains.", "Investment accounts always earn less than 10% and cannot earn more."],
                "answer": "Investment returns vary, and an investment can lose value in some years.",
            },
            {
                "question": "Using the Rule of 72, approximately how long would it take Jordan's money to double at a steady 10% annual growth rate?",
                "options": ["10.2 years", "7.2 years", "5.2 years"],
                "answer": "7.2 years",
            },
        ],
    },
    {
        "title": "Investing Basics",
        "tier": "Managing Director",
        "content": "Maya has \\$300 to use in a classroom investing simulation. She divides the example into three equal amounts of \\$100 to learn about three different investments: a stock, a bond, and a fund. A stock represents a small piece of ownership in a company, so owning shares makes her a partial owner. A bond represents a loan to a company or government, which borrows money and agrees to repay it under the bond's terms. A fund combines multiple investments into one product, allowing investors to own a portion of a collection of assets. Her three \\$100 amounts add up to \\$300, giving her a simple way to compare how different investments work.\n\nAt first, Maya assumes that buying a fund means her money cannot lose value because it holds many investments instead of just one. During the simulation, however, she sees the fund's value fall when several of its investments decline. She learns that funds can spread out risk, but their values can still rise or fall depending on what they hold. Stocks, bonds, and funds all have different risks and potential returns, and none guarantees a profit.\n\n“How can Maya compare investment options without assuming one is automatically safe or better than the others?”",
        "tip": "Understand what you own before investing: stocks represent ownership, bonds represent loans, and funds hold collections of investments, but none guarantees a return.",
        "audio": "audio/investing-basics.m4a",
        "quiz": [
            {
                "question": "Maya divides \\$300 equally among three investment categories in her classroom simulation; how much does she assign to each category?",
                "options": ["\\$100", "\\$150", "\\$75"],
                "answer": "\\$100",
            },
            {
                "question": "Which statement best explains what owning a stock means?",
                "options": ["You have loaned money to a company that must repay it under agreed terms.", "You have purchased a collection of investments managed as one product.", "You own a small piece of a company through its shares."],
                "answer": "You own a small piece of a company through its shares.",
            },
            {
                "question": "What does purchasing a bond generally mean?",
                "options": ["Buying partial ownership in a company and sharing in its results.", "Lending money to a company or government under agreed terms.", "Buying a collection of different stocks and other investments."],
                "answer": "Lending money to a company or government under agreed terms.",
            },
            {
                "question": "Maya's fund loses value because several investments inside it decline; what does this demonstrate?",
                "options": ["A fund can lose value even when it holds multiple investments.", "A fund cannot lose money unless every investment becomes worthless.", "A fund guarantees a profit as long as it owns different companies."],
                "answer": "A fund can lose value even when it holds multiple investments.",
            },
            {
                "question": "What should Maya understand before comparing different investments?",
                "options": ["Stocks, bonds, and funds all provide the same level of risk and return.", "Funds always perform better because they contain more than one investment.", "Different investments have different risks, and their returns are not guaranteed."],
                "answer": "Different investments have different risks, and their returns are not guaranteed.",
            },
        ],
    },
    {
        "title": "Risk and Diversification",
        "tier": "Managing Director",
        "content": "Ethan has \\$900 set aside for two future goals: \\$300 for a program he expects to pay for in one year and \\$600 for a goal seven years away. In his finance class, he learns that risk is the possibility of losing money and that investments with higher potential returns often involve greater risk. His class compares two simplified examples using the \\$600 intended for the longer-term goal. If the entire amount were in one investment that lost 20% of its value, it would fall to \\$480. If he instead divided the \\$600 equally across six different investments worth \\$100 each, and only one lost 20% while the other five stayed unchanged, the total would be \\$580.\n\nEthan initially believes diversification prevents losses entirely. His teacher explains that spreading investments can reduce the damage caused by one investment performing poorly, but multiple investments can decline together. He also learns that time horizon matters: money needed in one year has less time to recover from a market decline than money intended for a goal seven years away. A longer timeline offers more opportunity to recover, but it does not guarantee a positive return.\n\n“How should investors think about risk when their goals have different deadlines?”",
        "tip": "Spread investments across different companies and asset types to reduce reliance on any one holding, while remembering that diversification cannot eliminate all losses.",
        "audio": "audio/risk-and-diversification.m4a",
        "quiz": [
            {
                "question": "In Ethan's classroom example, what would happen to \\$600 invested in one place if its value fell by 20%?",
                "options": ["It would fall to \\$500.", "It would fall to \\$480.", "It would fall to \\$420."],
                "answer": "It would fall to \\$480.",
            },
            {
                "question": "Ethan divides \\$600 equally across six investments worth \\$100 each; if one falls by 20% and the other five stay unchanged, what is the combined value?",
                "options": ["\\$580", "\\$560", "\\$520"],
                "answer": "\\$580",
            },
            {
                "question": "What is the main purpose of diversification?",
                "options": ["To guarantee that at least one investment will always make money.", "To ensure every investment earns approximately the same return.", "To reduce reliance on any one investment and potentially limit losses."],
                "answer": "To reduce reliance on any one investment and potentially limit losses.",
            },
            {
                "question": "Why does Ethan consider the time horizon of his two goals?",
                "options": ["Investments intended for longer-term goals are guaranteed to earn more money.", "Money needed soon has less time to recover from a potential market decline.", "Money intended for a goal seven years away cannot lose value in the meantime."],
                "answer": "Money needed soon has less time to recover from a potential market decline.",
            },
            {
                "question": "What does the risk-and-return tradeoff mean?",
                "options": ["Investments with lower risk always produce the highest long-term returns.", "Investments with higher potential returns cannot lose more money than safer investments.", "Investments with higher potential returns often involve a greater chance of loss."],
                "answer": "Investments with higher potential returns often involve a greater chance of loss.",
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
def tier_counts(tier_name):
    finished = 0
    total = 0
    for lesson in lessons:
        if lesson["tier"] == tier_name:
            total = total + 1
            if lesson["title"] in st.session_state["completed"]:
                finished = finished + 1
    return finished,total
def go_learn():
    st.session_state["page"] = "Learn"
page = st.sidebar.radio("Go to", ["Home", "Learn", "Simulator", "About"], key="page")
demo = st.sidebar.checkbox("Demo mode: unlock all tiers")
if demo:
    unlocked = ["Analyst", "Vice President", "Managing Director"]
if page == "Home":
    st.title("StackUp Lite")
    st.subheader("Financial literacy for teens, one tier at a time.")
    st.write("Short stories, real numbers, and quick quizzes that turn money basics into skills you can use.")
    st.button("Start learning", on_click=go_learn, type="primary")
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("**1. Read**")
            st.write("A short story with real numbers.")
    with col2:
        with st.container(border=True):
            st.markdown("**2. Quiz**")
            st.write("Five questions check what you learned.")
    with col3:
        with st.container(border=True):
            st.markdown("**3. Level up**")
            st.write("Finish a tier to unlock the next one.")
        st.divider()
    st.subheader("Your path")
    tiers = ["Analyst", "Vice President", "Managing Director"]
    tier_cols = st.columns(3)
    for i in range(len(tiers)):
        with tier_cols[i]:
            with st.container(border=True):
                finished, total = tier_counts(tiers[i])
                st.markdown("**" + tiers[i] + "**")
                if tiers[i] in unlocked:
                    st.caption("Unlocked")
                else:
                    st.caption("Locked: finish the tier before it")
                st.progress(finished / total)
                st.write(str(finished) + " of " + str(total) + " lessons")
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
            with st.container(border=True):
                st.header(lesson["title"])
                st.caption(lesson["tier"] + " tier")
                st.write(lesson["content"])
                if "audio" in lesson:
                    st.audio(lesson["audio"], format="audio/mp4")
                if "tip" in lesson:
                    st.info(lesson["tip"])
            if len(lesson["quiz"]) > 0:
                with st.container(border=True):
                    st.subheader("Quiz")
                    answers = []
                    for q in lesson["quiz"]:
                        picked = st.radio(q["question"], q["options"], index=None, key=lesson["title"] + q["question"])
                        answers.append(picked)
                    clicked = st.button("Check answers", type="primary")
            if clicked and None in answers:
                    st.warning("Answer every question first.")
            elif clicked:
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
                            st.balloons()
                            if lesson["title"] not in st.session_state["completed"]:
                                st.session_state["completed"].append(lesson["title"])
                                st.toast("Lesson Complete! Progress Saved.")
            else:
                st.write("Quiz coming soon.")
elif page == "Simulator":
    st.title("Money growth simulator")
    st.caption("A hypothetical example, not a prediction. Real returns vary from year to year.")
    start = st.slider("Starting amount in dollars", 100, 5000, 1000, step=100)
    rate = st.slider("Yearly growth in percent", 1, 12, 10)
    years = st.slider("Number of years", 1, 40, 20)
    st.write("You picked " + str(start) + " at " + str(rate) + " percent for " + str(years) + " years.")
else:
    st.title("About StackUp")
    with st.container(border=True):
        st.subheader("The problem")
        st.write("Financial literacy is a huge problem in today’s world, especially among kids. Kids are expected to know how to file their taxes, build their credit, and manage investments straight out of high school, and that’s a problem.")
    with st.container(border=True):
        st.subheader("How it works")
        st.write("My app is designed to be a learning tool for kids who want to develop financial skills. I understand that learning about finance can feel boring, so StackUp makes it quick and captivating. Every lesson is a short story with real numbers, a quiz, and narration, and finishing a tier unlocks the next one.")
    with st.container(border=True):
        st.subheader("Who built it")
        st.write("I’m Aydin, the founder of StackUp. I built this app because one day I asked my dad, “What does credit mean?” and I did not understand a word of his explanation. I thought to myself, there is no way it should be this hard to build simple financial skills. That is why I built StackUp: to make kids want to start learning and to prepare themselves for the world that is about to present itself.")
    st.caption("StackUp is for education, not personal financial advice.")
done = len(st.session_state["completed"])
total = len(lessons)
fraction = done / total
st.sidebar.progress(fraction)
st.sidebar.write("Progress: " + str(done) + " of " + str(total) + " lessons")

