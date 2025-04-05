# a basic class 

# class TestClass:
# ## variables in class are attributes
# ## Functions in a class are methods


#     # test_var = "Hello"
# # self refers to any instance of the class and must ne the first parameter for all methods It allows you to target attributes everywhere within the class
#     def test_function(self):
#         print('This is called from test class')
#         self.another_function("Hi")
    
#     def another_function(self,test_param):
#         print(test_param)


# # create an instance
# test = TestClass()
# print(test.test_var)

# test2 = TestClass()
# test2.test_function()
# test2.another_function('Test')


# ## Dunder methods are special methods of a class __init__ is run when an instance of the class is created 
# # __len__ gets called when the instance is passed into the len function
# mage class

# class Mage:
#     def __init__(self,health,mana):
#         self.health = health
#         self.mana = mana

#         print('The mage class was created')
#         print(self.health)
#     def __len__(self):
#         return self.health
#     def attack(self,target):
#         target.health-=10


# class Monster:
#     health =40
# mage = Mage(100,200)
# print(len(mage))

# monster = Monster()

# print(monster.health)
# mage.attack(monster)
# print(monster.health)


# Inheritance

# With inheritance one class can get the methods and attributes of another class
# A class can also inherit from multiple classes and you can have entires family trees

# class Human:
#     def __init__(self,health):
#         self.health= health
#     def attack(self):
#         print('Attack')

# class Warrior(Human):
#     def __init__(self, health, defense):
#         super().__init__(health)
#         self.defense = defense
    
# class Barbarian(Human):
#     def __init__(self, health, defense):
#         super().__init__(health)
#         self.defense = defense

# warrior=Warrior(5.5,10)
# barbarian = Barbarian(100,8.1)
# warrior.attack()
# barbarian.attack()

class Entity:
    def attack(self):
        print(f'attack with {self.damage} damage')
class Monster(Entity):
    def __init__(self,health, damage):
        self.health= health
        self.damage = damage
    def __repr__(self):
        return f'a monster with {self.health} hp'
monster = Monster(100,10)
monster.attack()
print(monster)