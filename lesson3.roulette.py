"""

"""

import random
import time

cash=1000
print('В нашем распряжении 1000$.\nЕсли угадываете число,то получаете только сыгравшую ставку с коэф 5.\nЕсли число и цвет,то ставку с коэффициентом 17.\nУгадай один из секторов, и ты увеличишь свой кэш на величину ставки.\nИ,да,в нашем казино не ставят на Зеро.\n')
slovarColor={0:'Красный',1:'Черный'}

while cash>0:
    print('Делайте ставки,господа')
    print('Введи число от 1 до 36')
    cell=int(input('твое число: '))
    if cell <=0 or cell>36:
        print('Строго от 1 до 36\n')
        continue
    print('Введи цвет: красный -0,черный -1')
    color=int(input('твой цвет  '))
    if color not in range(0,2):
        print('строго 0 или 1\n')
        continue
    print('Введи сумму ставки  ')
    bet=int(input('твоя ставка: $'))
    if bet>cash/2:
        print('У тебя нет столько денег,введи меньше\n')
        continue
    print('Ставки сделаны, ставок больше нет \a')
    time.sleep(5)

    rndCell=random.randint(0,36)
    rndColor=random.randint(0,1)
    print('Выпал номер {} {}\n'.format(rndCell,slovarColor[rndColor]))
    time.sleep(5)           
    if cell==rndCell and color==rndColor:
        cash=cash+17*bet
        print('Бинго,везунчик.Твой выигрыш составил {}$, всего доступно {}$'.format(bet,cash))
        print('\n')
    elif cell==rndCell:
        cash=cash+5*bet
        print('Поздравляю,твой выигрыш составил {}$, всего доступно {}$'.format(bet,cash))
        print('\n')
    elif cell in range(1,13) and rndCell in range(1,13):
        cash=cash+bet
        print('Угадал первый сектор,твой выигрыш составил {}$, всего доступно {}$'.format(bet,cash))
        print('\n')
    elif cell in range(13,25) and rndCell in range(13,25):
        cash=cash+bet
        print('Угадал второй сектор,твой выигрыш составил{}$, всего доступно {}$'.format(bet,cash))
        print('\n')
    elif cell in range(25,37) and rndCell in range(25,37):
        cash=cash+bet
        print('Угадал третий сектор,твой выигрыш составил {}$, всего доступно {}$'.format(bet,cash))    
        print('\n')
    elif rndCell==0:
        cash==0
        print('Я извиняюсь,но выпало Зеро,все твои деньги сгорели')
    else:
        cash=cash-2*bet
        print('Отличная попытка разбогатеть,твой проигрыш составил {}$, всего доступно {}$'.format(bet,cash))
        print('\n')
print('Что бы ты не делал,но казино всегда в выигрыше')
