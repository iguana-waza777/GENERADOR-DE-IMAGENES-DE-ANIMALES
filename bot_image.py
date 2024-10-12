import discord
import requests
from discord.ext import commands
import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
intents.message_content = True

# Crear un bot en la variable bot y transferirle los privilegios
bot = commands.Bot(command_prefix='!', intents=intents)

# Funciones para obtener la imagen de cada API
def get_random_dog():
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    data = response.json()
    return data['url']

def get_random_fox():
    url = 'https://randomfox.ca/floof/'
    response = requests.get(url)
    data = response.json()
    return data['image']

def get_random_duck():
    url = 'https://random-d.uk/api/random'
    response = requests.get(url)
    data = response.json()
    return data['url']

# Diccionario que contiene las funciones para obtener los memes
meme_funcs = {
    'animales': [
        get_random_dog,
        get_random_fox,
        get_random_duck
    ]
}

@bot.command()
async def animales(ctx):
    '''Responde con un meme de animales'''
    meme_func = random.choice(meme_funcs['animales'])
    meme_url = meme_func()
    await ctx.send(meme_url)

bot.run('MTI4NzQxNjYyNzE4NDI3MTM3MA.GytV2l.gZtUgf6MADlan4rH0ZGY0ig4QGeJ1r4SllBnVM')

