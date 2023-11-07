import discord
import os

from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.load_extension("commands.princ_command")
    await bot.tree.sync()

    print('All extensions loaded')

bot.run(os.environ['token'])
