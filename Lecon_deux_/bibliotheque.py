class Bibliotheque:
    def __init__(self, list_livres: list, list_readers: list) -> None:
        """
        Создаем объект класса Библиотека.
        У объекта два атрибута - список книг и список пользователей
        :param list_livres:
        :param list_readers:
        """
        self.list_livres = list_livres
        self.list_readers = list_readers

    def plus_livre(self, new_livre: any) -> None:
        """
        Метод обавления новой книги в бибилиотеку.
        Необходимо передать пять атрибутов объекта Книга.
        Метод записывает атрибуты в словарь и добавляет его в список книг.
        В методе реализована проверка эксклюзивности Книги.
        :param new_livre: первые четыре атрибута str, пятый атрибут - int
        :return:
        """
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

    def delete_livre(self, id_livre: str) -> None:
        """
        Метод удаления книги из библиотеки.
        Необходимо передать id удаляемой книги.
        :param id_livre:
        :return:
        """
        id_livres_list = [element['id'] for element in self.list_livres]
        if id_livre in id_livres_list:
            for element in self.list_livres:
                if element['id'] == id_livre:
                    self.list_livres.pop(self.list_livres.index(element))
            print('Книга успешно удалена')
        else:
            print('Книга с таким id не найдена')

    def envoyer_livre_a_reader(self, id_livre: str, id_reader: str) -> None:
        """
        Метод выдачи книги читателю.
        Необходимо передать id книги и id читателя.
        :param id_livre:
        :param id_reader:
        :return:
        """
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

    def ajouter_livre_de_reader(self, id_livre: str, id_reader: str) -> None:
        """
        Метод приема книги от читателя.
        Необходимо передать id книги и id читателя.
        :param id_livre:
        :param id_reader:
        :return:
        """
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
        """
        Сортировка по названию книги.
        :return:
        """
        print('Сортировка по названию книги')
        j = 1
        for element in sorted(self.list_livres,
                              key=lambda element: element['nom']):
            print(f'{j}. {element["nom"]} {element["author"]} '
                  f'{element["year"]} {element["id"]}')
            j += 1

    def sort_de_author(self):
        """
        Сортировка по фамилии автора книги
        :return:
        """
        print('Сортировка по автору книги')
        j = 1
        for element in sorted(self.list_livres,
                              key=lambda element: element['author']):
            print(f'{j}. {element["nom"]} {element["author"]} '
                  f'{element["year"]} {element["id"]}')
            j += 1

    def sort_de_year(self):
        """
        Сортировка по году издания книги
        :return:
        """
        print('Сортировка по году издания')
        j = 1
        for element in sorted(self.list_livres,
                              key=lambda element: element['year']):
            print(f'{j}. {element["nom"]} {element["author"]} '
                  f'{element["year"]} {element["id"]}')
            j += 1

    def plus_reader(self, new_reader: any) -> None:
        """
        Метод добавления читателя в библиотеку.
        Необходимо передать девять атрибутов объекта Читатель.
        Первые восемь атрибутов - str. Девятый - list.
        В методе реализована проверка эксклюзивности Читателя.
        :param new_reader:
        :return:
        """
        temp_id_list = len(list(
            filter(lambda element: element['id'] == new_reader.id_reader,
                   self.list_readers)))
        temp_1 = len(list(
            filter(lambda element: element['nom'] == new_reader.nom,
                   self.list_readers)))
        temp_2 = len(list(
            filter(lambda element: element['prenom'] == new_reader.prenom,
                   self.list_readers)))
        temp_3 = len(list(
            filter(lambda element: element['birth_jour'] == new_reader.
                   birth_jour, self.list_readers)))
        temp_4 = len(list(
            filter(lambda element: element['birth_mois'] == new_reader.
                   birth_mois, self.list_readers)))
        temp_5 = len(list(
            filter(lambda element: element['birth_an'] == new_reader.birth_an,
                   self.list_readers)))

        if temp_1 != 0 and temp_2 != 0 and temp_3 != 0 and temp_4 != 0 and \
                temp_5 != 0:
            print('Пользователь с такими данными уже зарегистрирован!')

        elif temp_id_list != 0:
            print('id уже занят!')

        else:
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
            print('Пользователь успешно зарегистрирован!')

    def get_list_livres_all(self):
        """
        Показать список всех книг в бибилиотеке.
        :return:
        """
        print('\nСписок всех книг в библиотеке:\n')
        j = 1
        for element in self.list_livres:
            print(f'{j}. {element["nom"]} {element["author"]} '
                  f'{element["year"]}')
            j += 1

    def get_list_livres_dans_bibliotheque(self):
        """
        Показать список книг в наличии.
        :return:
        """
        print('\nСписок книг в наличии:\n')
        j = 1
        for element in self.list_livres:
            if element['triger'] == 1:
                print(f'{j}. {element["nom"]} {element["author"]} '
                      f'{element["year"]}')
                j += 1

    def get_list_livres_dans_readers(self):
        """
        Показать список книг на руках у читателей.
        :return:
        """
        print('\nСписок книг на руках у читателей:\n')
        j = 1
        for element in self.list_livres:
            if element['triger'] == 0:
                print(f'{j}. {element["nom"]} {element["author"]} '
                      f'{element["year"]}')
                j += 1

    def get_list_readers_all(self):
        """
        Показать список всех читателей.
        :return:
        """
        print('\nСписок зарегистрированных читателей:\n')
        j = 1
        for element in self.list_readers:
            print(f'{j}. {element["prenom"]} {element["nom"]} {element["id"]}')
            j += 1
