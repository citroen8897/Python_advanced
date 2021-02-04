import animaux

current_animal = animaux.Animal('xxx', 'yyy', '0')

current_animal.nom_de_animal = input('Имя: ')
while current_animal.nom_de_animal == 'не задано':
    current_animal.nom_de_animal = input('Имя: ')

current_animal.__setattr__('type_', input('Вид: '))
while current_animal.type_ == 'не задано':
    current_animal.__setattr__('type_', input('Вид: '))

current_animal.__setattr__('age', input('Возраст: '))
while current_animal.age == 'не задано':
    current_animal.__setattr__('age', input('Возраст: '))

current_animal.__str__()
