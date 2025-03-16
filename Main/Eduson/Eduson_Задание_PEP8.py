# Ввод коэффициентов
first_coefficient = int(input('a = ', ))
second_coefficient = int(input('b = ', ))
third_coefficient = int(input('c = ', ))

# Решение по сокращенной формуле, т.к. b - четное
if first_coefficient != 0 and second_coefficient % 2 == 0 and third_coefficient != 0:
    k = second_coefficient / 2
    d = k ** 2 - first_coefficient * third_coefficient
    x1 = (-k + d ** 0.5) / first_coefficient
    x2 = (-k - d ** 0.5) / first_coefficient
    print('Так как коэффициент b - четное число, то решаем по сокращенной формуле')
    print(f'Дискриминант = {d}')
    if d != 0:
        print(f'Первый корень = {x1}')
        print(f'Второй корень = {x2}')
    else:
        print(f'Корень уравнения = {x1}')

# Решение уравнения при a = 0, b = 0 и c = 0
elif first_coefficient == 0 and second_coefficient == 0 and third_coefficient == 0:
        print(f'Корни уравнения равны нулю')

# Решение уравнения при с = 0
elif first_coefficient != 0 and second_coefficient != 0 and third_coefficient == 0:
        print(f'Корень уравнения равен либо нулю, либо {-second_coefficient / first_coefficient}')

# Решение уравнения при b = 0 и c = 0
elif first_coefficient != 0 and second_coefficient == 0 and third_coefficient == 0:
        print(f'Корни уравнения равны нулю')

# Решение полного уравнения
elif first_coefficient != 0 and second_coefficient % 2 != 0 and third_coefficient != 0:
    d = second_coefficient ** 2 - 4 * first_coefficient * third_coefficient
    if d > 0:
        x1 = (-second_coefficient + d ** 0.5) / (2 * first_coefficient)
        print(f'Дискриминант = {d}')
        print(f'Первый корень = {round(x1, 2)}')
        x2 = (-second_coefficient - d ** 0.5) / (2 * first_coefficient)
        print(f'Второй корень = {round(x2, 2)}')
    elif d < 0:
        print(f'Так как дискриминант меньше нуля и равен: {d}')
        print('то действительных корней нет')
    else:
        k = -second_coefficient / (2 * first_coefficient)
        print(f'Уравнение имеет один корень: {k}')

        # Решение уравнения при b = 0
        if first_coefficient != 0 and third_coefficient != 0 and second_coefficient == 0:
            if (- third_coefficient / first_coefficient) >= 0:
                x1 = (-third_coefficient / first_coefficient) ** 0.5
                print(f'Первый корень равен: {x1}')
                x2 = (-1) * ((-third_coefficient / first_coefficient) ** 0.5)
                print(f'Второй корень равен: {x2}')
        if (- third_coefficient / first_coefficient) < 0:
            print(f' -third_coefficient / first_coefficient = : {-third_coefficient / first_coefficient},'
                  f'т.е. < 0, поэтому действительных корней нет')
else:
    print('Корней не существует')