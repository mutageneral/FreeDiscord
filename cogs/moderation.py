import discord, time
from discord.ext import commands
class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def timeconvertion(period):#Time convertion
        to_convert = ''.join(filter(str.isdigit, period))
        convertion = {"s":1, "m":60, "h":3600,"d":86400}
        timeconvert = int(to_convert) * convertion[period[-1]]

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

    @commands.command()#Takes 1s 1m 1h 1d
    @commands.has_permissions(mute=True)
    async def mute(self, ctx, user: discord.Member = None, _time):
        await user.add_roles(user, "mute")
        await ctx.send("User muted.")
        await asyncio.sleep(timeconvertion(_time))
        await user.remove_roles(user, "mute")

def setup(bot):
    bot.add_cog(Moderation(bot))
