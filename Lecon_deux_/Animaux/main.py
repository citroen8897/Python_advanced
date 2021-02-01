import animaux


current_animal = animaux.Animal("", "", "")
current_nom = animaux.Animal.set_nom(current_animal, nom=input("Имя: "))
current_type = animaux.Animal.set_type(current_animal, type_=input("Вид: "))
current_age = animaux.Animal.set_age(current_animal, age=input("Возраст: "))

print(
    f"\nДанные животного:\nИмя: {current_animal.get_nom()}\n"
    f"Возраст: {current_animal.get_age()}\n"
    f"Вид: {current_animal.get_type()}"
)

current_animal.set_nom('Тришка')
print(current_animal.get_nom())
