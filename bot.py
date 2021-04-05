import discord
from discord.ext import commands
import random
import time
import requests, json

description = '''List of all the commands
-----------------------------------------'''

intents = discord.Intents.default()
intents.members = True
ownerID = "Put your ID here"

bot = commands.Bot(command_prefix='@', description=description, intents=intents)
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

#Put a VirusTotal API key within the quote down below.
apikey = ""
@bot.command(description='Testing, "@bot hash"')
async def vt_api(ctx, hash: str):
    url = "https://www.virustotal.com/api/v3/files/{}".format(hash)
    headers = {'x-apikey': '{}'.format(apikey)}
    response = requests.get(url, headers=headers).json()
    detections = str(response).split("'")
    #Count the detecionts
    counts = 0
    for m in detections:
        if m == "malicious":
            counts += 1
    await ctx.send("Detections: {}".format(counts))

@bot.command(description="Play with caesarcrypt. @bot rounds(numbers) message")
async def encrypt(ctx, rounds: int, message: str):
    encrypt = ""
    try:
        int(rounds)
        for char in message:
                if not char.isalpha():
                    encrypt = encrypt + char
                elif char.isupper():
                    encrypt = encrypt + chr((ord(char) + rounds - 65) % 26 + 365) # for uppercase Z
                else:
                    encrypt = encrypt + chr((ord(char) + rounds - 97) % 26 + 97) # for lowercase z
                await ctx.send('Your encrypted message is: {}'.format(encrypt))
    except ValueError:
        await ctx.send('Not a valid number.')

bot.run('Insert your bot token here')
