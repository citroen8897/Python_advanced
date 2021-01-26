# Проверка существования уравнения и нахождение его корней


def main():
    print('S.P.Q.R.\nВсе коефициенты должны быть целочисленными!')

    try:
        a_start = int(input('Задайте начало диапазона для первого '
                            'коефициента: '))
        a_fin = int(input('Задайте конец диапазона для первого '
                          'коефициента: '))
        b_start = int(input('Задайте начало диапазона для второго '
                            'коефициента: '))
        b_fin = int(input('Задайте конец диапазона для второго '
                          'коефициента: '))
        c_start = int(input('Задайте начало диапазона для третьего '
                            'коефициента: '))
        c_fin = int(input('Задайте конец диапазона для третьего '
                          'коефициента: '))

    except ValueError:
        print('Ошибка! Задано не целое число.\n')

    else:
        x_list = []
        for a in range(a_start, a_fin + 1):
            for b in range(b_start, b_fin + 1):
                for c in range(c_start, c_fin + 1):
                    if b ** 2 - 4 * a * c >= 0:
                        diskriminant = b ** 2 - 4 * a * c
                        x_1 = (-b + diskriminant ** (1 / 2)) / 2 * a
                        x_2 = (-b - diskriminant ** (1 / 2)) / 2 * a
                        x_list.append((x_1, x_2))
                        print(f'Уравнение с коефициентами {a}, {b}, {c} '
                              f'существует.\nКорни уравнения: {x_1}, {x_2}\n')

        if len(x_list) == 0:
            print('В заданных диапазонах не существует ни одного уравнения!\n')

    finally:
        continuer = input('Проверить другие диапазоны?\nД/н')
        if continuer == 'Д':
            print()
            main()
        else:
            input('Нажмите любую клавишу')
            exit()


if __name__ == '__main__':
    main()
