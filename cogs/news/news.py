import discord
from discord.ext import commands,tasks
from .schedule import schedule
from . import weather
import datetime
import os

CHANNEL_ID = int(os.environ['CHANNEL_ID'])

class News(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def w(self,ctx):
        api_data = weather.get_API()
        tenki,max_temp,text = weather.today(api_data)
        embed = weather.create_message(tenki,max_temp,text)
        await ctx.send(embed=embed)

    @commands.group(invoke_without_command=True)
    async def sche(self,ctx):
        # invoke_without_command=True -> サブコマンド有無判定
        # True -> サブコマンドない時のみ実行
        date = datetime.datetime.now()
        today = int(date.strftime('%d'))
        embed = schedule.make_schedule_embed(today)     
        await ctx.send(embed=embed) 

    @sche.command()
    async def today(self,ctx):
        date = datetime.datetime.now()
        today = int(date.strftime('%d'))
        embed = schedule.make_schedule_embed(today)     
        await ctx.send(embed=embed) 
    
    @sche.command()
    async def tomorrow(self,ctx):
        date = datetime.datetime.now()
        today = int(date.strftime('%d')) + 1
        print(today)
        embed = schedule.make_schedule_embed(today)     
        await ctx.send(embed=embed) 
    
    @tasks.loop(seconds=60)
    async def loop(self,ctx):
        await bot.wait_until_ready()
        td_9h = datetime.timedelta(hours=9)
        now = datetime.datetime.now()+td_9h
        
        if now.strftime('%H:%M') == '07:00':
            api_data = weather.get_API()
            tenki,max_temp,text = weather.today(api_data)
            embed = weather.create_message(tenki,max_temp,text)
            channel = ctx.get_channel(CHANNEL_ID)
            await channel.send(embed=embed)
        elif now.strftime('%H:%M') == '08:00':
            date = datetime.datetime.now()+td_9h
            today = int(date.strftime('%d'))
            embed = schedule.make_schedule_embed(today)
            channel = ctx.get_channel(CHANNEL_ID)
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(News(bot))


