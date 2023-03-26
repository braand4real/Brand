import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

client.run('MTA4ODkwMjI5MzQwOTI0NzQ1NQ.GL2ANn.G8OjAtvdWz25Z6xvZF8Kjl-dCSIaXlEcyshttI')
