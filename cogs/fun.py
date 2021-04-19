import discord
from discord.ext import commands
import psutil
import config
import bot

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        
def setup(bot):
    bot.add_cog(Fun(bot))