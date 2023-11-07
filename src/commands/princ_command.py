from discord.ext import commands

class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ola(self, ctx):
        await ctx.send('Olá!')

async def setup(bot):
    await bot.add_cog(CommandCog(bot))   