# import discord
# import os
# from discord.ext import commands
# from discord import app_commands
# from dotenv import load_dotenv

# load_dotenv()

# MY_GUILD_ID = 1034181969409474682
# MY_SECRET_TOKEN = os.environ.get("key_discord")
# prefix = "!"

# intents = discord.Intents.default()
# intents.messages = True
# intents.members = True

# bot = commands.Bot(command_prefix=prefix, intents=intents)

# def sep(text):
#     size = len(text) + 4
#     print("-" * size)
#     print(f"  {text}")
#     print("-" * size)

# class MyClient(discord.Client):
#     def __init__(self, *, intents: discord.Intents):
#         super().__init__(intents=intents)
#         self.tree = app_commands.CommandTree(self)  

#     async def setup_hook(self):
#         self.tree.copy_global_to(guild=MY_GUILD_ID)
#         await self.tree.sync(guild=MY_GUILD_ID)

# client = MyClient(intents=intents)

# @bot.event
# async def on_ready():
#     sep(f'Conectou-se {bot.user.name}')
#     await bot.tree.sync()

# @client.tree.command()
# @app_commands.describe(member='member')
# async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
#     member = member or interaction.user
#     await interaction.response.send_message(f'{member.mention} entrou no dia {discord.utils.format_dt(member.joined_at)}')

# @client.tree.context_menu(name='Data que entrou')
# async def show_join_date(interaction: discord.Interaction, member: discord.Member):
#     await interaction.response.send_message(f'{member.mention} está conosco desde o dia {discord.utils.format_dt(member.joined_at)}')

# @client.tree.context_menu(name='Reportar está menssagem')
# async def report_message(interaction: discord.Interaction, message: discord.Message):
#     await interaction.response.send_message(
#         f'Obrigado por denunciar esta mensagem por {message.author.mention} para nossa moderação.', ephemeral=False
#     )

#     log_channel = interaction.guild.get_channel(0) 

#     embed = discord.Embed(title='Reportar está menssagem')
#     if message.content:
#         embed.description = message.content

#     embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
#     embed.timestamp = message.created_at

#     url_view = discord.ui.View()
#     url_view.add_item(discord.ui.Button(label='ir para a menssagem', style=discord.ButtonStyle.url, url=message.jump_url))

#     await log_channel.send(embed=embed, view=url_view) 

# bot.run(MY_SECRET_TOKEN)

import discord
import os
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from dotenv import load_dotenv

load_dotenv()

MY_GUILD_ID = 1034181969409474682
MY_SECRET_TOKEN = os.environ.get("key_discord")
prefix = "!"

intents = discord.Intents.default()
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix=prefix, intents=intents)
slash = SlashCommand(bot, sync_commands=True)

def sep(text):
    size = len(text) + 4
    print("-" * size)
    print(f"  {text}")
    print("-" * size)

@bot.event
async def on_ready():
    sep(f'Conectou-se {bot.user.name}')

@bot.event
async def on_slash_command(ctx: SlashContext):
    # Adicione esta função caso queira executar algo quando um slash command for chamado.
    pass

@slash.slash(name="joined", description="Get join date of a member")
async def joined(ctx: SlashContext, member: discord.Member):
    await ctx.send(f'{member.mention} entrou no dia {discord.utils.format_dt(member.joined_at)}')

@slash.context_menu(target=1, name='Mostrar Data de Entrada')
async def show_join_date(ctx: SlashContext, member: discord.Member):
    await ctx.send(f'{member.mention} está conosco desde o dia {discord.utils.format_dt(member.joined_at)}')

bot.run(MY_SECRET_TOKEN)