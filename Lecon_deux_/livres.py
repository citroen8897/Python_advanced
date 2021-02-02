class Livre:
    def __init__(
        self, id_livre: str, nom: str, author: str, year: str, triger: int
    ) -> None:
        """
        Создаем объект класса Книга.
        Необходимо передать пять атрибутов. Первые четыре - str. Пятый - int.
        :param id_livre: id
        :param nom: название
        :param author: автор
        :param year: год издания
        :param triger: триггер (0 - книгу у читателя или 1 - книга в библи-ке)
        """
        self.id_livre = id_livre
        self.nom = nom
        self.author = author
        self.year = year
        self.triger = triger
