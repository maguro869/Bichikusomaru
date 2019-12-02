from discord.ext import commands
import discord
import random
import traceback
import os

bot = commands.Bot(command_prefix='b!', description='ビチクソ丸')
TOKEN = os.environ['DISCORD_BOT_TOKEN']

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
    await bot.change_presence(activity=discord.Game(name="b!helpでヘルプが見れるよ"))

@bot.event
async def on_command_error(ctx,error):
    embed = discord.Embed(title="エラー情報", description="", color=0x0080ff)
    embed.add_field(name="エラー発生コマンド", value='**'+ctx.message.content+'**\n\nそんなコマンドは無いよ :sob: \n**b!help**でコマンドを確認してみよう', inline=False)
    await ctx.send(embed=embed)


bot.run(TOKEN)