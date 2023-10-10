from typing import Optional

import main
import logging
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
load_dotenv()


MY_GUILD = discord.Object(id=1034181969409474682)


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Acabou de entrar {client.user} (ID: {client.user.id})')
    print('-' * 30)


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Olá, {interaction.user.mention}')


@client.tree.command()
@app_commands.describe(
    primeiro_número='Você vai passar  valor para somar, subtrair, multiplicar, ou dividir',
    segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
)
async def somar(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
    await interaction.response.send_message(
        f'{primeiro_número} + {segundo_número} = {primeiro_número + segundo_número}'
        )
    

@client.tree.command()
@app_commands.describe(
    primeiro_número='Você vai passar  valor para somar, subtrair, multiplicar, ou dividir',
    segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
)
async def subtrair(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
    await interaction.response.send_message(
        f'{primeiro_número} - {segundo_número} = {primeiro_número - segundo_número}'
        )    


@client.tree.command()
@app_commands.describe(
    primeiro_número='Você vai passar  valor para somar, subtrair, multiplicar, ou dividir',
    segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
)
async def multiplicar(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
    await interaction.response.send_message(
        f'{primeiro_número} * {segundo_número} = {primeiro_número * segundo_número}'
        )
    

@client.tree.command()
@app_commands.describe(
    primeiro_número='Você vai passar  valor para somar, subtrair, multiplicar, ou dividir',
    segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
) 
async def dividir(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
    await interaction.response.send_message(
        f'{primeiro_número} / {segundo_número} = {primeiro_número / segundo_número}'
        )


@client.tree.command()
@app_commands.rename(text_to_send='text')
@app_commands.describe(text_to_send='Texto que sera enviado no canal atual da menssagem')
async def send(interaction: discord.Interaction, text_to_send: str):
    await interaction.response.send_message(text_to_send)


@client.tree.command()
@app_commands.describe(member='member')
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
    
    member = member or interaction.user

    await interaction.response.send_message(f'{member.mention} entrou no dia {discord.utils.format_dt(member.joined_at)}')

# This context menu command only works on members
@client.tree.context_menu(name='Data que entrou')
async def show_join_date(interaction: discord.Interaction, member: discord.Member):
    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member.mention} está conosco desde o dia {discord.utils.format_dt(member.joined_at)}')



@client.tree.context_menu(name='Reportar está menssagem')
async def report_message(interaction: discord.Interaction, message: discord.Message):
    # We're sending this response message with ephemeral=True, so only the command executor can see it
    await interaction.response.send_message(
        f'Obrigado por denunciar esta mensagem por {message.author.mention} para nossa moderação.', ephemeral=False
    )

    # Handle report by sending it into a log channel
    log_channel = interaction.guild.get_channel(0)  # replace with your channel id

    embed = discord.Embed(title='Reportar está menssagem')
    if message.content:
        embed.description = message.content

    embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    embed.timestamp = message.created_at

    url_view = discord.ui.View()
    url_view.add_item(discord.ui.Button(label='ir para a menssagem', style=discord.ButtonStyle.url, url=message.jump_url))

    await log_channel.send(embed=embed, view=url_view)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
client.run(os.environ['token'], log_handler=handler)