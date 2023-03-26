import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

client.run('MTA4ODkwMjI5MzQwOTI0NzQ1NQ.G33k0x.1HVV2Ecz8DdHR7ULo5WPUALDxNHno_0BepYP5M')
