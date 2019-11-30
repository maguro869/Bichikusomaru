import discord
from discord.ext import commands
import requests
import json

class Gif(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def gif(self,ctx,key):
        API_KEY = 'cKEMX2RxaRH65WT2Tq7QB2a0zGBXN8R8'
        url = 'https://api.giphy.com/v1/gifs/random'
        res = requests.get(f'{url}?api_key={API_KEY}&tag={key}&rating=g')
        gif_url = res.json()['data']['images']['original']['url']
        embed = discord.Embed(title=key,color=0x0080ff)
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Gif(bot))