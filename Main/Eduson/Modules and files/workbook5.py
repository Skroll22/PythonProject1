import os

def del_comments(file_name, new_file_name):
    base_path = r'C:\Users\Kirill\PycharmProjects\PythonProject\Main\Eduson\Modules and files'
    input_file_path = os.path.join(base_path, file_name)
    output_file_path = os.path.join(base_path, new_file_name)
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        new_lines = []
        for line in lines:
            cleaned_line = line.split('#')[0].rstrip()
            new_lines.append(cleaned_line)
        with open(output_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write('\n'.join(new_lines))

        print('Комментарии успешно удалены')

    except FileNotFoundError:
        print(f'Ошибка: файл "{file_name}" не найден.')
    except IOError as e:
        print(f'Ошибка при работе с файлом: "{e}"')
    except Exception as e:
        print(f'Произошла ошибка: "{e}"')


del_comments(input('Введите имя исходного файла: '), input('Введите имя конечного файла: '))