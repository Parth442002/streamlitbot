from email.policy import default
from multiprocessing.connection import answer_challenge
import os
import openai
import streamlit as st
from streamlit_chat import message
from Bot import jolly, append_interaction_to_chat_log

openai.api_key = "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"
print(os.getenv('OPENAI_API_KEY'))

st.set_page_config(
    page_icon='🏢',
    page_title='Attorney ChatBot',
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This is a chatbot created using OPENAI's Advance GPT-3 model",
        'Get Help': 'https://github.com',
        'Report a bug': "https://github.com",
    }
)
st.title("Attorney ChatBot")

st.sidebar.title("🏢 Attorney Chatbot")
st.sidebar.markdown("""

**Feedback/Questions**:
[Githhub](https://github.com)
""")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


question = st.text_input("Say Something to the Chatbot:",
                         value='Hello Jolly')
message(question, is_user=True)

answer = jolly(question)
message(answer)


with st.expander("Not sure what to ask?"):
    st.markdown("""
Try some of these:
```
1. What are basic human rights.
2. Where can I find a lawyer
3. I want to register a company
4. Help me do my taxes better
5. I wanna start a Company
6. How much does it cost to start a LLP?
```
    """)
