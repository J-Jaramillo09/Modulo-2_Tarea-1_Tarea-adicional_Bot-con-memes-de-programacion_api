#Importaciones 

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from funciones_API import get_duck_image_url, get_dog_image_url, random_image

#Permisos del bot

intents = discord.Intents.default()
intents.message_content = True
bot=commands.Bot(command_prefix='!',intents=intents)

#Imágenes de patos.

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#Imágenes de perros.

@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando dog, 
    el programa llama a la función get_dog_image_url'''
    image_url_dog = get_dog_image_url()
    await ctx.send(image_url_dog)

#Imágenes random de perros y de patos.

@bot.command('randompic')
async def randompic(ctx):
    image_url_random = random_image()
    await ctx.send(image_url_random)

load_dotenv(dotenv_path="token.env")

TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)





