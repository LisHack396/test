import os
from dotenv import load_dotenv
from langchain.llms import openai
from langchain_openai import ChatOpenAI
from langchain.schema import (AIMessage, HumanMessage)
from dataset_api import get_api_data

load_dotenv()
openai.apikey = os.getenv('OPENAI_API_KEY')
api_key = openai.apikey

def asking_chatbot(message : str):
    place = message.split('in')[-1].split()
    data = get_api_data(place)
    if data:
        chat = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.7, openai_api_key=api_key)
        chat.invoke([
            HumanMessage(content=message),
            AIMessage(content=f"Weather: \n {data}")
        ])
