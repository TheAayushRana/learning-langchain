import streamlit as st
from streamlit_chat import message
from main import chat_with_product

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'user_prompt_history' not in st.session_state:
    st.session_state['user_prompt_history'] = []
if 'chat_answer_history' not in st.session_state:
    st.session_state['chat_answer_history'] = []

st.header("Talk to your product")

file = st.file_uploader("Upload your product info", accept_multiple_files=False, type=["png", "jpg", "jpeg"])

if file:
    product_info = chat_with_product(file)
    print(product_info)
    st.session_state['user_prompt_history'].append("I want to know details about this product")
    st.session_state['chat_answer_history'].append(product_info)
    st.session_state['chat_history'].append(("human", "I want to know details about this product"))
    st.session_state['chat_history'].append(("ai", product_info))

if st.session_state['user_prompt_history']:
    print(st.session_state['user_prompt_history'])
    for (user_chat, chat_answer) in zip(st.session_state['user_prompt_history'], st.session_state['chat_answer_history']):
        print("user_chat", user_chat)
        message(user_chat, is_user=True)
        message(chat_answer, is_user=False)