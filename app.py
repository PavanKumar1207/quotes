import streamlit as st
import random
from datetime import datetime

# List of motivational quotes
quotes = [
    "Believe in yourself!",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it."
]

# Greeting based on time
hour = datetime.now().hour
if hour < 12:
    greeting = "🌅 Good Morning!"
elif 12 <= hour < 17:
    greeting = "☀ Good Afternoon!"
else:
    greeting = "🌙 Good Evening!"

# Streamlit UI
st.title("💡 Daily Motivation App")
st.header(greeting)

# Display random quote
quote = random.choice(quotes)
st.subheader("✨ Today's Quote:")
st.success(quote)

# User input to add new quote
st.write("💬 Want to add your own motivational quote?")
new_quote = st.text_input("Type your quote here:")

if st.button("Add Quote"):
    if new_quote:
        quotes.append(new_quote)
        st.success("Your quote has been added!")
    else:
        st.warning("Please type something before clicking 'Add Quote'.")

# Show all quotes
if st.checkbox("Show all motivational quotes"):
    st.write("📝 All Quotes:")
    for q in quotes:
        st.markdown(f"- {q}")