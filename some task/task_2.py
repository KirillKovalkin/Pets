# Задача 2. Необходимо создать класс Animal, который имеет атрибуты Name (тип животного), Color (его расцветку) и Voice (издаваемый звук).
# Написать функцию, которая возвращает строку вида «It says <Voice>.», где <Voice> является уникальным атрибутом класса Animal.
# Задать три экземпляра класса Cow, Cat, Dog с уникальными атрибутами для каждого.
# Для каждого экземпляра вывести строку вида «<Name> is <Color>. It says <Voice>.»


class Animal:
    """Описание класса Animal"""

    def __init__(self, name, color, voice):
        """Свойства класса Animal"""
        self.name = name
        self.color = color
        self.voice = voice

    def animal_properties(self):
        """Метод вывыодит свойства животного"""
        return f'"{self.name} is {self.color}. It says {self.voice}"'


cow = Animal("Cow", "Brown", "Moooo")
cat = Animal("Cat", "White", "Meoow")
dog = Animal("Dog", "Black", "Woof-Woof")


print(cow.animal_properties())
print(cat.animal_properties())
print(dog.animal_properties())
