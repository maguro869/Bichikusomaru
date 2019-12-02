import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="help")
    async def _help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed=discord.Embed(title="help",description='それぞれのコマンド名の先頭に「**b!**」をつけて実行してね\nコマンドの詳細はhelp 〇〇(コマンド名)',color=0x0080ff)
            embed.add_field(name="**roll**", value="ロール機能です\n数字やキーワードをランダムで選出してくれます", inline=False)
            embed.add_field(name="**yn**", value="YesかNoかを教えてくれます", inline=False)
            embed.add_field(name="**cat**", value=":cat: 猫の画像を表示します", inline=False)
            embed.add_field(name="**fox**", value=":fox: 狐の画像を表示します", inline=False)
            embed.add_field(name="**dog**",value=":dog: 犬の画像を表示します", inline=False)
            embed.add_field(name='**gif keyword**',value='keywordに関連したgifを表示します',inline=False)
            embed.add_field(name="**sche**", value='時間割を表示します')
            await ctx.send(embed=embed)
    
    @_help.command()
    async def roll(self,ctx):
        embed=discord.Embed(title="help roll",color=0x0080ff)
        embed.add_field(name='roll num a b n',value='a~bの範囲の値をn個表示します',inline=False)
        embed.add_field(name='roll key a 候補1 候補2 … 候補n', value='n個の候補の中からa個選びます',inline=False)
        await ctx.send(embed=embed)
    @_help.command()
    async def yn(self,ctx):
        embed=discord.Embed(title="help yn",color=0x0080ff)
        embed.add_field(name="**yn**", value="YesかNoかを教えてくれます", inline=False)
        await ctx.send(embed=embed)
    @_help.command()
    async def cat(self,ctx):
        embed=discord.Embed(title="help cat",color=0x0080ff)
        embed.add_field(name="**cat**", value=":cat: 猫の画像を表示します", inline=False)
        await ctx.send(embed=embed)
    @_help.command()
    async def fox(self,ctx):
        embed=discord.Embed(title="help fox",color=0x0080ff)
        embed.add_field(name="**fox**", value=":fox: 狐の画像を表示します", inline=False)
        await ctx.send(embed=embed)
    @_help.command()
    async def dog(self,ctx):
        embed=discord.Embed(title="help dog",color=0x0080ff)
        embed.add_field(name="**dog**",value=":dog: 犬の画像を表示します", inline=False)
        await ctx.send(embed=embed)
    @_help.command()
    async def gif(self,ctx):
        embed=discord.Embed(title='help gif',color=0x0080ff)
        embed.add_field(name='**gif keyword**',value='keywordに関連したgifを表示します', inline=False)
        await ctx.send(embed=embed)
    @_help.command()
    async def sche(self,ctx):
        embed=discord.Embed(title='help sche',color=0x0080ff)
        embed.add_field(name='**sche**',value='今日の時間割を表示します\nsche todayでも動きます', inline=False)
        embed.add_field(name='**sche tomorrow**',value='明日の時間割を表示します', inline=False)
        await ctx.send(embed=embed)
def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))
