import discord
from discord.ext import commands
import psutil
import config
import bot
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        """Adds two numbers together."""
        if config.bot_lockdown_status == 'no_lockdown':
            em = discord.Embed(title = left + right)
            await ctx.send(embed = em)
        elif config.bot_lockdown_status == "lockdown_activated":
            em = discord.Embed(title = "This bot is locked down", description = "<@!" + config.ownerID + "> has locked down this bot globally.")
            await ctx.send(embed = em)

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in N-N format."""
        if config.bot_lockdown_status == 'no_lockdown':
            try:
                rolls, limit = map(int, dice.split('-'))
            except Exception:
                em = discord.Embed(title = "Format has to be in `Number-Number`")
                await ctx.send(embed = em)
                return

            result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            em = discord.Embed(title = result)
            await ctx.send(embed = em)
        elif config.bot_lockdown_status == "lockdown_activated":
            em = discord.Embed(title = "This bot is locked down", description = "<@!" + config.ownerID + "> has locked down this bot globally.")
            await ctx.send(embed = em)
    
    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        if config.bot_lockdown_status == 'no_lockdown':
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
        elif config.bot_lockdown_status == "lockdown_activated":
            em = discord.Embed(title = "This bot is locked down", description = "<@!" + config.ownerID + "> has locked down this bot globally.")
            await ctx.send(embed = em)


        
def setup(bot):
    bot.add_cog(Fun(bot))