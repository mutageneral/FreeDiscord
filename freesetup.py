import os
print("Welcome to the FreeDiscord interactive setup script!")
def tokenWrite() :
    writeBotToken = input("Enter your bot token: ")
    verificationOne = input("Is this correct? (y/n): '" + writeBotToken + "'")
    if verificationOne == "y":
        print("Writing...")
        writeTokenTemplate = "bot_token = '" + writeBotToken + "'\n"
        config = open('config.py', 'a')
        config.write(writeTokenTemplate)
        config.close()
        print("Written!")
        print()
    elif verificationOne == "n":
        print("Please rerun the file and input the correct bot token.")
        exit()
    elif verificationOne != "n" or "y":
        print("Invalid response, please rerun the script.")
        exit()

def prefixWrite() :
    writePrefix = input("Enter the bot's prefix: ")
    verificationTwo = input("Is this correct? (y/n): '" + writePrefix + "'")
    if verificationTwo == "y":
        print("Writing...")
        config = open('config.py', 'a')
        writePrefixTemplate = "prefix = '" + writePrefix + "'\n"
        config.write(writePrefixTemplate)
        config.close()
        print("Written!\n")
        #print(writeTokenTemplate)
    elif verificationTwo == "n":
        print("Please rerun the file and input your preferred bot prefix.")
        exit()
    elif verificationTwo != "n" or "y":
        print("Invalid response, please rerun the script.")
        exit()

def ownerIDWrite() :
    ownerIDinput = input("Enter the bot owner's user ID: ")
    verificationThree = input("Is this correct? (y/n): '" + ownerIDinput + "'")
    if verificationThree == "y":
        print("Writing...")
        config = open('config.py', 'a')
        writePrefixTemplate = "ownerID = '" + ownerIDinput + "'\n"
        config.write(writePrefixTemplate)
        config.close()
        config = open('config.py', 'r')
    elif verificationThree == "n":
        print("Please rerun the file and input the bot owner's user ID")
        exit()
    elif verificationThree != "n" or "y":
        print("Invalid response, please rerun the script.")
        exit()

def githubLoginWrite() :
    print("Since FreeDiscord is still a private repository, please enter your GitHub login in this format: 'https://username:auth_key_if_2fa@github.com/FreeTechnologies/FreeDiscord'\n If you don't know how to get this, search up 'clone github repository with auth key'.\n")
    githubLoginInput = input("Enter your GitHub login credentials: ")
    verificationFive = input("Is this correct? (y/n): '" + githubLoginInput + "'")
    if verificationFive == "y":
        print("Writing...")
        config = open('config.py', 'a')
        writePrefixTemplate = "github_login_url = '" + githubLoginInput + "'\n"
        config.write(writePrefixTemplate)
        config.close()
        print("Written!")
        print()
    elif verificationFive == "n":
        print("Please rerun the file and input your GitHub login credentials.")
        exit()
    elif verificationFive != "n" or "y":
        print("Invalid response, please rerun the script.")
        exit()

def vtapiWrite() :
    print("If you don't have a VirusTotal API key, or don't want this feature, just hit enter on this prompt and type 's' when it asks if what you inputted is correct.\n")
    vtapiToken = input("Enter your VirusTotal API key: ")
    verificationFour = input("Is this correct? (y/n/s): '" + vtapiToken + "'")
    if verificationFour == "y":
        print("Writing...")
        config = open('config.py', 'a')
        writePrefixTemplate = "virustotal_api = '" + vtapiToken + "'\n"
        config.write(writePrefixTemplate)
        config.close()
        print("Written!")
        print()
    elif verificationFour == "n":
        print("Please rerun the file and input your VirusTotal API key.")
        exit()
    elif verificationFour == "s":
        print("Writing...")
        config = open('config.py', 'a')
        writePrefixTemplate = "virustotal_api = '' "
        config.write(writePrefixTemplate)
        config.close()
        print("Written!")
        print()
        print("You have chosen not to input a VirusTotal API key. You may add one by editing the config.py file later.")
    elif verificationFour != "n" or "y" or "s":
        print("Invalid response, please rerun the script.")
        exit()

def badwordWrite() :
    print("Please put in bad words that you want to be filtered by the bot.\n If you don't want this feature just hit enter on this prompt and type 's' when it asks if what you inputted is correct.\n The format is ")
    print('["badword1", "badword2", "badword3"]')
    badwords = input("Enter the bad words (make sure to use the format): ")
    verificationFour = input("Is this correct? (y/n/s): '" + badwords + "'")
    if verificationFour == "y":
        print("Writing...")
        config = open('config.py', 'a')
        writePrefixTemplate = "bad_words = " + badwords + "\n"
        config.write(writePrefixTemplate)
        config.close()
        print("Written!")
        print()
    elif verificationFour == "n":
        print("Please rerun the file and input the bad words you want to be filtered.")
        exit()
    elif verificationFour == "s":
        print("Writing...")
        config = open('config.py', 'a')
        writePrefixTemplate = "bad_words = []\n"
        config.write(writePrefixTemplate)
        config.close()
        print("Written!")
        print()
        print("You have chosen not to input bad words. You may add them by editing the config.py file later.")
    elif verificationFour != "n" or "y" or "s":
        print("Invalid response, please rerun the script.")
        exit()

if os.path.exists("config.py"):
    prompt = input("Existing config.py found. Should I delete it? (y/n)")
    if prompt == "y":
        print("Deleting existing config file...")
        os.remove("config.py")
        print("Deleted! Continuing with normal script now...")
        print()
    elif prompt == "n":
        print("Exiting...")
        exit()
    elif prompt != "n" or "y":
        print("Invalid response, please rerun the script.")
        exit()

githubLoginWrite()
tokenWrite()
prefixWrite()
ownerIDWrite()
vtapiWrite()
badwordWrite()
config = open('config.py', 'a')
config.write("bot_lockdown_status = 'no_lockdown'")
config.close()
print("Your config file should be written now!")
print("To start your bot, run python3 bot.py")
print("Have a nice day! :)")
exit()