import bibliotheque
import livres

print('S.P.Q.R.')
list_de_livres = []
list_des_readers = []

while True:
    current_biblioteque = bibliotheque.Bibliotheque(list_de_livres,
                                                    list_des_readers)

    user_input_1 = input('Выберите действие\n1 - добавить книгу\n'
                         '2 - удалить книгу'
                         '\n5 - показать список книг в библиотеке'
                         '\nВаш выбор: ')

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

    elif user_input_1 == '5':
        bibliotheque.Bibliotheque.get_list_livres_all(current_biblioteque)

