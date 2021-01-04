import os
import discord 
import random
import datetime
import asyncio

from dotenv import load_dotenv 
from discord.ext import commands, tasks
from randomtimestamp import randomtimestamp

from gifs import gifs

#================================================

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='/')

#=================================================

@bot.command()
async def tapa(ctx, arg):
    await ctx.send(f'tapa em {arg} \n{random.choice(gifs)}')

@bot.command()
async def appear_fusca(ctx):
    while True:
        await ctx.send(f'FUSCA AZUL PASSANDOOO!!! https://media3.giphy.com/media/56zX8No3gs1e72gflB/giphy.gif')
        await asyncio.sleep(10)


#==================================================

bot.run(TOKEN)
