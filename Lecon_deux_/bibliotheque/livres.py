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
            while not value.isdigit():
                print('Некорректный id!')
                value = input('Введите корректный id: ')
            self.__dict__[key] = int(value)

        elif key == 'nom':
            while not re.findall(r'\w', value):
                print('Некорректное название книги!')
                value = input('Введите корректно название книги: ')
            self.__dict__[key] = value.title()

        elif key == 'author':
            while re.findall(r'[^a-zA-Zа-яА-Я, \s]', value):
                print('Некорректный автор!')
                value = input('Введите корректно автора книги: ')
            self.__dict__[key] = value.title()

        elif key == 'year':
            while not value.isdigit() or len(value) != 4:
                print('Некорректный год!')
                value = input('Введите корректно год издания книги: ')
            self.__dict__[key] = value

        else:
            self.__dict__[key] = value

    def __str__(self):
        return f'\nНазвание: {self.nom}\nАвтор: {self.author}\n' \
               f'Год: {self.year}\nid: {self.id_livre}\n'

    @classmethod
    def faire_object_livre(cls, dict_data: dict):
        return cls(
            str(dict_data['id_livre']),
            dict_data["nom"],
            dict_data['author'],
            dict_data['year'],
            dict_data['triger']
            )
