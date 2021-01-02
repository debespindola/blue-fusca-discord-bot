import os

import discord 
from dotenv import load_dotenv 

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='/')

@bot.command()
async def fusca(ctx, arg):
    await ctx.send(f'tapa em {arg}')

bot.run(TOKEN)
