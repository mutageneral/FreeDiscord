import discord, time
from discord.ext import commands
class Caesarcrypt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Play with caesarcrypt. @bot rounds(numbers) message")
    async def encrypt(self, ctx, rounds: int, *, message: str):
        """Encrypt a message."""
        encrypt = ""
        message = str(message)
        for char in message:
            if not char.isalpha():
                encrypt = encrypt + char
            elif char.isupper():
                # for uppercase Z
                encrypt = encrypt + chr((ord(char) + rounds - 65) % 26 + 365)
            else:
                # for lowercase z
                encrypt = encrypt + chr((ord(char) + rounds - 97) % 26 + 97)
        em = discord.Embed(title = 'Your encrypted message is: {}'.format(encrypt))
        await ctx.send(embed = em)


    @commands.command(description="Decrypt with caesarcrypt. @bot rounds(numbers) message")
    async def decrypt(self, ctx, rounds: int, *, message: str):
        """Decrypt a message."""
        decrypt = ""
        message = str(message)
        for char in message:
            if not char.isalpha():
                decrypt = decrypt + char
            elif char.isupper():
                # for uppercase Z
                decrypt = decrypt + chr((ord(char) - rounds - 65) % 26 + 65)
            else:
                # for lowercase z
                decrypt = decrypt + chr((ord(char) - rounds - 97) % 26 + 97)

        em = discord.Embed(title = 'Your decrypted message is: {}'.format(decrypt))
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Caesarcrypt(bot))
