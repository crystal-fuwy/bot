import discord

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('cfur help | revision 11'))
    print('Online!')

@client.event
async def on_message(message):

    if message.content.startswith('cfur info'):
      await message.channel.send(embed = discord.Embed(title="Crystal Fur Bot", description='Crystal Fur Bot\nRevision 11\nOwner: Crystal Fur#5411'))

client.run('token')
