class Animal:
    def __init__(self, type_: str, nom: str, age: str) -> None:
        self.__type_ = type_
        self.__nom = nom
        self.__age = age

    def get_type(self):
        return self.__type_

    def set_type(self, type_):
        if not type_.isalpha():
            print("Некорректно!")
        else:
            self.__type_ = type_

    def get_nom(self):
        return self.__nom.title()

    def set_nom(self, nom):
        if not nom.isalpha():
            print("Некорректно!")
        else:
            self.__nom = nom

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if not age.isdigit():
            print("Некорректно!")
        else:
            self.__age = age
