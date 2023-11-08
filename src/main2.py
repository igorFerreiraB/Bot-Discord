import discord
import os

from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
load_dotenv()

MY_GUILD = discord.Object(id=1034181969409474682)
MY_SECRET_TOKEN = os.environ.get("token")
prefix = "!"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

def sep(text):
    size = len(text) + 4
    print("-" * size)    
    print(f"  {text}")
    print("-" * size) 

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)  

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

    @bot.event
    async def on_ready():
        sep(f'Conectou-se {bot.user.name}')
        await bot.load_extension("commands.princ_command")
        await bot.load_extension("utils.chat_bot")
        await bot.tree.sync()

client = MyClient(intents=intents)

if __name__ == '__main__':
    bot.run(MY_SECRET_TOKEN)
