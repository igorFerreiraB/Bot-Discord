from typing import Optional

import logging
import os
import discord

from commands import hello
from discord import app_commands
from dotenv import load_dotenv
load_dotenv()

MY_GUILD = discord.Object(id=1034181969409474682)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

client = MyClient(intents=intents)

@client.event
async def on_ready():
    print('-' * 60)
    print(f'Acabou de entrar {client.user} (ID: {client.user.id})')
    print('-' * 60)

hello()

@client.tree.command()
@app_commands.describe(member='member')
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
    member = member or interaction.user
    await interaction.response.send_message(f'{member.mention} entrou no dia {discord.utils.format_dt(member.joined_at)}')

@client.tree.context_menu(name='Data que entrou')
async def show_join_date(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f'{member.mention} está conosco desde o dia {discord.utils.format_dt(member.joined_at)}')

@client.tree.context_menu(name='Reportar está menssagem')
async def report_message(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(
        f'Obrigado por denunciar esta mensagem por {message.author.mention} para nossa moderação.', ephemeral=False
    )

    log_channel = interaction.guild.get_channel(0) 

    embed = discord.Embed(title='Reportar está menssagem')
    if message.content:
        embed.description = message.content

    embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    embed.timestamp = message.created_at

    url_view = discord.ui.View()
    url_view.add_item(discord.ui.Button(label='ir para a menssagem', style=discord.ButtonStyle.url, url=message.jump_url))

    await log_channel.send(embed=embed, view=url_view) 


client.run(os.environ['token'],log_handler=handler)

