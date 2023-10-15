from typing import Optional

from commands import hello
import logging
import os
import discord
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

'''ESTÃO EM OUTRA AREA'''

# @client.tree.command()
# async def hello(interaction: discord.Interaction):
#     await interaction.response.send_message(f'Olá, {interaction.user.mention}')

'''ESTÃO EM OUTRA AREA'''

# @client.tree.command()
# @app_commands.describe(
#     primeiro_número='Você vai passar  valor para somar, subtrair, multiplicar, ou dividir',
#     segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
# )
# async def somar(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
#     await interaction.response.send_message(
#         f'{primeiro_número} + {segundo_número} = {primeiro_número + segundo_número}'
#         )
    
# @client.tree.command()
# @app_commands.describe(
#     primeiro_número='Você vai passar  valor para somar, subtrair, multiplicar, ou dividir',
#     segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
# )
# async def subtrair(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
#     await interaction.response.send_message(
#         f'{primeiro_número} - {segundo_número} = {primeiro_número - segundo_número}'
#         )    

# @client.tree.command()
# @app_commands.describe(
#     primeiro_número='Você vai passar  valor para somar, subtrair, multiplicar, ou dividir',
#     segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
# )
# async def multiplicar(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
#     await interaction.response.send_message(
#         f'{primeiro_número} * {segundo_número} = {primeiro_número * segundo_número}'
#         )
    
# @client.tree.command()
# @app_commands.describe(
#     primeiro_número='Você vai passar valor para somar, subtrair, multiplicar, ou dividir',
#     segundo_número='Você vai passar outro valor para somar, subtrair, multiplicar, ou dividir',
# ) 
# async def dividir(interaction: discord.Interaction, primeiro_número: float, segundo_número: float):
#     await interaction.response.send_message(
#         f'{primeiro_número} / {segundo_número} = {primeiro_número / segundo_número}'
#         )

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


client.run(os.environ['token'], log_handler=handler)


# async def on_message(self, message):
#     print(f'Message from {message.author}: {message.content}')
#     if message.content == ('$ola'):
#         await message.channel.send(f'Olá! {message.author.mention}, Como vai ?')
#     elif message.content == ('?regras'):
#         await message.channel.send(
#             f"{message.author.mention}{os.linesep}\
#             \n1. É proibido usar sapatos de cores diferentes em dias pares.\
#             \n2. Todo mundo deve usar um chapéu de abacaxi às segundas-feiras.\
#             \n3. É ilegal falar com esquilos em voz alta.\
#             \n4. Todos os sanduíches devem ser comidos de trás para frente às quartas-feiras.\
#             \n5. Os elevadores só podem ser usados por pessoas que estejam cantando uma música de karaokê.\
#             \n6. É obrigatório andar de costas em calçadas ímpares.\
#             \n7. Deve-se dar um aperto de mão a todos os cães que encontrar na rua.\
#             \n8. É ilegal usar guarda-chuvas em dias de sol.\
#             \n9. É proibido contar piadas às quintas-feiras.\
#             \n10. Todo mundo deve usar uma gravata borboleta em forma de pena aos domingos."
#         )
#     elif message.content == ('?nivel'):
#         await message.author.send(f"{message.author.mention}{os.linesep}Nivel menininha")
#     elif message.content == ('?help'):
#         await message.channel.send(
#             f"{message.author.mention}{os.linesep}\
#             \nAqui estão todos os meus comandos:\
#             \n?regras: Você vera as regras importantíssimas do server\
#             \n$ola: Vou te dar um olá\
#             \n?nivel: Vou te mostrar o quão grande você é\
#             \n?help: Você vera oque eu posso fazer"
#         )

# async def on_member_join(self, member):
#     guild = member.guild
#     if guild.system_channel is not None:
#         mensagem = f"{member.mention} Acabou de entrar no {guild.name}"
#         await guild.system_channel.send(mensagem)

