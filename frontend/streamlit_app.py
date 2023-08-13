import openai
import streamlit as st
api_key = st.secrets["api"]["key"]
openai.api_key = api_key
st.title('Automated Code Generator')
user_input = st.text_input('Describe what you want the code to do:')

if user_input:
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'Generate Python code for: {user_input}',
        max_tokens=500,
        temperature=0.5
    )
    generated_code = response['choices'][0]['text'].strip()
    st.code(generated_code, language='python')

st.write('Created by Group 7: Dheeraj Pagare and Prashant Kumar Jha')
