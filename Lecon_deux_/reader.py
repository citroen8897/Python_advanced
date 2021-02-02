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
