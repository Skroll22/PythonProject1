import os


def unity_files(file_names):
    unity_content = ''
    base_path = r'C:\Users\Kirill\PycharmProjects\PythonProject\Main\Eduson\Modules and files'

    for file_name in file_names:
        input_file_path = os.path.join(base_path, file_name)

        try:
            with open(input_file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                unity_content += content + '\n'
        except FileNotFoundError:
            print(f'Ошибка: файл {file_name} не найден')
        except Exception as e:
            print(f'Произошла ошибка при открытии файла: "{file_name}". Ошибка: {e}')

    return unity_content


if __name__ == "__main__":
    file_name_input = input('Введите имена файлов через пробел: ')
    file_names = file_name_input.split()
    if not file_names:
        print('Ошибка: Не указаны файлы для объединения')
    else:
        result = unity_files(file_names)
        if result:
            print('Объединенное содержимое файлов:\n')
            print(result)