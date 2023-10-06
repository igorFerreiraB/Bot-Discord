import discord
import os
import logging
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

# class MyClient(discord.Client):

#     async def on_ready(self):
#         print(f'{self.user} Conectou ao nosso servidor!')

#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')
#         if message.content == ('$ola'):
#             await message.channel.send(f'Olá! {message.author.mention}, Como vai ?')
#         elif message.content == ('?regras'):
#             await message.channel.send(
#                 f"{message.author.mention}{os.linesep}\
#                 \n1. É proibido usar sapatos de cores diferentes em dias pares.\
#                 \n2. Todo mundo deve usar um chapéu de abacaxi às segundas-feiras.\
#                 \n3. É ilegal falar com esquilos em voz alta.\
#                 \n4. Todos os sanduíches devem ser comidos de trás para frente às quartas-feiras.\
#                 \n5. Os elevadores só podem ser usados por pessoas que estejam cantando uma música de karaokê.\
#                 \n6. É obrigatório andar de costas em calçadas ímpares.\
#                 \n7. Deve-se dar um aperto de mão a todos os cães que encontrar na rua.\
#                 \n8. É ilegal usar guarda-chuvas em dias de sol.\
#                 \n9. É proibido contar piadas às quintas-feiras.\
#                 \n10. Todo mundo deve usar uma gravata borboleta em forma de pena aos domingos."
#             )
#         elif message.content == ('?nivel'):
#             await message.author.send(f"{message.author.mention}{os.linesep}Nivel menininha")
#         elif message.content == ('?help'):
#             await message.channel.send(
#                 f"{message.author.mention}{os.linesep}\
#                 \nAqui estão todos os meus comandos:\
#                 \n?regras: Você vera as regras importantíssimas do server\
#                 \n$ola: Vou te dar um olá\
#                 \n?nivel: Vou te mostrar o quão grande você é\
#                 \n?help: Você vera oque eu posso fazer"
#             )

#     async def on_member_join(self, member):
#         guild = member.guild
#         if guild.system_channel is not None:
#             mensagem = f"{member.mention} Acabou de entrar no {guild.name}"
#             await guild.system_channel.send(mensagem)

# client = MyClient(intents=intents)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# client.run(os.environ['token'], log_handler=handler)


async def on_ready(self):
    print(f'{self.user} Conectou ao nosso servidor!')

async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')
    if message.content == ('$ola'):
        await message.channel.send(f'Olá! {message.author.mention}, Como vai ?')
    elif message.content == ('?regras'):
        await message.channel.send(
            f"{message.author.mention}{os.linesep}\
            \n1. É proibido usar sapatos de cores diferentes em dias pares.\
            \n2. Todo mundo deve usar um chapéu de abacaxi às segundas-feiras.\
            \n3. É ilegal falar com esquilos em voz alta.\
            \n4. Todos os sanduíches devem ser comidos de trás para frente às quartas-feiras.\
            \n5. Os elevadores só podem ser usados por pessoas que estejam cantando uma música de karaokê.\
            \n6. É obrigatório andar de costas em calçadas ímpares.\
            \n7. Deve-se dar um aperto de mão a todos os cães que encontrar na rua.\
            \n8. É ilegal usar guarda-chuvas em dias de sol.\
            \n9. É proibido contar piadas às quintas-feiras.\
            \n10. Todo mundo deve usar uma gravata borboleta em forma de pena aos domingos."
        )
    elif message.content == ('?nivel'):
        await message.author.send(f"{message.author.mention}{os.linesep}Nivel menininha")
    elif message.content == ('?help'):
        await message.channel.send(
            f"{message.author.mention}{os.linesep}\
            \nAqui estão todos os meus comandos:\
            \n?regras: Você vera as regras importantíssimas do server\
            \n$ola: Vou te dar um olá\
            \n?nivel: Vou te mostrar o quão grande você é\
            \n?help: Você vera oque eu posso fazer"
        )

async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        mensagem = f"{member.mention} Acabou de entrar no {guild.name}"
        await guild.system_channel.send(mensagem)