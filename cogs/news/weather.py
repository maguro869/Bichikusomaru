import requests
import discord
import datetime
import pytz
import aiohttp

async def get_API() -> dict:
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=150010'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            if res.status == 200:
                api_data = await res.json()
                return api_data

def today(api_data) -> str:
    forecasts = api_data['forecasts']
    text = api_data['description']['text']
    for f in forecasts:
        if f['dateLabel'] == '明日':
            tenki = f['telop']
            
            try:
                max_temp = f['temperature']['max']['celsius']
            except:
                max_temp = '不明'
    
    return tenki,max_temp,text

def create_message(tenki,max_temp,text):
    date = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    embed=discord.Embed(title="お天気情報", description=date.strftime('%m{0}%d{1}').format('月','日')+"新潟の天気", color=0x0080ff)
    embed.add_field(name="天気", value=tenki, inline=False)
    embed.add_field(name="最高気温", value=max_temp, inline=True)
    if '雨' in tenki:
        embed.add_field(name="傘", value="いる", inline=True)
    else:
        embed.add_field(name="傘", value="いらない", inline=True)
    embed.add_field(name='詳細情報', value=text, inline=True)
    return embed
