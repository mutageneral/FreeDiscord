import discord, time
from discord.ext import commands
import config
import json, base64, requests, asyncio

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
        else:
            return -1
    detections = "".join(filter(str.isdigit, m))
    return int(detections)

class VT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vt_hash(self, ctx, hash: str):
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

    @commands.command()
    async def scan_url(self, ctx, url: str):
        #Need to import base64 module to work
        if config.bot_lockdown_status == 'no_lockdown':
            header = {'x-apikey': '{}'.format(apikey)}
            data = {'url': url}
            vturl = "https://www.virustotal.com/api/v3/urls"
            requests.post(vturl, data = data, headers = header)
            em = discord.Embed(title = "Please wait for 30 seconds.")
            await ctx.send(embed = em)
            await asyncio.sleep(30)
            encode = base64.b64encode(url.encode("utf-8"))
            url_in_base64 = str(encode, "utf-8").replace("=", "")
            vturl = "https://www.virustotal.com/api/v3/urls/{}".format(url_in_base64)
            response = requests.get(vturl, headers = header).json()
            parsed = vt_json_parsing(response)
            if parsed == -1:
                em = discord.Embed(title = "Something went wrong.")
                await ctx.send(embed = em)
            else:
                em = discord.Embed(title = "Detections: {}".format(parsed))
                await ctx.send(embed = em)
        elif config.bot_lockdown_status == "lockdown_activated":
            em = discord.Embed(title = "This bot is locked down", description = "<@!" + config.ownerID + "> has locked down this bot globally.")
            await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(VT(bot))