import discord
from discord.ext import commands
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
        api_data = await weather.get_API()
        tenki,max_temp,text = weather.today(api_data)
        embed = weather.create_message(tenki,max_temp,text)
        await ctx.send(embed=embed)

    @commands.group(invoke_without_command=True)
    async def sche(self,ctx):
        # invoke_without_command=True -> サブコマンド有無判定
        # True -> サブコマンドない時のみ実行
        
        td_9h = datetime.timedelta(hours=9)
        now = datetime.datetime.now()+td_9h
        today = int(now.strftime('%d'))
        embed = schedule.make_schedule_embed(today)     
        await ctx.send(embed=embed) 

    @sche.command()
    async def today(self,ctx):
        td_9h = datetime.timedelta(hours=9)
        now = datetime.datetime.now()+td_9h
        today = int(now.strftime('%d'))
        embed = schedule.make_schedule_embed(today)     
        await ctx.send(embed=embed) 
    
    @sche.command()
    async def tomorrow(self,ctx):
        date = datetime.datetime.now()
        today = int(date.strftime('%d')) + 1
        embed = schedule.make_schedule_embed(today)     
        await ctx.send(embed=embed) 
    

def setup(bot):
    bot.add_cog(News(bot))
    


