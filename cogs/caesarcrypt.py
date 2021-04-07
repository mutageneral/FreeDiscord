import discord, time
from discord.ext import commands
class Caesarcrypt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Play with caesarcrypt. @bot rounds(numbers) message")
    async def encrypt(ctx, rounds: int, * , message):
        """Encrypt a message."""
        encrypt = ""
        try:
            int(rounds)
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
        except ValueError:
            em = discord.Embed(title = "Not a valid number.")
            await ctx.send(embed = em)


    @commands.command(description="Decrypt with caesarcrypt. @bot rounds(numbers) message")
    async def decrypt(ctx, rounds: int, * , message):
        """Decrypt a message."""
        decrypt = ""
        try:
            int(rounds)
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
        except ValueError:
            em = discord.Embed(title = "Not a valid number.")
            await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Caesarcrypt(bot))
