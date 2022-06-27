# Помните игру с конфетами из модуля "Математика и Информатика"? 
# Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом" 

def play_game(n, m, players):
    count = 0
    while n > 0:
        print(f'{players[count%2]}, ваш ход')
        move = int(input())
        n = n - move
        if n > 0: print(f'Осталось конфет:{n}')
        else: print('Все, конфеты кончились')
        count +=1
    return players[not count%2]

N = int(input('Общее количество конфет в игре:\n '))
M = int(input('Max количество конфет за один ход:\n '))

player_1 = input('Введите имя первого игрока\n')
player_2 = input('Введите имя второго игрока\n')
players = [player_1, player_2]

winner = play_game(N, M, players)
if not winner:
    print('ничья!')
else: print(f'Победил {winner}! Ура!')