from discord.ext import commands
import discord
import random
import traceback
import os

bot = commands.Bot(command_prefix='卍', description='ビチグソ丸')
#TOKEN = os.environ['DISCORD_BOT_TOKEN']
TOKEN = "NjMyMDg4NzY3NzYyNzkyNDU5.XeReJA.aj6wKE3bnhVKaF3CXl80-IN4z38"

cogs = [
    'cogs.help',
    'cogs.animals',
    'cogs.gif',
    'cogs.roll',
    'cogs.news.news'
    ]

for cog in cogs:
    try:
        bot.load_extension(cog)
    except Exception:
        traceback.print_exc()

@bot.command()
async def hello(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.event
async def on_ready():
    
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)