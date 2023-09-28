import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
        if message.content.startswith('?regras'):
            await message.channel.send(
                f"{message.author.name}{os.linesep}\
                1. É proibido usar sapatos de cores diferentes em dias pares.{os.linesep}\
                2. Todo mundo deve usar um chapéu de abacaxi às segundas-feiras.\
                3. É ilegal falar com esquilos em voz alta.\
                4. Todos os sanduíches devem ser comidos de trás para frente às quartas-feiras.\
                5. Os elevadores só podem ser usados por pessoas que estejam cantando uma música de karaokê.\
                6. É obrigatório andar de costas em calçadas ímpares.\
                7. Deve-se dar um aperto de mão a todos os cães que encontrar na rua.\
                8. É ilegal usar guarda-chuvas em dias de sol.\
                9. É proibido contar piadas às quintas-feiras.\
                10. Todo mundo deve usar uma gravata borboleta em forma de pena aos domingos."
            )

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')