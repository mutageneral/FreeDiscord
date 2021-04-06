import discord
from discord.ext import commands
import os
import sys
sys.path.append(os.path.realpath('.'))
from config import *
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            em = discord.Embed(title = "Help", description = "Use [prefix]help <command> for extended information on a command.")
            em.add_field(name = "General", value = "add, choose, roll, vt")
            em.add_field(name = "Moderation", value = "ban, kick, mute, purge, unban, unmute")
            em.add_field(name = "Settings", value = "botstatus")
            em.add_field(name = "Utils", value = "avatar, joined, ping, userinfo")
            em.add_field(name = "Caesarcrypt", value = "decrypt, encrypt")
            em.add_field(name = "Help", value = "help - Shows this message")

            await ctx.send(embed = em)

    # Moderation commands
    @help.command(name="ban")
    async def _ban(self, ctx):
        em = discord.Embed(title = "Moderation: Ban", description = prefix + "ban <user> optional:<reason> \n\n Ban a member.")
        await ctx.send(embed = em)
    
    @help.command(name="kick")
    async def _kick(self, ctx):
        em = discord.Embed(title = "Moderation: Kick", description = prefix + "kick <user> optional:<reason> \n\n Kick a member.")
        await ctx.send(embed = em)

    @help.command(name="mute")
    async def _mute(self, ctx):
        em = discord.Embed(title = "Moderation: Mute", description = prefix + "mtue <user> <mutetime> \n\n Mute a member.")
        await ctx.send(embed = em)

    @help.command(name="purge")
    async def _purge(self, ctx):
        em = discord.Embed(title = "Moderation: Purge", description = prefix + "purge <number of messages to purge> \n\n Purge messages, default amount is 10.")
        await ctx.send(embed = em)
    
    @help.command(name="unban")
    async def _unban(self, ctx):
        em = discord.Embed(title = "Moderation: Unban", description = prefix + "unban <userid> \n\n Unban a member.")
        await ctx.send(embed = em)
    
    @help.command(name="unmute")
    async def _unmute(self, ctx):
        em = discord.Embed(title = "Moderation: Unmute", description = prefix + "unmute <user> \n\n Unmute a member.")
        await ctx.send(embed = em)

    # General commands
    @help.command(name="add")
    async def _add(self, ctx):
        em = discord.Embed(title = "General: Add", description = prefix + "add <number1> <number2> \n\n Adds two numbers together.")
        await ctx.send(embed = em)

    @help.command(name="choose")
    async def _choose(self, ctx):
        em = discord.Embed(title = "General: Choose", description = prefix + "choose <choice1> <choice2> \n\n Chooses between multiple choices.")
        await ctx.send(embed = em)

    @help.command(name="roll")
    async def _roll(self, ctx):
        em = discord.Embed(title = "General: Roll", description = prefix + "roll <number1>-<number2> \n\n Rolls a dice in N-N format.")
        await ctx.send(embed = em)

    @help.command(name="vt")
    async def _vt(self, ctx):
        em = discord.Embed(title = "General: VT", description = prefix + "vt <hash> \n\n VirusTotal Integration")
        await ctx.send(embed = em)

    # Settings commands
    @help.command(name="botstatus")
    async def _botstatus(self, ctx):
        em = discord.Embed(title = "Settings: BotStatus", description = prefix + "botstatus <status> \n\n Sets the status of the bot. Owner only. '" + prefix + "botstatus' to reset")
        await ctx.send(embed = em)

    # Utils commands
    @help.command(name="avatar")
    async def _avatar(self, ctx):
        em = discord.Embed(title = "Utils: Avatar", description = prefix + "avatar <user> \n\n Get a link to somebody's avatar.")
        await ctx.send(embed = em)
    
    @help.command(name="encrypt")
    async def _encrypt(self, ctx):
        em = discord.Embed(title = "Caesarcrypt: Encrypt", description = prefix + "encrypt <rounds> <message> \n\n Encrypt a message. The '<message>' has to be in double quotes for it to work.")
        await ctx.send(embed = em)

    @help.command(name="decrypt")
    async def _decrypt(self, ctx):
        em = discord.Embed(title = "Caesarcrypt: Decrypt", description = prefix + "decrypt <rounds> <message> \n\n Decrypt a message. The '<message>' has to be in double quotes for it to work.")
        await ctx.send(embed = em)

    @help.command(name="joined")
    async def _joined(self, ctx):
        em = discord.Embed(title = "Utils: Joined", description = prefix + "joined <user> \n\n Tells you when a user joined the server.")
        await ctx.send(embed = em)

    @help.command(name="ping")
    async def _ping(self, ctx):
        em = discord.Embed(title = "Utils: Ping", description = prefix + "ping \n\n Tells you the latency between the bot and the server.")
        await ctx.send(embed = em)

    @help.command(name="userinfo")
    async def _userinfo(self, ctx):
        em = discord.Embed(title = "Utils: UserInfo", description = prefix + "userinfo <user> \n\n Gives you information about a user.")
        await ctx.send(embed = em)
    
def setup(bot):
    bot.add_cog(Help(bot))
