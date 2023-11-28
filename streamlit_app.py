import os
import streamlit as st
from langchain.llms import OpenAI

from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

from langchain.chat_models import ChatOpenAI



from shapely.geometry import Point, Polygon
import geopandas as gpd
import pandas as pd
import geopy

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

street = st.sidebar.text_input("Street", "75 Bay Street")
city = st.sidebar.text_input("City", "Toronto")
province = st.sidebar.text_input("Province", "Ontario")
country = st.sidebar.text_input("Country", "Canada")

geolocator = Nominatim(user_agent="GTA Lookup")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
location = geolocator.geocode(street+", "+city+", "+province+", "+country)

lat = location.latitude
lon = location.longitude

map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})

st.map(map_data) 

key_1 = (os.environ["key"])



messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. How can I help you?"),
    HumanMessage(content="I'd like to understand string theory.")
]

messages2 = [
    SystemMessage(content="You are a helpful assistant trying to create questions to narrow down costs and timeframes for a client project consisting of:" +  "continue asking questions until you have a reasonable idea of the project, ask the most important questions first. Once the User inputs 'Finished' output the project description and answers to questions in a way compatible with prompting an LLM to produce a cost "),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. Can you tell me more about the project?"),
    
    ]

messages3 = [
    SystemMessage(content="You are a helpful assistant trying to create questions to narrow down the cost and efficiency of a worker/freelancer, continue asking questions until you have a reasonable idea of what the person is capable of and what resources they have avaliable, ask the most important questions first. Once the User inputs 'Finished' output the project description and answers to questions in a way compatible with prompting an LLM to produce a cost when linked with a project description "),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. Can you tell me more about the project?")
    
    ]

messages4 = [
    SystemMessage(content="You are a helpful assistant trying to find the nearest major metropolitan urban center to a specified address, if the address is further than 100km away from the center you can call it rural and if it is further than 300km away from the nearest urban center you can call it remote "),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. Could you provide me with the address you'll be working from?")
    HumanMessage(content= street + city + province + country )
    
    ]

def generate_response2(input_text):
  

    chat = ChatOpenAI(
            openai_api_key = key_1,
            model='gpt-3.5-turbo'
    )

    messages2 = [
    SystemMessage(content="You are a helpful assistant trying to create questions to narrow down costs and timeframes for a client project consisting of:" +  "continue asking questions until you have a reasonable idea of the project, ask the most important questions first. Once the User inputs 'Finished' output the project description and answers to questions in a way compatible with prompting an LLM to produce a cost "),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. Can you tell me more about the project?"),
    HumanMessage(content= input_text)
    ]
    
    
    res2 = chat(messages2)
    st.write(res2.content)

    return res2


def generate_response3(input_text):
  

    chat = ChatOpenAI(
            openai_api_key = key_1,
            model='gpt-3.5-turbo'
    )

    messages3 = [
    SystemMessage(content="You are a helpful assistant trying to create questions to narrow down the cost and efficiency of a worker/freelancer, continue asking questions until you have a reasonable idea of what the person is capable of and what resources they have avaliable, ask the most important questions first. Once the User inputs 'Finished' output the project description and answers to questions in a way compatible with prompting an LLM to produce a cost when linked with a project description "),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. Can you tell me more about the project?"),
    HumanMessage(content= input_text)
    ]

    
    
    
    res2 = chat(messages3)
    st.write(res2.content)

    return res2

    



st.title('Project Details')

#openai_api_key = st.sidebar.text_input('OpenAI API Key')


with st.form('my_form'):
  text = st.text_area('Enter text:', 'Im making motion graphics for a 10 minute youtube video')
  submitted = st.form_submit_button('Submit')
  if submitted and key_1.startswith('sk-'):

    messages2.append(text)
    res = generate_response2(text)

    messages2.append(res)

st.title('Your Experience')

with st.form('my_form2'):
  text = st.text_area('Enter text:', 'Im a video graphic designer')
  submitted = st.form_submit_button('Submit')
  if submitted and key_1.startswith('sk-'):


    messages3.append(text)
    
    res = generate_response3(text)

    messages3.append(res)








