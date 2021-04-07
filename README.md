# FreeDiscord
## Welcome to the official GitHub page of the FreeDiscord bot!
FreeDiscord is a Discord bot made by the FreeTechnologies team ([SKBotNL](https://github.com/SKBotNL), [ItsJustLag](https://github.com/ItsJustLag), [recallwhoiam](https://github.com/recallwhoiam), and [Odysseus](https://github.com/Odysseus443)) that you can edit and self host. This bot is 100% open source, so feel free to make forks of it, if you want.
If you find an issue, or have a feature suggestion, please let us know by opening an issue [here](https://github.com/FreeTechnologies/FreeDiscord/issues). :)

## Documentation

### Starting the bot

1. Clone the repository: `git clone https://github.com/FreeTechnologies/FreeDiscord.git`. Or download the zip, upzip it, go into the folder, and go to step 3.
2. `cd` to the repository folder: `cd FreeDiscord`.
3. Make sure all the dependencies are installed, Windows: `python -m pip install discord.py requests` Linux: `pip3 install discord.py requests`.
4. Run `python3 freesetup.py` for an interative configuration creator.
5. Before starting, make sure Server Members Intent is enabled in your bot settings.
6. To make sure the `mute` and `unmute` command works, please make a role called `muted` in your server.
7. Run the bot main file: `python3 bot.py`.

### Features

There are many features of the bot. These features include:

- VirusTotal file scanning (see below)
- Message encryption
- Moderation
- Lots more
- More being added regularly :)

For the VirusTotal file scanning to work, you need to get a VirusTotal V3 API key.(Only hash working right now.)
To get this, sign in to VirusTotal and get the API key, then put it where it says:
`Your VirusTotal API Key Here` in the config file.

Like earlier said, if you have any feature requests or issues with the bot, open an issue [here](https://github.com/FreeTechnologies/FreeDiscord/issues)!
Enjoy the bot! We hope you have as much fun with it as we had programming it! :)
