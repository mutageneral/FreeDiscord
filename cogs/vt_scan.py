import discord, time
from discord.ext import commands
import config
import json, base64

class Caesarcrypt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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