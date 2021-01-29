#     Методы:
#         - Отдать книгу читателю
#         - Принять книгу от читателя
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

    def plus_reader(self, new_reader):
        self.list_readers.append({'nom': new_reader.nom,
                                  'prenom': new_reader.prenom,
                                  'id': new_reader.id_reader,
                                  'list_des_livres_reader':
                                      new_reader.list_des_livres_reader})

    def get_list_livres_all(self):
        j = 1
        for element in self.list_livres:
            print(f'{j}. {element["nom"]}')
            j += 1

    def get_list_livres_dans_bibliotheque(self):
        j = 1
        for element in self.list_livres:
            if element['triger'] == 1:
                print(f'{j}. {element["nom"]}')
                j += 1

    def get_list_livres_dans_readers(self):
        j = 1
        for element in self.list_livres:
            if element['triger'] == 0:
                print(f'{j}. {element["nom"]}')
                j += 1

    def get_list_readers_all(self):
        j = 1
        for element in self.list_readers:
            print(f'{j}. {element["prenom"]} {element["nom"]} {element["id"]}')
            j += 1
