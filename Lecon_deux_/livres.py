class Livre:
    def __init__(
        self, id_livre: str, nom: str, author: str, year: str, triger: int
    ) -> None:
        """
        Создаем объект класса Книга.
        Необходимо передать пять атрибутов. Первые четыре - str. Пятый - int.
        :param id_livre:
        :param nom:
        :param author:
        :param year:
        :param triger:
        """
        self.id_livre = id_livre
        self.nom = nom
        self.author = author
        self.year = year
        self.triger = triger
