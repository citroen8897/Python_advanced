# 2. Класс книга
#     Поля:
#         - ID
#         - Название
#         - Автор
#         - Год издания
#         - ??? (этот параметр нужен!!!)

class Livre:
    def __init__(self, id_livre, nom, author, year, triger):
        self.id_livre = id_livre
        self.nom = nom
        self.author = author
        self.year = year
        self.triger = triger

