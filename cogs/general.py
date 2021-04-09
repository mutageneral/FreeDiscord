import discord
from discord.ext import commands
import psutil
import config
import bot
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(invoke_without_command=True)
    # async def help(self, ctx):
        # em = discord.Embed(title = "Help", description = "Use [prefix]help <command> for extended information on a command.")
        # em.add_field(name = "General", value = "help")
        # em.add_field(name = "Moderation", value = "purge")
        # em.add_field(name = "Utils", value = "avatar, joined, ping, userinfo")

        # await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(General(bot))
