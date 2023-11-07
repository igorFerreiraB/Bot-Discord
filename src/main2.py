import discord
import os
from openai import OpenAI
client = OpenAI()

from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
my_secret_key = os.environ['token']
# openai.api_key = os.environ['key_chatgpt'] 

@bot.event
async def on_ready():
    print("-" * 30)
    print(f'Logged in as {bot.user.name}')
    print("-" * 30)

    await bot.load_extension("commands.princ_command")
    await bot.tree.sync()

    print('All extensions loaded')

bot.run(my_secret_key)
