import discord
import time
from discord.ext import commands
from discord.utils import get
import asyncio


def timeconvertion(period):  # Time convertion
    if period[-1].isalpha():
        to_convert = ''.join(filter(str.isdigit, period))
        convertion = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        timeconverted = int(to_convert) * convertion[period[-1]]
        return int(timeconverted)
    else:
        return 0

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
        """Kick a member."""
        args = " ".join(reason[:])
        if not reason:
            await user.kick()
            em = discord.Embed(title = f"**{user}** has been kicked, reason: **none**.")
            await ctx.send(embed = em)
        else:
            await user.kick()
            em = discord.Embed(title = f"**{user}** has been kicked, reason: **{reason}**.")
            await ctx.send(embed = em)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *reason):
        """Ban a member."""
        args = " ".join(reason[:])
        if not reason:
            await user.ban()
            em = discord.Embed(title = f"**{user}** has been banned, reason: **none**.")
            await ctx.send(embed = em)
        else:
            await user.ban()
            em = discord.Embed(title = f"**{user}** has been banned, reason: **{reason}**.")
            await ctx.send(embed = em)

    @commands.command()  # Takes 1s 1m 1h 1d
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, user: discord.Member, mutetime):
        """Mute a member."""
        if timeconvertion(mutetime) != 0:
            role = discord.utils.get(user.guild.roles, name="muted")
            await user.add_roles(role)

            em = discord.Embed(title = "User has been muted for " + "`{}`".format(str(mutetime)) + ".")
            await ctx.send(embed = em)

            await asyncio.sleep(timeconvertion(mutetime))
            await user.remove_roles(role)
        elif timeconvertion(mutetime) == 0:
            em = discord.Embed(title = "The time format doesn't seem right.")
            await ctx.send(embed = em)
        else:
            print("Something went wrong | Mute command, moderation.py, line 57.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
        """Unban a member."""
        userToUnban = await self.bot.fetch_user(id)
        await ctx.guild.unban(userToUnban)
        em = discord.Embed(title = "Successfully unbanned `" + userToUnban.name + "`")
        await ctx.send(embed = em)

    @commands.command()  # Takes 1s 1m 1h 1d
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, user: discord.Member):
        """Unmute a member."""
        role = discord.utils.get(user.guild.roles, name="muted")
        await user.remove_roles(role)
        em = discord.Embed(title = "Successfully unmuted `" + user.name + "`")
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Moderation(bot))
