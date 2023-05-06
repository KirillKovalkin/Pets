# Задача 2. Необходимо создать класс Animal, который имеет атрибуты Name (тип животного), Color (его расцветку) и Voice (издаваемый звук).
# Написать функцию, которая возвращает строку вида «It says <Voice>.», где <Voice> является уникальным атрибутом класса Animal.
# Задать три экземпляра класса Cow, Cat, Dog с уникальными атрибутами для каждого.
# Для каждого экземпляра вывести строку вида «<Name> is <Color>. It says <Voice>.»

# class Animal():
#     """Описание класса Animal"""
#     def __init__(self, name, color, voice):
#         """Свойства класса Animal"""
#         self.name = name
#         self.color = color
#         self.voice = voice
#
#     def animal_properties(self):
#         """Метод вывыодит свойства животного"""
#         print('"' + self.name + " is " + self.color + ". It's says " + self.voice + '"')
#
# Animal1 = Animal('Cow', 'Brown', 'Moooo')
# Animal2 = Animal('Cat', 'White', 'Meoow')
# Animal3 = Animal('Dog', 'Black', 'Woof-Woof')
#
#
#
# Animal1.animal_properties()
# Animal2.animal_properties()
# Animal3.animal_properties()

class Animal():
    """Описание класса Animal"""
    def __init__(self, name, color, voice):
        """Свойства класса Animal"""
        self.name = name
        self.color = color
        self.voice = voice

        if name == "Dog":
            self.voice = " It's says Woof-Woof"
        elif name == "Cat":
            self.voice = " It's says Meoow"
        elif name == "Cow":
            self.voice = " It's says Moooo"
        else:
            self.voice = " I don't know the voice of this animal"

    def animal_properties(self):
        """"Метод вывыодит свойства животного"""
        print('"' + self.name + " is " + self.color + "." + self.voice + '"')


Animal1 = Animal('Cow', 'Brown', 'Moooo')
Animal2 = Animal('Cat', 'White', 'Meoow')
Animal3 = Animal('Dog', 'Black', 'Woof-Woof')

Animal1.animal_properties()
Animal2.animal_properties()
Animal3.animal_properties()
