from discord.ext import commands
from openai import OpenAI
client = OpenAI()

# ALL Discord Commands
class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ola(self, *, ctx:str):
        gtp_answer = response(ctx)
        await ctx.send(gtp_answer)

async def setup(bot):
    await bot.add_cog(CommandCog(bot))  

# OpenAI


def response(messages):
    message = [
        {"role": "system", "content": str(messages)},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]

    response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = messages,
    max_tokens = 1024
    )

    retorno = response.choices[0].message.content 
    return retorno