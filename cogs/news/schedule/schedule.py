import discord

def make_schedule_list():
    kamoku = {0:'休日',1:'設計',2:'ネ概',3:'健社',4:'ヘリ',5:'情2',6:'言Ⅰ',7:'Java',8:'ネ応',9:'SQL',10:'修了',11:'J検',999:'不明'}

    with open('./cogs/news/schedule/src/12.txt', mode='r', encoding='utf8') as f:
        text = f.read()

    schedule_list = text.split('\n')

    for s in range(len(schedule_list)):
        if schedule_list[s] == '0':
            schedule_list[s] = '休日'
        
        else:
            work = schedule_list[s].split(' ')
            for w in range(1,len(work)):
                work[w] = work[w].split(':')
                work[w][1] = kamoku[int(work[w][1])]
            schedule_list[s] = work

    return schedule_list

def make_schedule_embed(today):
    schedule_list = make_schedule_list()
    embed=discord.Embed(title="講義情報")
    if len(schedule_list[today-1]) == 2:
        schedule = schedule_list[today-1]
        embed.add_field(name='予定',value=schedule)
        
    else:
        gen ,*schedule = schedule_list[today-1]
                
        for g in range(int(gen)):
            kyousitsu = schedule[g][0]
            kamoku = schedule[g][1]
            embed.add_field(name=f'{g+1}限目', value=f'{kamoku}\n{kyousitsu}', inline=False)
                   
    return embed