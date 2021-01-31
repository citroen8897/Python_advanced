# матрица 10х10 и поиск элементов


def main():
    user_numero = input("S.P.Q.R.\nЗадайте целое число для проверки: ")
    with open("matrix.txt", "r") as file_matrix:
        matrix = [line.split() for line in file_matrix]

    index_lines = [
        matrix.index(line) for line in matrix if user_numero in line
    ]

    matrix_transpose = [
        [line[j] for line in matrix] for j in range(len(matrix))
    ]

    index_rows = [
        matrix_transpose.index(line)
        for line in matrix_transpose
        if user_numero in line
    ]

    if len(index_lines) == 0:
        print(f"Число {user_numero} в матрице отсутствует\n")
    else:
        print(
            f"Число {user_numero} встречается в строках: "
            f'{", ".join(map(str, index_lines))}'
        )
        print(
            f"Число {user_numero} встречается в столбцах: "
            f'{", ".join(map(str, index_rows))}'
        )

    continuer = input("\nПроверить другое число?\nД/н")
    if continuer == "Д":
        print()
        main()
    else:
        input("Нажмите любую клавишу")
        exit()


if __name__ == "__main__":
    main()
