import streamlit as st
from chatbot.modules import CBT_MODULES
from chatbot.sentiment import analyze_sentiment
from chatbot.storage import init_db, save_chat

init_db()
st.title("🧠 CBT AI Mental Health Bot for Rwandan Youth")
st.sidebar.title("Choose CBT Module")
module = st.sidebar.selectbox("", list(CBT_MODULES.keys()))

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", "")
if st.button("Send") and user_input:
    sentiment, _ = analyze_sentiment(user_input)
    questions = CBT_MODULES[module]
    index = len(st.session_state.history) % len(questions)
    bot_response = questions[index]
    st.session_state.history.append((user_input, bot_response, sentiment))
    save_chat(module, user_input, bot_response, sentiment)

for user, bot, sentiment in st.session_state.history:
    st.markdown(f"**You** ({sentiment}): {user}")
    st.markdown(f"**Bot** 🤖: {bot}")
