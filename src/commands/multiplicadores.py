import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@commands.command()
@app_commands.describe(
    primeiro_número='Você vai passar um valor para somar, subtrair, multiplicar, ou dividir',
    segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
)
async def somar(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
    await interaction.response.send_message(
        f'{primeiro_número} + {segundo_número} = {primeiro_número + segundo_número}'
        )
    
@commands.command()
@app_commands.describe(
    primeiro_número='Você vai passar  valor para somar, subtrair, multiplicar, ou dividir',
    segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
)
async def subtrair(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
    await interaction.response.send_message(
        f'{primeiro_número} - {segundo_número} = {primeiro_número - segundo_número}'
        )    

@commands.command()
@app_commands.describe(
    primeiro_número='Você vai passar  valor para somar, subtrair, multiplicar, ou dividir',
    segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
)
async def multiplicar(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
    await interaction.response.send_message(
        f'{primeiro_número} * {segundo_número} = {primeiro_número * segundo_número}'
        )
    
@commands.command()
@app_commands.describe(
    primeiro_número='Você vai passar valor para somar, subtrair, multiplicar, ou dividir',
    segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
) 
async def dividir(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
    await interaction.response.send_message(
        f'{primeiro_número} / {segundo_número} = {primeiro_número / segundo_número}'
        )
    
bot.add_command(
    dividir,
    multiplicar,
    subtrair,
    somar
    )    