#################################################
# Program:  Mercury
# Version:  0.1.0
# Version Date:  02/13/2021
# Author:  Kevin Wilkins
# Date:  02/13/2021
# Contributor(s):  Kevin Wilkins
# Parameters:
# Bot will send a message to a specific channel
# when a Discord member joins the server for the
# first time.
#################################################

#################################################
# Import dependencies
#################################################
import os
import discord
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


#################################################
# Pull Discord token, guild, channel, and message
# IDs from .env file
#################################################
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
CHANNEL = int(os.getenv("CHANNEL_ID"))


#################################################
# Test and confirm bot has connected to Discord
#################################################
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            print(
                f"{client.user} has connected to Discord!\n\n"
                f"{client.user} is connected to the following guild(s):\n"
                f"{guild.name} (id: {guild.id})\n"
            )
            break


#################################################
# Send a message to new member
#################################################
# Send user a message when the join to agree to the rules
@client.event
async def on_member_join(member):
    channel = client.get_channel(CHANNEL)
    # Send message to check-point when the member joins
    await channel.send(f'Hello {member}, please proceed to #customs and agree to the rules to become a member.')
    # Output to console that member has joined the server and the welcome message has been sent
    print(f'{member} joined the server\n')
    print(f'Welcome message sent to {CHANNEL}. . .\n')
