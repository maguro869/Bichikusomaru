import discord
from discord.ext import commands
import random


class Roll(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def roll(self,ctx,a,b,n):
        ia = int(a)
        ib = int(b)
        _in = int(n)
        
        if ia>ib:
            ia,ib = ib,ia
        if ib - ia < _in:
            await ctx.send('値の範囲が小さいです')
        else:
            li = [i for i in range(ia,ib+1)]
            res = random.sample(li,_in)
            embed=discord.Embed(color=0x0080ff)
            embed.add_field(name="roll結果", value=res, inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Roll(bot))