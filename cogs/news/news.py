import discord
from discord.ext import commands,tasks
from .schedule import schedule
from . import weather


CHANNEL_ID = 573116659225591824

class News(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def w(self,ctx):
        api_data = weather.get_API()
        tenki,max_temp,text = weather.today(api_data)
        embed = weather.create_message(tenki,max_temp,text)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def test():
        date = datetime.datetime.now()+td_9h
        today = int(date.strftime('%d'))
        embed = schedule.make_schedule_embed(today)
        await ctx.send(embed=embed)

    @tasks.loop(seconds=60)
    async def loop():
        await client.wait_until_ready()
        td_9h = datetime.timedelta(hours=9)
        now = datetime.datetime.now()+td_9h
        
        if now.strftime('%H:%M') == '07:00':
            api_data = weather.get_API()
            tenki,max_temp,text = weather.today(api_data)
            embed = weather.create_message(tenki,max_temp,text)
            channel = bot.get_channel(CHANNEL_ID)
            await channel.send(embed=embed)
        elif now.strftime('%H:%M') == '08:00':
            date = datetime.datetime.now()+td_9h
            today = int(date.strftime('%d'))
            embed = schedule.make_schedule_embed(today)
            channel = bot.get_channel(CHANNEL_ID)
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(News(bot))