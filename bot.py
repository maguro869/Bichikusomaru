from discord.ext import commands
import discord
import random
import traceback

bot = commands.Bot(command_prefix='$', description='A bot that greets the user back.')
TOKEN = 'NjMyMDg4NzY3NzYyNzkyNDU5.XdYevQ.hZP90gXjaeKn3fw5Q88gbIO73Rw'

cogs = [
    'cogs.help',
    'cogs.animals',
    'cogs.gif',
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

@bot.command()
async def roll(ctx,a,b,n):
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

@bot.command()
async def yn(ctx):
    yn_list = ['https://gph.is/2ud7xAC','https://gph.is/g/EqNGrd7']
    await ctx.send(random.choice(yn_list))


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
 

bot.run(TOKEN)