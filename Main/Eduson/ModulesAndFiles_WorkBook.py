import os
def add_line_numbers(file_name, new_file_name):
    base_path = r'C:\Users\Kirill\PycharmProjects\PythonProject\Main\Eduson'
    input_file_path = os.path.join(base_path, file_name)
    output_file_path = os.path.join(base_path, new_file_name)

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
    except FileNotFoundError:
        print(f'Ошибка: файл {file_name} не найден.')
        return
    except Exception as e:
        print(f'Произошла ошибка при чтении файла: {e}')
        return

    try:
        with open(output_file_path, 'w', encoding='utf-8') as new_file:
            for index, line in enumerate(content):
                new_file.write(f'{index + 1}: {line}')
        print(f'Номера строк успешно добавлены в файл: "{new_file_name}"')
    except Exception as e:
        print(f'Произошла ошибка при записи в файл: {e}')

file_name = input('Введите имя исходного файла с расширением: ')
new_file_name = input('Введите имя целевого файла с расширением: ')

add_line_numbers(file_name, new_file_name)


#print(os.getcwd())