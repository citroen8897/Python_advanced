class Animal:
    def __init__(self, type_: str, nom_de_animal: str, age: str) -> None:
        self.type_ = type_
        self.nom_de_animal = nom_de_animal
        self.age = age

    def __str__(self):
        print(
            f"\nДанные животного:\nИмя: {self.nom_de_animal}\n"
            f"Вид: {self.type_}\nВозраст: {self.age}"
        )

    def __setattr__(self, key, value):
        if key == 'age':
            if not value.isdigit():
                print('Некорректный возраст!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value
        elif key == 'nom_de_animal':
            if not value.isalpha():
                print('Некорректное имя!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value.title()
        elif key == 'type_':
            if not value.isalpha():
                print('Некорректный вид!')
                self.__dict__[key] = 'не задано'
            else:
                self.__dict__[key] = value
