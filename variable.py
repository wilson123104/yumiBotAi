import discord
import configload 

client: discord.Client
token:str
target:str
chatAICookie = configload.getConfigSetting("Credentials", "ChatAICookie")

def setClient(client1):
    global client 
    client = client1

def setToken(token1):
    global token 
    token = token1

def setTarget(target1):
    global target 
    target = target1