import discord
from discord.ext import commands
import random
import time

description = '''List of all the commands
-----------------------------------------'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='@', description=description, intents=intents)

@bot.event
async def on_ready():
    # What gets printed in the terminal when the bot is succesfully logged in
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def setStatus(ctx, status):
    """Owner only. Sets the status of the bot. Requires double quotes."""

    userID = ctx.message.author.id
    ownerID = 461545952046743563 #Set this to the status you want

    if userID == ownerID:
        await bot.change_presence(activity=discord.Game(name=status))
        await ctx.send("Done! Successfully set the bot status.")
    else:
        await ctx.send("You don't have permission to change this")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.send('Done!', delete_after=5.0)
   
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in N-N format."""
    try:
        rolls, limit = map(int, dice.split('-'))
    except Exception:
        await ctx.send('Format has to be in N-N!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    if "@everyone" or "@here" in choices:
        await ctx.send("Haha, nice try. Isn't going to work")
    else:
        await ctx.send(random.choice(choices))

@bot.command()
async def avatar(ctx, *, user: discord.Member = None):
    """Get a link to somebody's avatar"""
    if user is None:
        user = ctx.author
    await ctx.send(user.avatar_url)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    try:
        if "@everyone" or "@here" in content:
            ctx.send("Haha, nice try. Isn't going to work.")
        else:
            if times > 10:
                await ctx.send("Please don't try to repeat too much.")
            else:
                for i in range(times):
                    await ctx.send(content)
        
    except Exception:
        await ctx.send("Please don't spam this command")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def ping(ctx):
    '''
    Get the latency of the bot.
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@bot.command()
async def userinfo(ctx, *, user: discord.Member = None):
    """Gives information about a user."""

    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)
    if isinstance(ctx.channel, discord.DMChannel):
        return

bot.run('Insert your bot token here')

