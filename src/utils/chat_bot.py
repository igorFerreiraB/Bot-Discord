import os
import discord
import openai
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=intents)

openai.api_key = os.environ.get("key_chatgpt")

# OpenAI
class ChatBotCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self,ctx, *, question):
        try:
            conversation = [
                {"role": "system", "content": "Você é um bot de bate-papo."},
                {"role": "user", "content": question}
            ]   

            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                messages=conversation,
                max_tokens=50
            )

            await ctx.send(response['choices'][0]['message']['content'])
        except Exception as error:
            await ctx.send(f"Ocorreu um erro: {str(error)}")
  
async def setup(bot):
    await bot.add_cog(ChatBotCog(bot))  