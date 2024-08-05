import os
import dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import (AIMessage, HumanMessage)
from dataset_api import get_api_data

dotenv.load_dotenv()
OpenAI.apikey = os.getenv('OPENAI_API_KEY')
api_key = OpenAI.apikey

def asking_chatbot(message : str):
    place = message.split('in')[-1].split()
    data = get_api_data(place)
    if data:
        chat = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.7, openai_api_key=api_key)
        chat.invoke([
            HumanMessage(content=message),
            AIMessage(content=f"Weather: \n {data}")
        ])
