import discord
from discord.ext import commands
import random
import time

description = '''List of all the commands
-----------------------------------------'''

intents = discord.Intents.default()
intents.members = True
ownerID = "Put your ID here"

bot = commands.Bot(command_prefix='@', description=description, intents=intents)
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
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You dont have permission to do that")
    if isinstance(error,commands.MissingRequiredArgument):
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

bot.run('Insert your bot token here')

