import discord
from discord.ext import commands
import random
import time
import requests
import json

description = '''List of all the commands
-----------------------------------------
This bot is based off of/is the FreeDiscord bot made by SKbotNL, ItsJustLag, 
Recall/Recallwhoiam, Quirinus, and antistalker.
Project URL: https://github.com/FreeTechnologies/FreeDiscord/
Support Server: https://discord.gg/VyNxSt55gj
-----------------------------------------'''

intents = discord.Intents.default()
intents.members = True
ownerID = 'Insert-YOUR-Discord-ID-here'

bot = commands.Bot(command_prefix='@',
                   description=description, intents=intents)
# bot.remove_command('help')


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


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have permission to do that")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Your command is missing an argument")

# skbotnl i swear to god if you remove this one more time im going to-
@bot.command()
async def setStatus(ctx, status):
    """Sets the status of the bot. Owner only."""
    if str(ctx.message.author.id) == ownerID:
        await bot.change_presence(activity=discord.Game(name=status))
        await ctx.send("Bot status successfully changed to " + status + "!")
    else:
        await ctx.send("listen here bud the command says 'Owner Only' for a reason")


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in N-N format."""
    try:
        rolls, limit = map(int, dice.split('-'))
    except Exception:
        await ctx.send('Format has to be in N-N!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    if "@everyone" in choices:
        await ctx.send("Hahaha nice try")
    else:
        if "@here" in choices:
            await ctx.send("Hahaha nice try")
        else:
            await ctx.send(random.choice(choices))

# Require "import json" to run.
# Put a VirusTotal API key within the quote down below.
apikey = "VIRUSTOTAL_API_KEY_HERE"


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
    await ctx.send("Detections: {}".format(counts))


bot.run('Insert-bot-token-here')
