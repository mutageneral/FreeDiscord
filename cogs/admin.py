import discord
from discord.ext import commands
import config
import globalconfig
import importlib

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lockdownbot(self, ctx):
        """Locks down bot globally. Bot owner only."""
        if str(ctx.message.author.id) == config.ownerID:
            if config.bot_lockdown_status == 'no_lockdown':
                em = discord.Embed(title = "Bot Lockdown Activated", description = "This bot is now locked down. Most commands will not work in any server.")
                await ctx.send(embed = em)
                await self.bot.change_presence(activity=discord.Game(name='v' + globalconfig.version + " | LOCKED DOWN"))
                with open('./config.py', 'r') as file :
                    filedata = file.read()
                filedata = filedata.replace('no_lockdown', 'lockdown_activated')
                with open('./config.py', 'w') as file:
                    file.write(filedata)
                importlib.reload(config)
            elif config.bot_lockdown_status == 'lockdown_activated':
                em = discord.Embed(title = "Bot Lockdown Deactivated", description = "This bot is now unlocked. All commands will now work in any server.")
                await ctx.send(embed = em)
                await self.bot.change_presence(activity=discord.Game(name=''))
                with open('./config.py', 'r') as file :
                    filedata = file.read()
                filedata = filedata.replace('lockdown_activated', 'no_lockdown')
                with open('./config.py', 'w') as file:
                    file.write(filedata)
                importlib.reload(config)
        else:
            em = discord.Embed(title = "This command is for the bot owner only.")
            await ctx.send(embed = em)




def setup(bot):
    bot.add_cog(Admin(bot))
