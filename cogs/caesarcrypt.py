import discord, time
from discord.ext import commands
class caesarcrypt(commands.Cog):
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
            await ctx.send('Your encrypted message is: {}'.format(encrypt))
        except ValueError:
            await ctx.send('Not a valid number.')


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
            await ctx.send('Your decrypted message is: {}'.format(decrypt))
        except ValueError:
            await ctx.send('Not a valid number.')

def setup(bot):
    bot.add_cog(caesarcrypt(bot))