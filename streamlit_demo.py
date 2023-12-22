import streamlit as st

prompt = st.chat_input(placeholder="Your message",key=None, max_chars=None, disabled=False, on_submit=None, args=None, kwargs=None)
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

with st.chat_message(name="AI",avatar=None):
    st.write(prompt)
   

