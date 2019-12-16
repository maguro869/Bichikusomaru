import discord
from discord.ext import commands
import requests
import json
import os
import random
import aiohttp

GIF_API_KEY  = os.environ['GIF_BOT_TOKEN']
class Gif(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def gif(self,ctx,keyword):
        url = f'https://api.giphy.com/v1/gifs/random?api_key={GIF_API_KEY}&tag={keyword}&rating=g'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                if res.status == 200:
                    gif_url = await res.json()['data']['images']['original']['url']
                    embed = discord.Embed(title=keyword,color=0x0080ff)
                    embed.set_image(url=gif_url)
                    await ctx.send(embed=embed)
        
    @commands.command()
    async def yn(self,ctx):
        yn_list = ['https://gph.is/2ud7xAC','https://gph.is/g/EqNGrd7']
        await ctx.send(random.choice(yn_list))

def setup(bot):
    bot.add_cog(Gif(bot))
