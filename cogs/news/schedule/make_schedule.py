schedule_list = []
kamoku = {0:'休日',1:'設計',2:'ネ概',3:'健社',4:'ヘリ',5:'情2',6:'言Ⅰ',7:'Java',8:'ネ応',9:'SQL',10:'修了',11:'J検',,999:'不明'}

for i in range(1,32):
    print(kamoku)
    schedule_list.append(input())

text = '\n'.join(schedule_list)
with open('res.txt',mode='w',encoding='utf8') as f:
    f.write(text)
