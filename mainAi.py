#導入 Discord.py
import discord
from discord import app_commands
import configload
from function import chatAI
import variable
import sys
sys.tracebacklimit = 0
lastDate = ''
guild_id = configload.getConfigSetting("Credentials", "Guild_id")
token = configload.getConfigSetting("Credentials", "Token")
target = configload.getConfigSetting("Credentials", "TargetUser")
drawLotsHK_room_ID = configload.getConfigSetting("Credentials", "DrawLotsHK_room_ID")
drawCard_room_ID = configload.getConfigSetting("Credentials", "DrawCard_room_ID")
textChannel = configload.getConfigSetting("Credentials", "TextChannel")
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.all())
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await bot.sync(guild = discord.Object(id=guild_id)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f'目前登入身份：{client.user}')

client = aclient()
bot = app_commands.CommandTree(client)

variable.setClient(client)
variable.setToken(token)
variable.setTarget(target)

@bot.command(guild = discord.Object(id=guild_id), name = '聊天ai', description='openAI chatGPT')
async def chat(interaction: discord.Interaction, 對話: str):
    await interaction.response.defer(thinking=True)
    text = chatAI.chat(對話)
    if interaction.user.nick == None:
        name = interaction.user.name
    else:
        name = interaction.user.nick

    await interaction.followup.send(f'{name}:{對話} \n\nAI:{text}')

client.run(token)

