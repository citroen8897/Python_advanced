class Bibliotheque:
    def __init__(self, list_livres, list_readers):
        self.list_livres = list_livres
        self.list_readers = list_readers

    def plus_livre(self, new_livre):
        id_livres_list = [element['id'] for element in self.list_livres]
        if new_livre.id_livre in id_livres_list:
            print('Книга с таким id уже существует!')
        else:
            self.list_livres.append({'id': new_livre.id_livre,
                                     'nom': new_livre.nom,
                                     'author': new_livre.author,
                                     'year': new_livre.year,
                                     'triger': new_livre.triger})
            print('Книга успешно добавлена')

    def delete_livre(self, id_livre):
        id_livres_list = [element['id'] for element in self.list_livres]
        if id_livre in id_livres_list:
            for element in self.list_livres:
                if element['id'] == id_livre:
                    self.list_livres.pop(self.list_livres.index(element))
            print('Книга успешно удалена')
        else:
            print('Книга с таким id не найдена')

    def envoyer_livre_a_reader(self, id_livre, id_reader):
        id_livres_list = [element['id'] for element in self.list_livres]
        id_readers_list = [element['id'] for element in self.list_readers]
        if id_livre in id_livres_list and id_reader in id_readers_list:
            for livre in self.list_livres:
                for person in self.list_readers:
                    if livre['id'] == id_livre:
                        if person['id'] == id_reader:
                            if livre['triger'] == 1:
                                person['list_des_livres_reader'].append(livre)
                                livre['triger'] = 0
                                print('Книга успешно занесена в карточку '
                                      'читателя')
                            else:
                                print('Книга уже выдана другому читателю!')
        else:
            print('id книги или читателя не найден!')

    def ajouter_livre_de_reader(self, id_livre, id_reader):
        id_livres_list = [element['id'] for element in self.list_livres]
        id_readers_list = [element['id'] for element in self.list_readers]
        if id_livre in id_livres_list and id_reader in id_readers_list:
            for livre in self.list_livres:
                for person in self.list_readers:
                    if livre['id'] == id_livre:
                        if person['id'] == id_reader:
                            if livre['triger'] == 0:
                                if livre in person['list_des_livres_reader']:
                                    person['list_des_livres_reader'].pop(
                                        person['list_des_livres_reader'].index(
                                            livre))
                                    livre['triger'] = 1
                                    print('Книга успешно перемещена в список '
                                          'доступных книг')
                                else:
                                    print('У данного читателя нет этой книги!')
                            else:
                                print('Данная книга находится в библиотеке!')
        else:
            print('id книги или читателя не найден!')

    def sort_de_nom(self):
        print('Сортировка по названию книги')
        j = 1
        for element in sorted(self.list_livres,
                              key=lambda element: element['nom']):
            print(f'{j}. {element["nom"]} {element["author"]} '
                  f'{element["year"]} {element["id"]}')
            j += 1

    def sort_de_author(self):
        print('Сортировка по автору книги')
        j = 1
        for element in sorted(self.list_livres,
                              key=lambda element: element['author']):
            print(f'{j}. {element["nom"]} {element["author"]} '
                  f'{element["year"]} {element["id"]}')
            j += 1

    def sort_de_year(self):
        print('Сортировка по году издания')
        j = 1
        for element in sorted(self.list_livres,
                              key=lambda element: element['year']):
            print(f'{j}. {element["nom"]} {element["author"]} '
                  f'{element["year"]} {element["id"]}')
            j += 1

    def plus_reader(self, new_reader):
        self.list_readers.append({'nom': new_reader.nom,
                                  'prenom': new_reader.prenom,
                                  'birth_jour': new_reader.birth_jour,
                                  'birth_mois': new_reader.birth_mois,
                                  'birth_an': new_reader.birth_an,
                                  'rue': new_reader.rue,
                                  'maison': new_reader.maison,
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
