import bibliotheque
import livres
import reader

print('S.P.Q.R.')
list_de_livres = []
list_des_readers = []

while True:
    current_biblioteque = bibliotheque.Bibliotheque(list_de_livres,
                                                    list_des_readers)

    user_input_1 = input('\nВыберите действие\n'
                         '1 - добавить книгу\n'
                         '2 - удалить книгу\n'
                         '3 - отдать книгу читателю\n'
                         '4 - принять книгу от читателя\n'
                         '5 - показать список книг в библиотеке\n'
                         '6 - показать список книг в наличии\n'
                         '7 - показать список книг выданных читателям\n'
                         '9 - добавить читателя\n'
                         '10 - показать список читателей\n'
                         '0 - выход из программы\n'
                         'Ваш выбор: ')

    if user_input_1 == '1':
        new_livre = livres.Livre(input('id книги: '),
                                 input('Название: '),
                                 input('Автор: '),
                                 input('Год издания: '),
                                 triger=1)
        bibliotheque.Bibliotheque.plus_livre(current_biblioteque,
                                             new_livre=new_livre)

    elif user_input_1 == '2':
        user_input_2 = input('Введите id книги для удаления: ')
        bibliotheque.Bibliotheque.delete_livre(current_biblioteque,
                                               str(user_input_2))

    elif user_input_1 == '3':
        user_input_2 = input('Введите id книги: ')
        user_input_3 = input('Введите id читателя: ')
        bibliotheque.Bibliotheque.envoyer_livre_a_reader(current_biblioteque,
                                                         user_input_2,
                                                         user_input_3)

    elif user_input_1 == '4':
        user_input_2 = input('Введите id книги: ')
        user_input_3 = input('Введите id читателя: ')
        bibliotheque.Bibliotheque.ajouter_livre_de_reader(current_biblioteque,
                                                          user_input_2,
                                                          user_input_3)

    elif user_input_1 == '5':
        bibliotheque.Bibliotheque.get_list_livres_all(current_biblioteque)

    elif user_input_1 == '6':
        bibliotheque.Bibliotheque.get_list_livres_dans_bibliotheque(
            current_biblioteque)

    elif user_input_1 == '7':
        bibliotheque.Bibliotheque.get_list_livres_dans_readers(
            current_biblioteque)

    elif user_input_1 == '9':
        new_reader = reader.Reader(input('Имя: '),
                                   input('Фамилия: '),
                                   input('id: '),
                                   [])
        bibliotheque.Bibliotheque.plus_reader(current_biblioteque,
                                              new_reader=new_reader)

    elif user_input_1 == '10':
        bibliotheque.Bibliotheque.get_list_readers_all(current_biblioteque)

    elif user_input_1 == '0':
        input('Нажмите любую клавишу для выхода')
        break
