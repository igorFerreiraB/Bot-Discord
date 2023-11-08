import os
from discord.ext import commands
# from openai import OpenAI
# client = OpenAI()

# my_secret_key = os.environ['key_chatgpt']

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
# def response(messages):
#     response = client.chat.completions.create(
#     model = "gpt-3.5-turbo",
#     messages = messages,
#     max_tokens = 1024,
    
#     message = [
#         {"role": "system", "content": str(messages)}
#     ]
#     )

#     retorno = response.choices[0].message.content 
#     return retorno
