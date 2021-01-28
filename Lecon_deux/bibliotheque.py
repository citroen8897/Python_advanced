# 1. Класс библиотека
#     Поля:
#         - список книг (list Books)
#         - список читателей (list Readers)
#
#     Методы:
#         - Добавить книгу
#         - Удалить книгу
#         - Отдать книгу читателю
#         - Принять книгу от читателя
#
#         - Вывести список всех книг
#         - Вывести список книг в библиотеке (в наличии)
#         - Вывести списк книг, которые не в наличии
#
#         - Отсортировать список книг по названию, автору, году издания
#         (lambda будет плюсом)

class Bibliotheque:
    def __init__(self, list_livres, list_readers):
        self.list_livres = list_livres
        self.list_readers = list_readers

    def plus_livre(self, new_livre):
        self.list_livres.append({'id': new_livre.id_livre,
                                 'nom': new_livre.nom,
                                 'author': new_livre.author,
                                 'year': new_livre.year,
                                 'triger': new_livre.triger})

    def delete_livre(self, id_livre):
        for element in self.list_livres:
            if element['id'] == id_livre:
                self.list_livres.pop(self.list_livres.index(element))
            else:
                print('Такой книги в библиотеке нет!')

    def get_list_livres_all(self):
        for element in self.list_livres:
            print(f'{element["nom"]}')
