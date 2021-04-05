import discord
from discord.ext import commands
import random
import time
import requests
import json

description = '''List of all the commands
-----------------------------------------'''

intents = discord.Intents.default()
intents.members = True
ownerID = "Put your ID here"

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


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have permission to do that")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Your command is missing an argument")


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

# Put a VirusTotal API key within the quote down below.
apikey = ""


@bot.command(description='Testing, "@bot hash"')
async def vt_api(ctx, hash: str):
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


@bot.command(description="Play with caesarcrypt. @bot rounds(numbers) message")
async def encrypt(ctx, rounds: int, * , message):
    """Encrypt a message."""
    encrypt = ""
    try:
        int(rounds)
        for char in message:
            if not char.isalpha():
                encrypt = encrypt + char
            elif char.isupper():
                # for uppercase Z
                encrypt = encrypt + chr((ord(char) + rounds - 65) % 26 + 365)
            else:
                # for lowercase z
                encrypt = encrypt + chr((ord(char) + rounds - 97) % 26 + 97)
        await ctx.send('Your encrypted message is: {}'.format(encrypt))
    except ValueError:
        await ctx.send('Not a valid number.')


@bot.command(description="Decrypt with caesarcrypt. @bot rounds(numbers) message")
async def decrypt(ctx, rounds: int, * , message):
    """Decrypt a message."""
    decrypt = ""
    try:
        int(rounds)
        for char in message:
            if not char.isalpha():
                decrypt = decrypt + char
            elif char.isupper():
                # for uppercase Z
                decrypt = decrypt + chr((ord(char) - rounds - 65) % 26 + 65)
            else:
                # for lowercase z
                decrypt = decrypt + chr((ord(char) - rounds - 97) % 26 + 97)
        await ctx.send('Your decrypted message is: {}'.format(decrypt))
    except ValueError:
        await ctx.send('Not a valid number.')


@bot.command()
async def setStatus(ctx, statusMsg):
    """Sets the status of the bot. Requires double quotes."""
    if ownerID == ctx.message.author.id:
        await client.change_presence(activity=discord.Game(name=statusMsg))
        await ctx.send("Status successfully changed!")
    else:
        await ctx.send("'Owner Only.'")

bot.run('Insert Your Bot Token Here')
