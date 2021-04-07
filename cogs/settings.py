import discord
from discord.ext import commands
import os
import sys
sys.path.append(os.path.realpath('.'))
from config import *

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botstatus(self, ctx, *args):
        """Sets the status of the bot. Owner only. 'botstatus' to reset"""
        args = " ".join(args[:])
        if str(ctx.message.author.id) == ownerID:
            if args == '':
                await self.bot.change_presence(activity=discord.Game(name=''))

                em = discord.Embed(title = "Bot status successfully reset!")
                await ctx.send(embed = em)
            else:
                await self.bot.change_presence(activity=discord.Game(name=args))

                em = discord.Embed(title = "Bot status successfully changed to `" + args + "`!")
                await ctx.send(embed = em)
        else:
            em = discord.Embed(title = "This command is for the bot owner only.")
            await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(Settings(bot))


