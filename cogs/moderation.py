import discord
import time
from discord.ext import commands
from discord.utils import get


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def timeconvertion(period):  # Time convertion
        to_convert = ''.join(filter(str.isdigit, period))
        convertion = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        timeconverted = int(to_convert) * convertion[period[-1]]
        return int(timeconverted)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=10):
        """Purge messages, default amount is 10."""
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *reason):
        """Kick a member."""
        args = " ".join(reason[:])
        if not reason:
            await user.kick()
            await ctx.send(f"**{user}** has been kicked, reason: **none**.")
        else:
            await user.kick()
            await ctx.send(f"**{user}** has been kicked, reason: **{reason}**.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *reason):
        """Ban a member."""
        args = " ".join(reason[:])
        if not reason:
            await user.ban()
            await ctx.send(f"**{user}** has been banned, reason: **none**.")
        else:
            await user.ban()
            await ctx.send(f"**{user}** has been banned, reason: **{reason}**.")

    @commands.command()  # Takes 1s 1m 1h 1d
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, user: discord.Member, time):
        """Mute a member"""
        role = discord.utils.get(user.guild.roles, name="muted")
        await user.add_roles(role)
        await ctx.send("User muted for " + "```{}```.".format(str(time)))
        await asyncio.sleep(timeconvertion(time))
        await user.remove_roles(role)


def setup(bot):
    bot.add_cog(Moderation(bot))
