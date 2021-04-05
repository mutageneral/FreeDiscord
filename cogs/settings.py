import discord
from discord.ext import commands
class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def botstatus(ctx, statusMsg):
    """Sets the status of the bot. Requires double quotes."""
    if ownerID == str(ctx.message.author.id):
        await bot.change_presence(activity=discord.Game(name=statusMsg))
        await ctx.send("Status successfully changed!")
    else:
        await ctx.send("'Owner Only.'")

def setup(bot):
    bot.add_cog(Settings(bot))