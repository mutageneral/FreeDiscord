import discord
from discord.ext import commands
import random
import time
import requests
import json
from config import *

description = '''List of all the commands
-----------------------------------------
This bot is based off of/is the FreeDiscord bot made by SKbotNL, ItsJustLag, 
Recall/Recallwhoiam, Quirinus, and antistalker.
Project URL: https://github.com/FreeTechnologies/FreeDiscord/
Support Server: https://discord.gg/VyNxSt55gj
-----------------------------------------'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    # What gets printed in the terminal when the bot is succesfully logged in
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.load_extension("cogs.general")
bot.load_extension("cogs.utils")
bot.load_extension("cogs.moderation")
bot.load_extension("cogs.settings")
bot.load_extension("cogs.caesarcrypt")
bot.load_extension("cogs.help")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        em = discord.Embed(title = "You do not have permission to do that.")
        await ctx.send(embed = em)
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title = "Your command is missing an argument.")
        await ctx.send(embed = em)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    em = discord.Embed(title = left + right)
    await ctx.send(embed = em)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in N-N format."""
    try:
        rolls, limit = map(int, dice.split('-'))
    except Exception:
        em = discord.Embed(title = "Format has to be in `Number-Number`")
        await ctx.send(embed = em)
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    em = discord.Embed(title = result)
    await ctx.send(embed = em)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    if "@everyone" in choices:
        em = discord.Embed(title = "Nice try, sadly that won't work here.")
        await ctx.send(embed = em)
    else:
        if "@here" in choices:
            em = discord.Embed(title = "Nice try, sadly that won't work here.")
            await ctx.send(embed = em)
        else:
            em = discord.Embed(title = random.choice(choices))
            await ctx.send(embed = em)
            
apikey = virustotal_api

@bot.command(description='Testing, "@bot hash"')
async def vt(ctx, hash: str):
    """VirusTotal Integration"""
    url = "https://www.virustotal.com/api/v3/files/{}".format(hash)
    headers = {'x-apikey': '{}'.format(apikey)}
    response = requests.get(url, headers=headers).json()
    detections = str(response).split("'")
    # Count the detecionts
    counts = 0
    for m in detections:
        if m == "malicious":
            counts += 1
    em = discord.Embed(title = "Detections: {}".format(counts))
    await ctx.send(embed = em)


bot.run(bot_token)
