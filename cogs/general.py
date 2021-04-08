import discord
from discord.ext import commands
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot   
    
    @commands.command()
    async def about(self, ctx):
        em = discord.Embed(title = "About FreeDiscord", description = "This bot is based off of/is the FreeDiscord bot made by SKBotNL, ItsJustLag, recallwhoiam, Quirinus, and antistalker.")
        em.add_field(name = "Project URL", value = "https://github.com/FreeTechnologies/FreeDiscord/")
        em.add_field(name = "Support Server", value = "https://discord.gg/VyNxSt55gj")

        await ctx.send(embed = em)
        
    # @commands.command(invoke_without_command=True)
    # async def help(self, ctx):
        # em = discord.Embed(title = "Help", description = "Use [prefix]help <command> for extended information on a command.")
        # em.add_field(name = "General", value = "help")
        # em.add_field(name = "Moderation", value = "purge")
        # em.add_field(name = "Utils", value = "avatar, joined, ping, userinfo")

        # await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(General(bot))
