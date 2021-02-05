import livres
import reader


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

    def plus_livre(self, new_livre: livres.Livre) -> None:
        """
        Метод добавления новой книги в бибилиотеку.
        Необходимо передать объект типа Книга.
        Метод записывает атрибуты переданного объекта Книга в словарь и
        добавляет его в список книг.
        В методе реализована проверка эксклюзивности Книги.
        :param new_livre: см. объект Книга -> livres.py
        :return:
        """
        id_livres_list = [element.id_livre for element in self.list_livres]
        if new_livre.id_livre in id_livres_list:
            print("Книга с таким id уже существует!")
        else:
            self.list_livres.append(new_livre)
            print("Книга успешно добавлена")

    def delete_livre(self, id_livre: int) -> None:
        """
        Метод удаления книги из библиотеки.
        Необходимо передать id удаляемой книги.
        :param id_livre:
        :return:
        """
        id_livres_list = [element.id_livre for element in self.list_livres]
        if id_livre in id_livres_list:
            for element in self.list_livres:
                if element.id_livre == id_livre:
                    self.list_livres.pop(self.list_livres.index(element))
            print("Книга успешно удалена")
        else:
            print("Книга с таким id не найдена")

    def envoyer_livre_a_reader(self, id_livre: int, id_reader: int) -> None:
        """
        Метод выдачи книги читателю.
        Необходимо передать id книги и id читателя.
        :param id_livre:
        :param id_reader:
        :return:
        """
        id_livres_list = [element.id_livre for element in self.list_livres]
        id_readers_list = [element.id_reader for element in self.list_readers]
        if id_livre in id_livres_list and id_reader in id_readers_list:
            for livre in self.list_livres:
                for person in self.list_readers:
                    if livre.id_livre == id_livre:
                        if person.id_reader == id_reader:
                            if livre.triger == 1:
                                person.list_des_livres_reader.append(livre)
                                livre.triger = 0
                                print(
                                    "Книга успешно занесена в карточку "
                                    "читателя"
                                )
                            else:
                                print("Книга уже выдана другому читателю!")
        else:
            print("id книги или читателя не найден!")

    def ajouter_livre_de_reader(self, id_livre: int, id_reader: int) -> None:
        """
        Метод приема книги от читателя.
        Необходимо передать id книги и id читателя.
        :param id_livre:
        :param id_reader:
        :return:
        """
        id_livres_list = [element.id_livre for element in self.list_livres]
        id_readers_list = [element.id_reader for element in self.list_readers]
        if id_livre in id_livres_list and id_reader in id_readers_list:
            for livre in self.list_livres:
                for person in self.list_readers:
                    if livre.id_livre == id_livre:
                        if person.id_reader == id_reader:
                            current_reader_livres = [
                                str(j) for j in person.list_des_livres_reader
                            ]
                            if livre.triger == 0:
                                if str(livre) in current_reader_livres:
                                    for (
                                        element
                                    ) in person.list_des_livres_reader:
                                        if str(livre) == str(element):
                                            person.list_des_livres_reader.pop(
                                                person.list_des_livres_reader.index(
                                                    element
                                                )
                                            )
                                            livre.triger = 1
                                            print(
                                                "Книга успешно перемещена в "
                                                "список доступных книг"
                                            )
                                else:
                                    print("У данного читателя нет этой книги!")

                            else:
                                print("Данная книга находится в библиотеке!")
        else:
            print("id книги или читателя не найден!")

    def sort_de_nom(self):
        """
        Сортировка по названию книги.
        :return:
        """
        print("Сортировка по названию книги")
        j = 1
        for element in sorted(
            self.list_livres, key=lambda element: element.nom
        ):
            print(f"{j}. {str(element)}")
            j += 1

    def sort_de_author(self):
        """
        Сортировка по фамилии автора книги
        :return:
        """
        print("Сортировка по автору книги")
        j = 1
        for element in sorted(
            self.list_livres, key=lambda element: element.author
        ):
            print(f"{j}. {str(element)}\n")
            j += 1

    def sort_de_year(self):
        """
        Сортировка по году издания книги
        :return:
        """
        print("Сортировка по году издания")
        j = 1
        for element in sorted(
            self.list_livres, key=lambda element: element.year
        ):
            print(f"{j}. {str(element)}")
            j += 1

    def plus_reader(self, new_reader: reader.Reader) -> None:
        """
        Метод добавления читателя в библиотеку.
        Необходимо передать объект типа Читатель.
        В методе реализована проверка эксклюзивности Читателя.
        :param new_reader: см. объект Читатель -> reader.py
        :return:
        """
        temp_id_list = len(
            list(
                filter(
                    lambda element: element.id_reader == new_reader.id_reader,
                    self.list_readers,
                )
            )
        )
        temp_1 = len(
            list(
                filter(
                    lambda element: element.nom == new_reader.nom,
                    self.list_readers,
                )
            )
        )
        temp_2 = len(
            list(
                filter(
                    lambda element: element.prenom == new_reader.prenom,
                    self.list_readers,
                )
            )
        )
        temp_3 = len(
            list(
                filter(
                    lambda element: element.birth_jour
                    == new_reader.birth_jour,
                    self.list_readers,
                )
            )
        )
        temp_4 = len(
            list(
                filter(
                    lambda element: element.birth_mois
                    == new_reader.birth_mois,
                    self.list_readers,
                )
            )
        )
        temp_5 = len(
            list(
                filter(
                    lambda element: element.birth_an == new_reader.birth_an,
                    self.list_readers,
                )
            )
        )

        if (
            temp_1 != 0
            and temp_2 != 0
            and temp_3 != 0
            and temp_4 != 0
            and temp_5 != 0
        ):
            print("Пользователь с такими данными уже зарегистрирован!")

        elif temp_id_list != 0:
            print("id уже занят!")

        else:
            self.list_readers.append(new_reader)
            print("Пользователь успешно зарегистрирован!")

    def delete_reader(self, id_reader: int) -> None:
        """
        Метод удаления пользователя.
        Необходимо передать id читателя для удаления
        :param id_reader:
        :return:
        """
        id_readers_list = [element.id_reader for element in self.list_readers]
        if id_reader in id_readers_list:
            for element in self.list_readers:
                if element.id_reader == id_reader:
                    self.list_readers.pop(self.list_readers.index(element))
            print("Читатель удален из картотеки")
        else:
            print("Читатель с таким id не найден")

    def get_list_livres_all(self):
        """
        Показать список всех книг в бибилиотеке.
        :return:
        """
        print("\nСписок всех книг в библиотеке:\n")
        j = 1
        for element in self.list_livres:
            print(f"{j}. {str(element)}")
            j += 1

    def get_list_livres_dans_bibliotheque(self):
        """
        Показать список книг в наличии.
        :return:
        """
        print("\nСписок книг в наличии:\n")
        j = 1
        for element in self.list_livres:
            if element.triger == 1:
                print(f"{j}. {str(element)}")
                j += 1

    def get_list_livres_dans_readers(self):
        """
        Показать список книг на руках у читателей.
        :return:
        """
        print("\nСписок книг на руках у читателей:\n")
        j = 1
        for element in self.list_livres:
            if element.triger == 0:
                print(f"{j}. {str(element)}")
                j += 1

    def get_list_readers_all(self):
        """
        Показать список всех читателей.
        :return:
        """
        print("\nСписок зарегистрированных читателей:\n")
        j = 1
        for element in self.list_readers:
            print(f"{j}. {str(element)}")
            j += 1
