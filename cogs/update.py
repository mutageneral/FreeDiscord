import discord
from discord.ext import commands
from git import Repo
import os
import shutil
import sys
import subprocess
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
from shutil import copyfile
from config import *

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def updatebot(self, ctx):
        """Attempts to update the bot directly from the GitHub repository."""
        if str(ctx.message.author.id) == ownerID:
            os.mkdir('/tmp/freeupdate')
            HTTPS_REMOTE_URL = github_login_url
            DEST_NAME = '/tmp/freeupdate'
            cloned_repo = Repo.clone_from(HTTPS_REMOTE_URL, DEST_NAME)
            dir_path = os.getcwd()
            shutil.rmtree(dir_path + "/cogs/")
            path = '/home/recallwhoiam'
            src = '/tmp/freeupdate/cogs'
            dest = dir_path + "/cogs"
            destination = shutil.copytree(src, dest)
            copyfile('/tmp/freeupdate/bot.py', dir_path + '/bot.py')
            copyfile('/tmp/freeupdate/freesetup.py', dir_path + '/freesetup.py')
            copyfile('/tmp/freeupdate/README.md', dir_path + '/README.md')
            print("Done!")
        else:
            em = discord.Embed(title = "This command is for the bot owner only.")
            await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Update(bot))
