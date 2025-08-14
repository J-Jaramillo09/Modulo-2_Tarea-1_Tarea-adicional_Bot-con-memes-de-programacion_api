import discord
from discord.ext import commands
import os
import requests
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
bot=commands.Bot(command_prefix='!',intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
# Otro API
def get_dog_image_url():    
    url_dog = 'https://random.dog/woof.json'
    res_dog = requests.get(url_dog)
    data_dog = res_dog.json()
    return data_dog ['url']


@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url_dog = get_dog_image_url()
    await ctx.send(image_url_dog)

# api random
def random_image():
    img_enviada = [get_dog_image_url(),get_duck_image_url()]
    return random.choice(img_enviada)
@bot.command('randompic')
async def randompic(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url_random = random_image()
    await ctx.send(image_url_random)

load_dotenv(dotenv_path="token.env")

TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)





