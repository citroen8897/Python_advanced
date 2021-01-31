# def decorator_1(func):
#     def wrapper(x, y):
#         print('Выполняется декоратор')
#         result_main = x ** y
#         result_dekor = x ** (y + 1)
#         return result_main, result_dekor
#     return wrapper
#
#
# @decorator_1
# def func_1(a, b):
#     return a ** b
#
#
# print(func_1(2, 3))


def func_2(nom):
    def func_3(prenom):
        print(f"Bonjour {nom} {prenom}")

    return func_3


# func_2(input('Votre nom est: '), input('Votre prenom est: '))
func_2(input("Votre nom est: "))(input("Votre prenom est: "))

temp = func_2("Jerome")
temp("Roten")
