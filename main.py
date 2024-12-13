import streamlit as st

# Add title
st.title("My First Streamlit App")

# Display some text
st.write("Hello, welcome to my app built using Streamlit!")

# Slider for user input
slider_value = st.slider("Select a number", min_value=0, max_value=100, value=50)

# Display the slider value using Streamlit's write method
st.write(f"You selected: {slider_value}")

# Use Python's print function (will not show in the Streamlit app, but in the terminal)
print(f"You selected: {slider_value}")
