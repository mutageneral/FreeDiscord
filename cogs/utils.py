import discord
from discord.ext import commands
class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot     
        
    @commands.command()
    async def ping(self, ctx):
        '''
        Get the latency of the bot.
        '''
        await ctx.send(f"{self.bot.latency}")

    @commands.command()
    async def avatar(self, ctx, *, user: discord.Member = None):
        """Get a link to somebody's avatar."""
        if user is None:
            user = ctx.author
        await ctx.send(user.avatar_url)

    @commands.command()
    async def userinfo(self, ctx, *, user: discord.Member = None):
        """Gives information about a user."""

        if user is None:
            user = ctx.author      
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=0xdfa3ff, description=user.mention)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        embed.add_field(name="Guild permissions", value=perm_string, inline=False)
        embed.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=embed)
        if isinstance(ctx.channel, discord.DMChannel):
            return

    @commands.command()
    async def joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


    @commands.command()
    async def serverinfo(self, ctx):
        """Gives some information about the server."""
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url) 
        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.blue()
            )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utils(bot))
