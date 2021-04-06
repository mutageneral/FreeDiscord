import discord
from discord.ext import commands
# from bot import ownerID 
ownerID = "Insert-YOUR-Discord-ID-Here"

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botstatus(self, ctx, status):
        """Sets the status of the bot. Owner only."""
        if str(ctx.message.author.id) == ownerID:
            await self.bot.change_presence(activity=discord.Game(name=status))
            await ctx.send("Bot status successfully changed to " + status + "!")
        else:
            await ctx.send("listen here bud the command says 'Owner Only' for a reason")


def setup(bot):
    bot.add_cog(Settings(bot))

