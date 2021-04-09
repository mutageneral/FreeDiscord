import discord
from discord.ext import commands
import random
import requests
import time
import json
import config
import base64
import psutil

description = '''List of all the commands
-----------------------------------------
This bot is based off of/is the FreeDiscord bot made by SKbotNL, ItsJustLag,
Recall/Recallwhoiam, Quirinus, and antistalker.
Project URL: https://github.com/FreeTechnologies/FreeDiscord/
Support Server: https://discord.gg/VyNxSt55gj
-----------------------------------------'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=config.prefix, description=description, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    # What gets printed in the terminal when the bot is succesfully logged in
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.load_extension("cogs.general")
bot.load_extension("cogs.utils")
bot.load_extension("cogs.moderation")
bot.load_extension("cogs.settings")
bot.load_extension("cogs.caesarcrypt")
bot.load_extension("cogs.help")
bot.load_extension("cogs.update")
bot.load_extension("cogs.admin")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        em = discord.Embed(title = "You do not have permission to do that.")
        await ctx.send(embed = em)
    elif isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title = "Your command is missing an argument.")
        await ctx.send(embed = em)
    elif isinstance(error, commands.CommandNotFound):
        em = discord.Embed(title = "Command not found")
        await ctx.send(embed = em)
    else:
        em = discord.Embed(title = "An internal error occurred.", description = "Here are the details of the error: " + str(error))
        await ctx.send(embed = em)

@bot.command(description='Shows information about bot instance.')
async def about(ctx):
    em = discord.Embed(title = "About FreeDiscord", description = "This bot is based off of/is the FreeDiscord bot made by SKBotNL, ItsJustLag, recallwhoiam, Quirinus, and antistalker#8888.")
    em.add_field(name = "Project URL", value = "https://github.com/FreeTechnologies/FreeDiscord/")
    em.add_field(name = "Support server", value = "https://discord.gg/VyNxSt55gj")
    em.add_field(name = "Bot invite link", value = "https://discord.com/oauth2/authorize?client_id=829158610965495848&permissions=8&scope=bot")
    servers = list(bot.guilds)
    serverNumber = len(servers)
    em.add_field(name = "Number of servers this instance is in", value = serverNumber)
    cpuUsage = psutil.cpu_percent()
    em.add_field(name = "CPU usage of host", value = cpuUsage)
    em.add_field(name = "Ping in milliseconds", value = bot.latency*1000)
    await ctx.send(embed = em)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    if config.bot_lockdown_status == 'no_lockdown':
        em = discord.Embed(title = left + right)
        await ctx.send(embed = em)
    elif config.bot_lockdown_status == "lockdown_activated":
        em = discord.Embed(title = "This bot is locked down", description = "<@!" + config.ownerID + "> has locked down this bot globally.")
        await ctx.send(embed = em)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in N-N format."""
    if config.bot_lockdown_status == 'no_lockdown':
        try:
            rolls, limit = map(int, dice.split('-'))
        except Exception:
            em = discord.Embed(title = "Format has to be in `Number-Number`")
            await ctx.send(embed = em)
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        em = discord.Embed(title = result)
        await ctx.send(embed = em)
    elif config.bot_lockdown_status == "lockdown_activated":
        em = discord.Embed(title = "This bot is locked down", description = "<@!" + config.ownerID + "> has locked down this bot globally.")
        await ctx.send(embed = em)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    if config.bot_lockdown_status == 'no_lockdown':
        if "@everyone" in choices:
            em = discord.Embed(title = "Nice try, sadly that won't work here.")
            await ctx.send(embed = em)
        else:
            if "@here" in choices:
                em = discord.Embed(title = "Nice try, sadly that won't work here.")
                await ctx.send(embed = em)
            else:
                em = discord.Embed(title = random.choice(choices))
                await ctx.send(embed = em)
    elif config.bot_lockdown_status == "lockdown_activated":
        em = discord.Embed(title = "This bot is locked down", description = "<@!" + config.ownerID + "> has locked down this bot globally.")
        await ctx.send(embed = em)

apikey = config.virustotal_api

def vt_json_parsing(detections):
    detections = json.dumps(detections)
    detections = json.dumps(json.loads(detections), indent=2)
    detections = str(detections).split("last_analysis_stats")
    detections = detections[1]
    detections = detections.split("        ")
    for m in detections:
        if 'malicious' in str(m) and any(d.isdigit() for d in m):
            detections = m
            break
    detections = "".join(filter(str.isdigit, m))
    return str(detections)

@bot.command(description='Testing, "@bot hash"')
async def vt_hash(ctx, hash: str):
    """VirusTotal Integration"""
    if config.bot_lockdown_status == 'no_lockdown':
        header = {'x-apikey': '{}'.format(apikey)}
        vturl = "https://www.virustotal.com/api/v3/files/{}".format(hash)
        response = requests.get(vturl, headers = header).json()
        em = discord.Embed(title = "Detections: {}".format(vt_json_parsing(response)))
        await ctx.send(embed = em)
    elif config.bot_lockdown_status == "lockdown_activated":
        em = discord.Embed(title = "This bot is locked down", description = "<@!" + config.ownerID + "> has locked down this bot globally.")
        await ctx.send(embed = em)

@bot.command(description='Testing, "@bot hash"')
async def scan_url(ctx, url: str):
    #Need to import base64 module to work
    if config.bot_lockdown_status == 'no_lockdown':
        header = {'x-apikey': '{}'.format(apikey)}
        encode = base64.b64encode(url.encode("utf-8"))
        url_in_base64 = str(encode, "utf-8").replace("=", "")
        vturl = "https://www.virustotal.com/api/v3/urls/{}".format(url_in_base64)
        response = requests.get(vturl, headers = header).json()
        em = discord.Embed(title = "Detections: {}".format(vt_json_parsing(response)))
        await ctx.send(embed = em)
    elif config.bot_lockdown_status == "lockdown_activated":
        em = discord.Embed(title = "This bot is locked down", description = "<@!" + config.ownerID + "> has locked down this bot globally.")
        await ctx.send(embed = em)

bot.run(config.bot_token)
