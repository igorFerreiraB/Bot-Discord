# import os
import discord
from discord.ext import commands
# import openai

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=intents)

# openai.api_key = os.environ.get("key_chatgpt")

# ALL Discord Commands
class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ola(self, ctx):
        await ctx.send('Olá!')
        await ctx.send('Bom dia! / Boa tarde! / Boa noite!')   

async def setup(bot):
    await bot.add_cog(CommandCog(bot))  

# # OpenAI
# class CommandOpenai(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.command()
#     async def ask(ctx, *, question):
#         try:
#             conversation = [
#                 {"role": "system", "content": "Você é um bot de bate-papo."},
#                 {"role": "user", "content": question}
#             ]

#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=conversation
#             )

#             await ctx.send(response['choices'][0]['message']['content'])
#         except Exception as error:
#             await ctx.send(f"Ocorreu um erro: {str(error)}")
  
# async def setup2(bot):
#     await bot.add_cog(CommandOpenai(bot))  