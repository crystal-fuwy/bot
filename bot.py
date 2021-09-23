# Import the Discord modules
import discord

# Define client
client = discord.Client()

# On connection to Discord event
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('cfur help'))
    print('Online!')

# On the message that triggers the command
@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('cfur help')
        await mssage.channel.send('`Crystal Fur#5411` has big plans for this bot!')

# Discord bot token to identify the application
client.run('discord bot token')
