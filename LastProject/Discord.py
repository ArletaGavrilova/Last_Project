import discord
from discord.ext import commands
import random 
import os 
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')   

@bot.command()
async def WhatIsClimatChange(ctx):
    await ctx.send('''Что такое изменение климата? Под изменением климата понимают долгосрочные температурные изменения и изменение погодных условий. 
                   Эти изменения могут быть естественными, вызванными изменениями в активности Солнца или крупными извержениями вулканов. ''')

@bot.command()
async def random_img_for_(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            #В переменную кладём файл, который преобразуется в файл библиотеки Discord!
            picture = discord.File(f)
            await ctx.send(file=picture)

@bot.command()
async def helpme(ctx):
    await ctx.send('''Вот что ты можешь у меня спросить: Что такое изменение климата? - WhatIsClimatChange,   
                    если напишешь это и имя человека то покажеться кто зашёл в группу - joined, 
                    можешь написать любое слово после этого и написать число повтора - repeat,  
                    бот тебя поприветствует - hello.''')

bot.run("your token")