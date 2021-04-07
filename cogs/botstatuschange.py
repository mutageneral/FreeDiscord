import discord
from discord.ext import commands
import os
import sys
import time
import asyncio
sys.path.append(os.path.realpath('.'))
from config import *

class Settings(commands.Cog):
        
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botstatusrepeat(self, ctx):
        if str(ctx.message.author.id) == ownerID:
            
            em = discord.Embed(title = "Status loop initiated.")
            await ctx.send(embed = em)

            while True:
                await self.bot.change_presence(activity=discord.Game("Activate Windows"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("Fixing Bugs"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("Made by the FreeTechnologies team"))
                await asyncio.sleep(5) 
                await self.bot.change_presence(activity=discord.Game("What am I doing with my life?"))
                await asyncio.sleep(5) 
                await self.bot.change_presence(activity=discord.Game("never gonna give you up, never gonna let you down"))
                await asyncio.sleep(5) 
                await self.bot.change_presence(activity=discord.Game("THE MINIMODS ARE COMING!!!"))            
                await asyncio.sleep(5) 
                await self.bot.change_presence(activity=discord.Game("no one cares bro"))
                await asyncio.sleep(5) 
                await self.bot.change_presence(activity=discord.Game("hey there buddy chum pal friend buddy pal chum bud friend fella brother amigo pal"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("made by two weebs and one 3 year old"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("ya like jazz?"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("we got a, number 1 victory royal, yeah fortnite we 'bout to get down"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("userDespacito"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("this python script is waaaaay too long. meh, who cares"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("SUS MONGUS"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("hey guys just wanna remind you this is a christian minecraft server"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("IT'S TIME TO STOP, OKAY?"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("stop it. get some help."))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("somebody once told me the world was macaroni"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("cringe"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("Among Us"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("fartnut"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("creeper? aw man"))
                await asyncio.sleep(5)
                await self.bot.change_presence(activity=discord.Game("FreeDiscord is the best open source discord bot"))
        else:
            em = discord.Embed(title = "This command is for the bot owner only.")
            await ctx.send(embed = em)           

def setup(bot):
    bot.add_cog(Settings(bot))
