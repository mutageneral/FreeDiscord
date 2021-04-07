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
            em = discord.Embed(title = "Help", description = "Use " + prefix + "help <command> for extended information on a command.")
            em.add_field(name = "General", value = "add, choose, roll, vt")
            em.add_field(name = "Moderation", value = "ban, delwarn, kick, mute, purge, unban, unmute, warn, warns")
            em.add_field(name = "Settings", value = "botstatus")
            em.add_field(name = "Utils", value = "avatar, joined, ping, userinfo")
            em.add_field(name = "Caesarcrypt", value = "decrypt, encrypt")
            em.add_field(name = "Help", value = "help - Shows this message")
            em.add_field(name = "botstatuschange", value = "botstatusrepeat")

            await ctx.send(embed = em)

    # Moderation commands
    @help.command(name="ban")
    async def _ban(self, ctx):
        em = discord.Embed(title = "Moderation: Ban", description = prefix + "ban <user> optional:<reason> \n\nBan a member.")
        await ctx.send(embed = em)

    @help.command(name="delwarn")
    async def _delwarn(self, ctx):
        em = discord.Embed(title = "Moderation: Delwarn", description = prefix + "delwarn <user> <reason of warn you want to delete> \n\nDelete a warning.")
        await ctx.send(embed = em)
    
    @help.command(name="kick")
    async def _kick(self, ctx):
        em = discord.Embed(title = "Moderation: Kick", description = prefix + "kick <user> optional:<reason> \n\nKick a member.")
        await ctx.send(embed = em)

    @help.command(name="mute")
    async def _mute(self, ctx):
        em = discord.Embed(title = "Moderation: Mute", description = prefix + "mtue <user> <mutetime> \n\nMute a member.")
        await ctx.send(embed = em)

    @help.command(name="purge")
    async def _purge(self, ctx):
        em = discord.Embed(title = "Moderation: Purge", description = prefix + "purge <number of messages to purge> \n\nPurge messages, default amount is 10.")
        await ctx.send(embed = em)
    
    @help.command(name="unban")
    async def _unban(self, ctx):
        em = discord.Embed(title = "Moderation: Unban", description = prefix + "unban <userid> \n\nUnban a member.")
        await ctx.send(embed = em)
    
    @help.command(name="unmute")
    async def _unmute(self, ctx):
        em = discord.Embed(title = "Moderation: Unmute", description = prefix + "unmute <user> \n\nUnmute a member.")
        await ctx.send(embed = em)

    @help.command(name="warn")
    async def _warn(self, ctx):
        em = discord.Embed(title = "Moderation: Warn", description = prefix + "warn <user> <reason> \n\nWarn a member.")
        await ctx.send(embed = em)

    @help.command(name="warns")
    async def _warns(self, ctx):
        em = discord.Embed(title = "Moderation: Warns", description = prefix + "warns <user> \n\nSee the warnings for a member.")
        await ctx.send(embed = em)

    # General commands
    @help.command(name="add")
    async def _add(self, ctx):
        em = discord.Embed(title = "General: Add", description = prefix + "add <number1> <number2> \n\nAdds two numbers together.")
        await ctx.send(embed = em)

    @help.command(name="choose")
    async def _choose(self, ctx):
        em = discord.Embed(title = "General: Choose", description = prefix + "choose <choice1> <choice2> \n\nChooses between multiple choices.")
        await ctx.send(embed = em)

    @help.command(name="roll")
    async def _roll(self, ctx):
        em = discord.Embed(title = "General: Roll", description = prefix + "roll <number1>-<number2> \n\nRolls a dice in N-N format.")
        await ctx.send(embed = em)

    @help.command(name="vt")
    async def _vt(self, ctx):
        em = discord.Embed(title = "General: VT", description = prefix + "vt <hash> \n\nScan a hash with VirusTotal")
        await ctx.send(embed = em)

    @help.command(name="scan_url")
    async def _vt(self, ctx):
        em = discord.Embed(title = "General: VT", description = prefix + "scan_url <url> \n\nScan a url with VirusTotal. **Make sure to do `https://<website>` and not `<website>`**")
        await ctx.send(embed = em)

    # Settings commands
    @help.command(name="botstatus")
    async def _botstatus(self, ctx):
        em = discord.Embed(title = "Settings: BotStatus", description = prefix + "botstatus <status> \n\nSets the status of the bot. Owner only. '" + prefix + "botstatus' to reset")
        await ctx.send(embed = em)
    
    @help.command(name="botstatusrepeat")
    async def _botstatusrepeat(self, ctx):
        em = discord.Embed(title = "Settings: BotStatusRepeat", description = prefix + "botstatusrepeat \n\nRepeatedly sets the status of the bot. Owner only.")
        await ctx.send(embed = em) 

    # Utils commands
    @help.command(name="avatar")
    async def _avatar(self, ctx):
        em = discord.Embed(title = "Utils: Avatar", description = prefix + "avatar <user> \n\nGet a link to somebody's avatar.")
        await ctx.send(embed = em)

    @help.command(name="joined")
    async def _joined(self, ctx):
        em = discord.Embed(title = "Utils: Joined", description = prefix + "joined <user> \n\nTells you when a user joined the server.")
        await ctx.send(embed = em)

    @help.command(name="ping")
    async def _ping(self, ctx):
        em = discord.Embed(title = "Utils: Ping", description = prefix + "ping \n\nTells you the latency between the bot and the server.")
        await ctx.send(embed = em)

    @help.command(name="userinfo")
    async def _userinfo(self, ctx):
        em = discord.Embed(title = "Utils: UserInfo", description = prefix + "userinfo <user> \n\nGives you information about a user.")
        await ctx.send(embed = em)
    
    # Caesar commands
    @help.command(name="encrypt")
    async def _encrypt(self, ctx):
        em = discord.Embed(title = "Caesarcrypt: Encrypt", description = prefix + "encrypt <rounds> <message> \n\nEncrypt a message. The '<message>' has to be in double quotes for it to work.")
        await ctx.send(embed = em)

    @help.command(name="decrypt")
    async def _decrypt(self, ctx):
        em = discord.Embed(title = "Caesarcrypt: Decrypt", description = prefix + "decrypt <rounds> <message> \n\nDecrypt a message. The '<message>' has to be in double quotes for it to work.")
        await ctx.send(embed = em)
    
def setup(bot):
    bot.add_cog(Help(bot))
