import sys
import variable
sys.path.append("..")
from pyChatGPT import ChatGPT
key = variable.chatAICookie
api = ChatGPT(key)

def chat(str:str):
    res = api.send_message(str)
    return res['message']