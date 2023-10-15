import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@commands.command()
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Olá, {interaction.user.mention}')

bot.add_command(hello)    