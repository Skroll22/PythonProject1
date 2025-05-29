import random

game = True # Игра идет
print('Игра начата. Игровое поле:')
# пустое игровое поле
start = [['*' for i in range(3)] for i in range(3)]
window = start.copy()
for row in window:
    print(*row)


def game_window():
    for row in window:
        print(*row)


while game:
    bot_move = False
    # Ход человека
    while True:

        try:
            x = int(input('Введите номер строки: '))
            if x < 1 or x > 3:
                print('Ошибка. Повторите ввод')
                break
            y = int(input('Введите номер столбца: '))
            if y < 1 or y > 3:
                print('Ошибка. Повторите ввод')
                break
        except Exception as err:
            print('Ошибка. Повторите ввод')
            break

        # Проверка на возможность хода
        if window[x-1][y-1] != '*':
            print('Ход невозможен, ячейка занята. Повторите ввод.')
            break

        else:
            window[x-1][y-1] = 'O'
            bot_move = True
            break
#был ли ход победным?
    # ход бота
    while bot_move and any('*' in i for i in window):
        try:
            x = random.choice([0, 1, 2])
            y = random.choice([0, 1, 2])
            while window[x-1][y-1] != '*': # свободна ли ячейка
                x = random.choice([0, 1, 2])
                y = random.choice([0, 1, 2])
            else:
                window[x - 1][y - 1] = 'X'
                game_window()
                break
        except Exception as err:
            print('Что-то пошло не так...')
            break

    # если победить по двум проверкам, то напечатается 2 строки выйгрыше
    # проверка по строкам

    draw = True
    for i in window:
        if all(j == 'O' for j in i):
            print('Вы победили! Бот унижен')
            draw = False
            game = False
        elif all(j == 'X' for j in i):
            print('Похоже, что играли 2 бота...\nДля вас игра окончена.')
            draw = False
            game = False


    # проверка по столбцам
    for i in range(3):
        if all(window[j][i] == 'O' for j in range(3)):
            print('Вы победили! Бот унижен')
            draw = False
            game = False
        elif all(window[j][i] == 'X' for j in range(3)):
            print('Похоже, что играли 2 бота...\nДля вас игра окончена.')
            draw = False
            game = False

    # проверка по главной диагонали
    if all(window[i][i] == 'O' for i in range(3)):
        print('Вы победили! Бот унижен')
        draw = False
        game = False
    elif all(window[i][i] == 'X' for i in range(3)):
        print('Похоже, что играли 2 бота...\nДля вас игра окончена.')
        draw = False
        game = False

    # проверка по побочной диагонали
    if all(window[i][2-i] == 'O' for i in range(3)):
        print('Вы победили! Бот унижен')
        draw = False
        game = False
    elif all(window[i][2-i] == 'X' for i in range(3)):
        print('Похоже, что играли 2 бота...\nДля вас игра окончена.')
        draw = False
        game = False

    # проверка на ничью
    if draw and not any('*' in i for i in window):
        print('Ничья!')
        game = False