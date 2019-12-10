import discord
from discord.ext import commands
import requests
import json
import random
import aiohttp

class Animal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def fox(self,ctx):
        i = random.randint(1,122)
        await ctx.send("https://randomfox.ca/images/{}.jpg".format(i))

    @commands.command()
    async def cat(self,ctx):
        api = 'https://api.thecatapi.com/v1/images/search'
        async with aiohttp.ClientSession() as session:
            async with session.get(api) as res:
                if res.status == 200:
                    j = await res.json()
                    await ctx.send(j[0]['url'])
    @commands.command()
    async def dog(self,ctx):
        url = 'https://random.dog/woof.json'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                if res.status == 200:
                    j = await res.json()
                    await ctx.send(j['url'])

def setup(bot):
    bot.add_cog(Animal(bot))