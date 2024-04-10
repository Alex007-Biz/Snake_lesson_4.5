# Kanban доска для работы над проектом игры:
#
# Backlog:
# - Создать класс Hero
# - Создать метод attack() для класса Hero
# - Создать метод is_alive() для класса Hero
# - Создать класс Game
# - Создать метод start() для класса Game
#
# In Progress:
# - Написать код для класса Hero
# - Написать код для метода attack() класса Hero
# - Написать код для метода is_alive() класса Hero
# - Написать код для класса Game
# - Написать код для метода start() класса Game
#
# Testing:
# - Провести тестирование классов Hero и Game
# - Исправить ошибки, если такие есть
#
# Done:
# - Игра готова к использованию

import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= (self.attack_power + random.randint(1,20))

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        self.player = Hero("Player")
        self.computer = Hero("Computer")

    def start(self):
        print("Да начнется битва!")
        while self.player.is_alive() and self.computer.is_alive():
            # Player's turn
            self.player.attack(self.computer)
            print(f"{self.player.name} attacks {self.computer.name}. {self.computer.name}'s health: {self.computer.health}")
            if not self.computer.is_alive():
                break

            # Computer's turn
            self.computer.attack(self.player)
            print(f"{self.computer.name} attacks {self.player.name}. {self.player.name}'s health: {self.player.health}")

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

# Создаем игру и запускаем ее
game = Game()
game.start()