from discord.ext import commands,tasks
import discord
import random
import traceback
import os
from cogs.news import weather
from cogs.news.schedule import schedule
import datetime
import pytz

bot = commands.Bot(command_prefix='b!', description='ビチクソ丸')
TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = int(os.environ['CHANNEL_ID'])
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

# 毎日するループ
@tasks.loop(seconds=60)
async def loop():
    await bot.wait_until_ready()
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

    print(now.strftime('%H:%M'))
    if now.strftime('%H:%M') == '07:00':
        api_data = weather.get_API()
        tenki,max_temp,text = weather.today(api_data)
        embed = weather.create_message(tenki,max_temp,text)
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send(embed=embed)
    elif now.strftime('%H:%M') == '08:00':
        today = int(now.strftime('%d'))
        embed = schedule.make_schedule_embed(today)
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send(embed=embed)
    elif now.strftime('%H:%M') == '22:00':
        today = int(now.strftime('%d'))+1
        embed = schedule.make_schedule_embed(today)
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send(embed=embed)
loop.start()
bot.run(TOKEN)
