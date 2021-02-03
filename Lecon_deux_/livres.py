import re


class Livre:
    def __init__(
        self, id_livre: str, nom: str, author: str, year: str, triger: int
    ) -> None:
        """
        Создаем объект класса Книга.
        Необходимо передать пять атрибутов. Первые четыре - str. Пятый - int.
        :param id_livre: id
        :param nom: название
        :param author: автор
        :param year: год издания
        :param triger: триггер (0 - книгу у читателя или 1 - книга в библи-ке)
        """
        self.id_livre = id_livre
        self.nom = nom
        self.author = author
        self.year = year
        self.triger = triger

    def __setattr__(self, key, value):
        if key == 'id_livre':
            if not value.isdigit():
                print('Некорректный id')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value

        elif key == 'nom':
            if not re.findall(r'\w', value):
                print('Некорректное название книги')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value.title()

        elif key == 'author':
            if re.findall(r'[^a-zA-Zа-яА-Я, \s]', value):
                print('Некорректный автор!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value.title()

        elif key == 'year':
            if not value.isdigit() or len(value) != 4:
                print('Некорректный год')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value

        else:
            self.__dict__[key] = value
