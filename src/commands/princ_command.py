import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.members = True
prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=intents)

# Discord Commands
class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ola(self, ctx):
        await ctx.send('Olá!')
        await ctx.send('Bom dia! / Boa tarde! / Boa noite!')   

# async def setup(bot):
#     await bot.add_cog(CommandCog(bot))  