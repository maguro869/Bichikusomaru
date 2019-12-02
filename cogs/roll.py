import discord
from discord.ext import commands
import random

class Roll(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        

    @commands.group(invoke_without_command=True)
    async def roll(self,ctx):
        embed = discord.Embed(color=0x0080ff)
        embed.add_field(name='roll num a b n',value='a~bの範囲の値をn個表示します',inline=False)
        embed.add_field(name='roll key a 候補1 候補2 … 候補n', value='n個の候補の中からa個選びます',inline=False)
        await ctx.send(embed=embed)

    @roll.command()
    async def num(self,ctx,a,b,n):
        a = int(a)
        b = int(b)
        n = int(n)
        embed = discord.Embed(color=0x0080ff)
        
        if a>b:
            a,b = b,a
        if b - a < n:
            embed.add_field(name='ERROR',value='個数が多すぎます')
        else:
            li = [i for i in range(a,b+1)]
            res = random.sample(li,n)
            embed.add_field(name="roll結果", value=res, inline=False)
        await ctx.send(embed=embed)
    
    @roll.command()
    async def key(self,ctx,a,*key):
        a = int(a)
        embed = discord.Embed(color=0x0080ff)
        if len(key)<a:
            embed.add_field(name='ERROR',value='個数が多すぎます')
        else:
            res = ' '.join(random.sample(key,a))
            embed.add_field(name="roll結果", value=res, inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Roll(bot))