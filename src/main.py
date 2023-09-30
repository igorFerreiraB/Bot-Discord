import discord
import os
from key import token



class MyClient(discord.Client):

    async def on_ready(self):
        print(f'{self.user} Conectou ao nosso servidor!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content == ('$ola'):
            await message.channel.send('olá!')
        elif message.content == ('?regras'):
            await message.channel.send(
                f"{message.author.mention.name}{os.linesep}\
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
            await message.author.send("Nivel menininha")

    async def member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f"{member.mention} Acabou de entrar no {guild.name}"
            await guild.system_channel.send(mensagem)

# TOKEN = token.get("TOKEN")
intents = discord.Intents.all()
intents.message_content = True

client = MyClient(intents=intents)
client.run("")