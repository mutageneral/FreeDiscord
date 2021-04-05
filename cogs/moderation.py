import discord
from discord.ext import commands
class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot     
        
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        await ctx.send('Done!', delete_after=5.0)

def setup(bot):
    bot.add_cog(Moderation(bot))
