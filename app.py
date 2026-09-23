import streamlit as st
st.set_page_config(page_title="StackUp Lite", page_icon="💰")
page = st.sidebar.radio ("Go to", ["Home","About"])
if page == "Home":
  st.title("StackUp Lite") 
  st.write("Financial literacy for teens, one tier at a time")
  if st.button("Start Learning"):
    st.write("Lessons arrive in the next build session")
else:
  st.title ("About StackUp")
  st.write ("Stackup teaches teens real money skills through a tiered curriculum")
