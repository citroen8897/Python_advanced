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
        :param nom:
        :param prenom:
        :param birth_jour:
        :param birth_mois:
        :param birth_an:
        :param rue:
        :param maison:
        :param id_reader:
        :param list_des_livres_reader:
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
