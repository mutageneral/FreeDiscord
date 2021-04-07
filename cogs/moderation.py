import discord
import time
import os
from discord.ext import commands
from discord.utils import get
import asyncio


def timeconvertion(time):# Time convertion
    convertion = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    letters_inside = ''.join(filter(str.isalpha, time))
    lettercount = len(letters_inside)
    to_convert = ''.join(filter(str.isdigit, time))
    if time[-1].isalpha() is True and time[0].isdigit() and lettercount == 1 and letters_inside in convertion and time.isalnum() == True:
        timeconverted = int(to_convert) * convertion[time[-1]]
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

    @commands.command() # Takes 1s 1m 1h 1d
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, user: discord.Member, mutetime):
        #BTW need to import time&asyncio module to work.
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

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, user : discord.Member, reason):
        if not os.path.exists('warns'):
            os.makedirs('warns')
        try:
            if os.stat("warns/" + str(user.id) + "_" + str(ctx.message.guild.id) + ".py").st_size > 0:
                await ctx.send("Successfully warned that member")
                writeReasonTemplate = str(reason)
                warns = open("warns/" + str(user.id) + "_" + str(ctx.message.guild.id) + ".py", 'a')
                warns.write("\n")
                warns.write(writeReasonTemplate)
                warns.close()

            elif os.stat("warns/" + str(user.id) + "_" + str(ctx.message.guild.id) + ".py").st_size == 0:
                await ctx.send("Successfully warned that member")
                writeReasonTemplate = str(reason)
                warns = open("warns/" + str(user.id) + "_" + str(ctx.message.guild.id) + ".py", 'a')
                warns.write(writeReasonTemplate)
                warns.close()
        except:
            await ctx.send("Successfully warned that member")
            writeReasonTemplate = str(reason)
            warns = open("warns/" + str(user.id) + "_" + str(ctx.message.guild.id) + ".py", 'a')
            warns.write(writeReasonTemplate)
            warns.close()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warns(self, ctx, user : discord.Member):
        if not os.path.exists('warns'):
            os.makedirs('warns')
        try:
            with open("warns/" + str(user.id) + "_" + str(ctx.message.guild.id) + ".py") as f:
                lines = f.readlines()
                lines_clean = " ".join(lines[:])
                if not lines_clean:
                    em = discord.Embed(title = "Warns for " + str(user), description = "This user has no warnings")
                else:
                    em = discord.Embed(title = "Warns for " + str(user), description = lines_clean)
                await ctx.send(embed = em)
        except:
            em = discord.Embed(title = "Warns for " + str(user), description = "This user has no warnings")
            await ctx.send(embed = em)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def delwarn(self, ctx, user : discord.Member, reason):
        if not os.path.exists('warns'):
            os.makedirs('warns')
        fn = "warns/" + str(user.id) + "_" + str(ctx.message.guild.id) + ".py"
        f = open(fn)
        output = []
        word=reason
        for line in f:
            if not line.startswith(word):
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()
        await ctx.send("Successfully removed that warning")

def setup(bot):
    bot.add_cog(Moderation(bot))
