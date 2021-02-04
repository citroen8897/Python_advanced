import re
import livres


class Reader:
    def __init__(
        self,
        nom: str,
        prenom: str,
        birth_jour: str,
        birth_mois: str,
        birth_an: str,
        rue: str,
        maison: str,
        id_reader: str,
        list_des_livres_reader: list,
    ) -> None:
        """
        Создаем объект класса Читатель.
        Необходимо передать девять атрибутов.
        :param nom: имя
        :param prenom: фамилия
        :param birth_jour: день рождения
        :param birth_mois: месяц рождения
        :param birth_an: год рождения
        :param rue: улица
        :param maison: дом
        :param id_reader: id
        :param list_des_livres_reader: список книг читателя
        """
        self.nom = nom
        self.prenom = prenom
        self.birth_jour = birth_jour
        self.birth_mois = birth_mois
        self.birth_an = birth_an
        self.rue = rue
        self.maison = maison
        self.id_reader = id_reader
        self.list_des_livres_reader = list_des_livres_reader

    def __setattr__(self, key, value):
        if key == "id_reader":
            while not value.isdigit():
                print("Некорректный id!")
                value = input("Введите корректный id: ")
            self.__dict__[key] = int(value)

        elif key == "nom":
            while not value.isalpha():
                print("Некорректное имя!")
                value = input("Введите корректно имя: ")
            self.__dict__[key] = value.title()

        elif key == "prenom":
            while not value.isalpha():
                print("Некорректная фамилия!")
                value = input("Введите корректно фамилию: ")
            self.__dict__[key] = value.title()

        elif key == "birth_jour":
            while not value.isdigit() or int(value) not in range(1, 32):
                print("Некорректный день!")
                value = input("Введите корректно день: ")
            self.__dict__[key] = value

        elif key == "birth_mois":
            while not value.isdigit() or int(value) not in range(1, 13):
                print("Некорректный месяц!")
                value = input("Введите корректно месяц: ")
            self.__dict__[key] = value

        elif key == "birth_an":
            while not value.isdigit() or len(value) != 4:
                print("Некорректный год!")
                value = input("Введите корректно год: ")
            self.__dict__[key] = value

        elif key == "rue":
            while re.findall(r"[^a-zA-Zа-яА-Я0-9, \s]", value):
                print("Некорректное название улицы!")
                value = input("Введите корректно название улицы: ")
            self.__dict__[key] = value

        elif key == "maison":
            while not value.isdigit():
                print("Некорректный номер дома!")
                value = input("Введите корректно номер дома: ")
            self.__dict__[key] = value

        else:
            self.__dict__[key] = value

    def __str__(self):
        return f"{self.prenom} {self.nom}    id: {self.id_reader}"

    def faire_dict(self):
        self.list_des_livres_reader = [
            element.__dict__ for element in self.list_des_livres_reader
        ]
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "birth_jour": self.birth_jour,
            "birth_mois": self.birth_mois,
            "birth_an": self.birth_an,
            "rue": self.rue,
            "maison": self.maison,
            "id_reader": int(self.id_reader),
            "list_des_livres_reader": self.list_des_livres_reader,
        }

    @classmethod
    def faire_object_reader(cls, dict_data: dict):
        dict_data["list_des_livres_reader"] = [
            livres.Livre.faire_object_livre(livre)
            for livre in dict_data["list_des_livres_reader"]
        ]
        return cls(
            dict_data["nom"],
            dict_data["prenom"],
            dict_data["birth_jour"],
            dict_data["birth_mois"],
            dict_data["birth_an"],
            dict_data["rue"],
            dict_data["maison"],
            str(dict_data["id_reader"]),
            dict_data["list_des_livres_reader"],
        )
