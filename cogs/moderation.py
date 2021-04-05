import discord
from discord.ext import commands
class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot     
        
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=10):
        """Purge messages, default amount is 10."""
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *reason):
        if not reason:
            await user.kick()
            await ctx.send(f"**{user}** has been kicked, reason: **none**.")
        else:
            await user.kick()
            await ctx.send(f"**{user}** has been kicked, reason: **{reason}**.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *reason):
        if not reason:
            await user.ban()
            await ctx.send(f"**{user}** has been banned, reason: **none**.")
        else:
            await user.ban()
            await ctx.send(f"**{user}** has been banned, reason: **{reason}**.")

def setup(bot):
    bot.add_cog(Moderation(bot))
