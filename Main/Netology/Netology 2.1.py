help = """
help - справка
add - добавить задачу
show - показать задачи
exit - выход"""

tasks_today = []
tasks_tomorrow = []
tasks_poslezavtra = []
other = []
tasks = [tasks_today, tasks_tomorrow, tasks_poslezavtra, other]
days = ['сегодня', 'завтра', 'послезавтра', 'другие']

run = True

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(help)
    elif command == 'add':
        task = input('Введите задачу: ')
        day = input('На какой день записать задачу? Введите "0", если не привязывать задачу ко дню: ')
        if day == 'сегодня':
            tasks_today.append(task)
        elif day == 'завтра':
            tasks_tomorrow.append(task)
        elif day == 'послезавтра':
            tasks_poslezavtra.append(task)
        elif day == '0':
            other.append(task)
        else:
            print('Некорректная запись')
    elif command == 'show':
        for i in range(len(tasks)):
            print(f'Задачи {days[i]}: {tasks[i]}')
    elif command == 'exit':
        print('До свидания')
        run = False
    else:
        print('Некорректная команда')