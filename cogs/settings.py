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
                await ctx.send("Bot status successfully reset the status!")
            else:
                await self.bot.change_presence(activity=discord.Game(name=args))
                await ctx.send("Bot status successfully changed to **" + status + "**!")
        else:
            await ctx.send("This command is Bot Owner only")


def setup(bot):
    bot.add_cog(Settings(bot))

