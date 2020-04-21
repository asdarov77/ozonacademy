import random

result=0  # результат угадал не угадал. Если угадал,то result=1
rangemax=int(input('Введи максимальное число Угадайки: '))
rndnum=random.randint(1,rangemax)
print('введи сложность: 1 сложный, 2 средний, 3 низкий')
difficult=int(input('твой выбор: '))
if difficult == 1:
    len=6
    print('сложный уровень,у тебя',len, 'попыток' )
elif difficult == 2:
    len=9
    print('средний уровень,у тебя', len, 'попыток')
else:
    len=12
    print('простой уровень,у тебя', len, 'попыток')

for i in range(0, len):
    print('угадай цифру')
    num = int(input())
    if num > rndnum:
        print('чуточку поменьше, у тебя',(len-1-i),'попыток')
        i += 1
    elif num < rndnum:
        print('почти,но чуть больше , у тебя',(len-1-i),'попыток')
        i += 1
    else:
        print('ты угадал! это число ', rndnum)
        result=1
        break
if result !=1:
    print('видимо,сегодня удача не на твоей стороне. Попробуем в другой раз')




