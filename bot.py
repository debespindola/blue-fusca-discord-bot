import os
import discord 
import random

from dotenv import load_dotenv 
from discord.ext import commands

from gifs import gifs

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='/')

@bot.command()
async def tapa(ctx, arg):
    await ctx.send(f'tapa em {arg} \n{random.choice(gifs)}')

bot.run(TOKEN)
