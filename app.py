import streamlit as st

# Set the title of the app
st.title("Letter Counter")

# Prompt the user to enter some text
user_input = st.text_input("Enter a message for Eve:")

if user_input:
    # Count the number of letters (ignoring spaces)
    letter_count = len(user_input.replace(" ", ""))

    # Display the input and the number of letters
    st.write(f"Message: {user_input}")
    st.write(f"Number of letters: {letter_count}")
