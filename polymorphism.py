class Animal:
    def sound(self):
        print("Animal SOund")
class Dog(Animal):
    def sound(self):
        print('Gheu Gheu')
class Cat(Animal):
    def sound(self):
        print('Miyau miyau')

animals =[Dog(),Cat()]

for animal in animals:
    print(animal.sound())