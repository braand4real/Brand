import discord
from discord.ext import commands

client = commands.Bot(command_prefix='@')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.event
async def on_message(message):
    if message.content == 'How are you?':
        await message.channel.send('I am doing great, fuck you')

client.run('TOKEN')
