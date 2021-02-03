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

while True:
    current_biblioteque = bibliotheque.Bibliotheque(
        list_de_livres, list_des_readers
    )

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
        new_livre = livres.Livre("0000", "xx", "yy", "2021", triger=1)

        new_livre.__setattr__("id_livre", input("id книги: "))
        while new_livre.id_livre == "не задано":
            new_livre.__setattr__("id_livre", input("id книги: "))

        new_livre.__setattr__("nom", input("Название книги: "))
        while new_livre.nom == "не задано":
            new_livre.__setattr__("nom", input("Название книги: "))

        new_livre.__setattr__("author", input("Автор книги: "))
        while new_livre.author == "не задано":
            new_livre.__setattr__("author", input("Автор книги: "))

        new_livre.__setattr__("year", input("Год издания книги: "))
        while new_livre.year == "не задано":
            new_livre.__setattr__("year", input("Год издания книги: "))

        bibliotheque.Bibliotheque.plus_livre(
            current_biblioteque, new_livre=new_livre
        )

    elif user_input_1 == "2":
        user_input_2 = input("Введите id книги для удаления: ")
        bibliotheque.Bibliotheque.delete_livre(
            current_biblioteque, str(user_input_2)
        )

    elif user_input_1 == "3":
        user_input_2 = input("Введите id книги: ")
        user_input_3 = input("Введите id читателя: ")
        bibliotheque.Bibliotheque.envoyer_livre_a_reader(
            current_biblioteque, user_input_2, user_input_3
        )

    elif user_input_1 == "4":
        user_input_2 = input("Введите id книги: ")
        user_input_3 = input("Введите id читателя: ")
        bibliotheque.Bibliotheque.ajouter_livre_de_reader(
            current_biblioteque, user_input_2, user_input_3
        )

    elif user_input_1 == "5":
        bibliotheque.Bibliotheque.get_list_livres_all(current_biblioteque)

    elif user_input_1 == "6":
        bibliotheque.Bibliotheque.get_list_livres_dans_bibliotheque(
            current_biblioteque
        )

    elif user_input_1 == "7":
        bibliotheque.Bibliotheque.get_list_livres_dans_readers(
            current_biblioteque
        )

    elif user_input_1 == "8":
        user_input_4 = input(
            "Сортировка по названию книги - нажмите 1\n"
            "Сортировка по автору книги - нажмите 2\n"
            "Сортировка по году издания книги - нажмите 3\n"
        )
        if user_input_4 == "1":
            bibliotheque.Bibliotheque.sort_de_nom(current_biblioteque)
        elif user_input_4 == "2":
            bibliotheque.Bibliotheque.sort_de_author(current_biblioteque)
        elif user_input_4 == "3":
            bibliotheque.Bibliotheque.sort_de_year(current_biblioteque)

    elif user_input_1 == "9":
        new_reader = reader.Reader(
            "nom", "prenom", "1", "1", "0000", "rue", "1", "0000", []
        )

        new_reader.__setattr__("nom", input("Имя читателя: "))
        while new_reader.nom == "не задано":
            new_reader.__setattr__("nom", input("Имя читателя: "))

        new_reader.__setattr__("prenom", input("Фамилия читателя: "))
        while new_reader.prenom == "не задано":
            new_reader.__setattr__("prenom", input("Фамилия читателя: "))

        new_reader.__setattr__("birth_jour", input("День рождения: "))
        while new_reader.birth_jour == "не задано":
            new_reader.__setattr__("birth_jour", input("День рождения: "))

        new_reader.__setattr__("birth_mois", input("Месяц рождения: "))
        while new_reader.birth_mois == "не задано":
            new_reader.__setattr__("birth_mois", input("Месяц рождения: "))

        new_reader.__setattr__("birth_an", input("Год рождения: "))
        while new_reader.birth_an == "не задано":
            new_reader.__setattr__("birth_an", input("Год рождения: "))

        new_reader.__setattr__("rue", input("Улица: "))
        while new_reader.rue == "не задано":
            new_reader.__setattr__("rue", input("Улица: "))

        new_reader.__setattr__("maison", input("Дом: "))
        while new_reader.maison == "не задано":
            new_reader.__setattr__("maison", input("Дом: "))

        new_reader.__setattr__("id_reader", input("id читателя: "))
        while new_reader.id_reader == "не задано":
            new_reader.__setattr__("id_reader", input("id читателя: "))

        bibliotheque.Bibliotheque.plus_reader(
            current_biblioteque, new_reader=new_reader
        )

    elif user_input_1 == "10":
        bibliotheque.Bibliotheque.get_list_readers_all(current_biblioteque)

    elif user_input_1 == "0":
        data_base_de_livres = open("livres_d_b.json", "w")
        data_base_des_readers = open("readers_d_b.json", "w")
        data_pour_ecrire = json.dumps(list_de_livres, indent=4)
        data_pour_ecrire_2 = json.dumps(list_des_readers, indent=4)
        data_base_de_livres.write(data_pour_ecrire)
        data_base_de_livres.close()
        data_base_des_readers.write(data_pour_ecrire_2)
        data_base_des_readers.close()

        input("Нажмите любую клавишу для выхода")
        break
