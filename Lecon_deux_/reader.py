import re


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
        if key == 'id_reader':
            if not value.isdigit():
                print('Некорректный id!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value

        elif key == 'nom':
            if not value.isalpha():
                print('Некорректное имя!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value.title()

        elif key == 'prenom':
            if not value.isalpha():
                print('Некорректная фамилия!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value.title()

        elif key == 'birth_jour':
            if not value.isdigit() or int(value) not in range(1, 32):
                print('Некорректный день!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value

        elif key == 'birth_mois':
            if not value.isdigit() or int(value) not in range(1, 13):
                print('Некорректный месяц!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value

        elif key == 'birth_an':
            if not value.isdigit() or len(value) != 4:
                print('Некорректный год!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value

        elif key == 'rue':
            if re.findall(r'[^a-zA-Zа-яА-Я0-9]', value):
                print('Некорректное название улицы!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value

        elif key == 'maison':
            if not value.isdigit():
                print('Некорректный номер дома!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value

        else:
            self.__dict__[key] = value
