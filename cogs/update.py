import discord
from discord.ext import commands
from git import Repo
import os
import shutil
import sys
import subprocess
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
from shutil import copyfile
import config
#import globalconfig

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def updatebot(self, ctx):
        """Attempts to update the bot directly from the GitHub repository."""
        if str(ctx.message.author.id) == config.ownerID:
            # username = os.getlogin()
            os.mkdir('/tmp/freeupdate')
            HTTPS_REMOTE_URL = config.github_login_url
            DEST_NAME = '/tmp/freeupdate'
            cloned_repo = Repo.clone_from(HTTPS_REMOTE_URL, DEST_NAME)
            dir_path = os.getcwd()
            shutil.rmtree(dir_path + "/cogs/")
            path = dir_path
            src = '/tmp/freeupdate/cogs'
            dest = dir_path + "/cogs"
            destination = shutil.copytree(src, dest)
            copyfile('/tmp/freeupdate/bot.py', dir_path + '/bot.py')
            copyfile('/tmp/freeupdate/freesetup.py', dir_path + '/freesetup.py')
            copyfile('/tmp/freeupdate/README.md', dir_path + '/README.md')
            copyfile('/tmp/freeupdate/globalconfig.py', dir_path + '/globalconfig.py')
            shutil.rmtree('/tmp/freeupdate')
            print("Done! Restart the bot to apply the changes!")
            em = discord.Embed(title = "Updated!", description = "FreeDiscord updated! No error reported. Check your console to confirm this.")
            em.add_field(name = "Note", value = "The bot will now restart.")

            await ctx.send(embed = em)

            await ctx.bot.logout()
            await login(config.bot_token, bot=True)

        else:
            em = discord.Embed(title = "This command is for the bot owner only.")
            await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Update(bot))
