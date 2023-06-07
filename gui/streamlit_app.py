import os
import sys
import numpy as np
import plotly.figure_factory as ff
import re

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

import streamlit as st
from gpt4free import you

def extract_python_code(response):
    # Find the code block using regex
    import re
    pattern = r"```python\n(.*?)\n```"
    matches = re.findall(pattern, response, re.DOTALL)
    
    if matches:
        python_code = matches[0]
        return python_code
    else:
        return None


def execute_python_code(python_code):
    try:
        exec(python_code)
    except Exception as e:
        print(f"Error executing Python code: {e}")




def get_answer(question: str) -> str:
    # Set cloudflare clearance cookie and get answer from GPT-4 model
    try:
        result = you.Completion.create(prompt=question)

        return result.text

    except Exception as e:
        # Return error message if an exception occurs
        return (
            f'An error occurred: {e}. Please make sure you are using a valid cloudflare clearance token and user agent.'
        )


# Set page configuration and add header
st.set_page_config(
    page_title="gpt4freeGUI",
    initial_sidebar_state="expanded",
    page_icon="🧠",
    menu_items={
        'Get Help': 'https://github.com/xtekky/gpt4free/blob/main/README.md',
        'Report a bug': "https://github.com/xtekky/gpt4free/issues",
        'About': "### gptfree GUI",
    },
)
st.header('GPT4free GUI')

# Add text area for user input and button to get answer
question_text_area = st.text_area('🤖 Ask Any Question :', placeholder='Explain quantum computing in 50 words')
if st.button('🧠 Think'):
    answer = get_answer(question_text_area)
    escaped = answer.encode('utf-8').decode('unicode-escape')
    # Display answer
    st.caption("Answer :")
    st.markdown(escaped)

    python_code = extract_python_code(escaped)
    st.write(python_code)

    if python_code:
        execute_python_code(python_code)
    else:
        print("No Python code found in the response.")

    







# Hide Streamlit footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)