import streamlit as st
st.title("Number Guessing Game : Test your luck!")
import random
number=random.randint(1,100)
user_guess=st.sidebar.slider("Guess the number between 1 and 100",1,100)
if st.sidebar.button("Guess"):
    if user_guess==number:
        st.sidebar.success("You won!")
    else:
        st.sidebar.error("You lost!")
        if user_guess<number:
            st.sidebar.write("Guess a bit more higher!")
            if user_guess>number:
                st.sidebar.write("Go low man!")
