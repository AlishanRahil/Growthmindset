import streamlit as st
import pandas as pd

# Sample dataset (you can replace it with any dataset)
data = pd.DataFrame({
    'Name': ['Inception', 'The Matrix', 'Interstellar', 'Avengers', 'The Dark Knight'],
    'Category': ['Sci-Fi', 'Sci-Fi', 'Sci-Fi', 'Action', 'Action'],
    'Year': [2010, 1999, 2014, 2012, 2008]
})

# Initialize session state
if 'index' not in st.session_state:
    st.session_state.index = 0

# User input
st.markdown("<style>body { background-color: white; }</style>", unsafe_allow_html=True)
user_name = st.text_input("Enter your name:")
if user_name:
    st.success(f"Hello, {user_name}!")

# Display current item
current_item = data.iloc[st.session_state.index]
st.subheader("Swipe Data App")
st.write(f"**{current_item['Name']} ({current_item['Year']})**")
st.write(f"Category: {current_item['Category']}")

# Next button to show data sequentially
if st.button("➡ Next"):
    st.session_state.index = (st.session_state.index + 1) % len(data)
