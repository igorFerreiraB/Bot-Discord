import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

MY_GUILD_ID = 1034181969409474682
MY_SECRET_TOKEN = os.environ.get("key_discord")
prefix = "!"

intents = discord.Intents.default()
intents.all()       

bot = commands.Bot(command_prefix=prefix, intents=intents)

# Mostra linhas sobre o Bot que conectou
def sep(text):
    size = len(text) + 4
    print("-" * size)
    print(f"  {text}")
    print("-" * size)

@bot.event
async def on_ready():
    sep(f'CONECTOU-SE {bot.user.name}')

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user.name:
        return

    if ctx.content.startswith('$hello'):
        await ctx.channel.send(f'Hello! {ctx.author.mention}!')

bot.run(MY_SECRET_TOKEN)