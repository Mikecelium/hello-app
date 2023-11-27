import os
import streamlit as st
from langchain.llms import OpenAI

from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

from langchain.chat_models import ChatOpenAI

key_1 = (os.environ["key"])



messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. How can I help you?"),
    HumanMessage(content="I'd like to understand string theory.")
]

def generate_response(input_text):
  

    chat = ChatOpenAI(
            openai_api_key = key_1,
            model='gpt-3.5-turbo'
    )
    
    messages2 = [
    SystemMessage(content="You are a helpful assistant trying to create questions to narrow down costs and timeframes for a client project, continue asking questions until you have a reasonable idea of the project, ask the most important questions first. Once the User inputs 'Finished' output the project description and answers to questions in a way compatible with prompting an LLM to produce a cost "),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. Can you tell me more about the project?"),
    HumanMessage(content= input_text)
    ]
    
    res2 = chat(messages2)
    st.write(res2)

    return res2

    



st.title('Project Details')

#openai_api_key = st.sidebar.text_input('OpenAI API Key')


with st.form('my_form'):
  text = st.text_area('Enter text:', 'Im making motion graphics fro a 10 minute youtube video')
  submitted = st.form_submit_button('Submit')
  if submitted and key_1.startswith('sk-'):
    generate_response(text)

with st.form('my_form2'):
  text = st.text_area('Enter text:', 'Im a video graphic designer')
  submitted = st.form_submit_button('Submit')
  if submitted and key_1.startswith('sk-'):
    generate_response(text)







'''

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

'''
