
import streamlit as st
from langchain.llms import OpenAI

st.title('Project Details')

#openai_api_key = st.sidebar.text_input('OpenAI API Key')

openai_api_key = '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'

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'Im making motion graphics fro a 10 minute youtube video')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

st.write('Yoooooo Romano NASA Time!')
