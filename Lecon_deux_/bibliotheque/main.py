import bibliotheque
import livres
import reader
import json

print("S.P.Q.R.")

try:
    data_base_de_livres = open("livres_d_b.json", "r")
    data_base_des_readers = open("readers_d_b.json", "r")
except FileNotFoundError:
    data_base_de_livres = open("livres_d_b.json", "w")
    data_base_des_readers = open("readers_d_b.json", "w")
    list_de_livres = []
    list_des_readers = []
else:
    list_de_livres = json.load(data_base_de_livres)
    list_des_readers = json.load(data_base_des_readers)
finally:
    data_base_de_livres.close()
    data_base_des_readers.close()

list_de_livres = [
    livres.Livre(
        str(element["id_livre"]),
        element["nom"],
        element["author"],
        element["year"],
        element["triger"],
    )
    for element in list_de_livres
]
list_des_readers = [
    reader.Reader(
        element["nom"],
        element["prenom"],
        element["birth_jour"],
        element["birth_mois"],
        element["birth_an"],
        element["rue"],
        element["maison"],
        str(element["id_reader"]),
        element["list_des_livres_reader"],
    )
    for element in list_des_readers
]
current_biblioteque = bibliotheque.Bibliotheque(
    list_de_livres, list_des_readers
)

while True:
    user_input_1 = input(
        "\n____Библиотека____\n\n"
        "Основное меню\n"
        "Выберите действие\n"
        "1 - добавить книгу\n"
        "2 - удалить книгу\n"
        "3 - выдать книгу читателю\n"
        "4 - принять книгу от читателя\n"
        "5 - показать список книг в библиотеке\n"
        "6 - показать список книг в наличии\n"
        "7 - показать список книг выданных читателям\n"
        "8 - сортировка книг в библиотеке\n"
        "9 - добавить читателя\n"
        "10 - показать список читателей\n"
        "0 - выход из программы\n"
        "Ваш выбор: "
    )

    if user_input_1 == "1":
        new_livre = livres.Livre("0", "nom", "author", "2021", triger=1)
        new_livre.id_livre = input("Введите id книги: ")
        new_livre.nom = input("Введите название книги: ")
        new_livre.author = input("Введите автора книги: ")
        new_livre.year = input("Введите год издания книги: ")

        current_biblioteque.plus_livre(new_livre)

    elif user_input_1 == "2":
        user_input_2 = input("Введите id книги для удаления: ")
        while not user_input_2.isdigit():
            user_input_2 = input("Введите id книги для удаления: ")
        current_biblioteque.delete_livre(int(user_input_2))

    elif user_input_1 == "3":
        user_input_2 = input("Введите id книги: ")
        user_input_3 = input("Введите id читателя: ")
        while not user_input_2.isdigit() or not user_input_3.isdigit():
            user_input_2 = input("Введите id книги: ")
            user_input_3 = input("Введите id читателя: ")
        current_biblioteque.envoyer_livre_a_reader(
            int(user_input_2), int(user_input_3)
        )

    elif user_input_1 == "4":
        user_input_2 = input("Введите id книги: ")
        user_input_3 = input("Введите id читателя: ")
        while not user_input_2.isdigit() or not user_input_3.isdigit():
            user_input_2 = input("Введите id книги: ")
            user_input_3 = input("Введите id читателя: ")
        current_biblioteque.ajouter_livre_de_reader(
            int(user_input_2), int(user_input_3)
        )

    elif user_input_1 == "5":
        current_biblioteque.get_list_livres_all()

    elif user_input_1 == "6":
        current_biblioteque.get_list_livres_dans_bibliotheque()

    elif user_input_1 == "7":
        current_biblioteque.get_list_livres_dans_readers()

    elif user_input_1 == "8":
        user_input_4 = input(
            "Сортировка по названию книги - нажмите 1\n"
            "Сортировка по автору книги - нажмите 2\n"
            "Сортировка по году издания книги - нажмите 3\n"
        )
        if user_input_4 == "1":
            current_biblioteque.sort_de_nom()
        elif user_input_4 == "2":
            current_biblioteque.sort_de_author()
        elif user_input_4 == "3":
            current_biblioteque.sort_de_year()

    elif user_input_1 == "9":
        new_reader = reader.Reader(
            "nom", "prenom", "1", "1", "0000", "rue", "1", "0000", []
        )

        new_reader.nom = input("Введите имя читателя: ")
        new_reader.prenom = input("Введите фамилию читателя: ")
        new_reader.birth_jour = input("Введите день рождения читателя: ")
        new_reader.birth_mois = input("Введите месяц рождения читателя: ")
        new_reader.birth_an = input("Введите год рождения читателя: ")
        new_reader.rue = input("Введите улицу прописки читателя: ")
        new_reader.maison = input("Введите дом прописки читателя: ")
        new_reader.id_reader = input("Введите id читателя: ")

        current_biblioteque.plus_reader(new_reader)

    elif user_input_1 == "10":
        current_biblioteque.get_list_readers_all()

    elif user_input_1 == "0":
        data_base_de_livres = open("livres_d_b.json", "w")
        data_base_des_readers = open("readers_d_b.json", "w")
        list_de_livres = [
            livre.__dict__ for livre in current_biblioteque.list_livres
        ]
        list_des_readers = [
            element.faire_dict() for element in current_biblioteque.list_readers
        ]
        data_pour_ecrire = json.dumps(list_de_livres, indent=4)
        data_pour_ecrire_2 = json.dumps(list_des_readers, indent=4)
        data_base_de_livres.write(data_pour_ecrire)
        data_base_de_livres.close()
        data_base_des_readers.write(data_pour_ecrire_2)
        data_base_des_readers.close()

        input("Нажмите любую клавишу для выхода")
        break
