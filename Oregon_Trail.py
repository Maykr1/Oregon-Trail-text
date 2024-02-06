import random
from scenarios import *

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def gainHealth(self, health):
        self.health += health

    def loseHealth(self, health):
        self.health -= health

def startGame():
    print("You set out on March 20th, 1857 on the Oregon Trail. Your destination is Oregon City. Your characters {} and {} must survive the grueling path.".format(char1.name, char2.name))
    while char1.health > 0 and char2.health > 0:
        #ranNum = random.randint(1, 10)
        ranNum = 1
        if ranNum == 1:
            scenario1()

if __name__ == '__main__':
    menu = input("""Hello and Welcome to the Oregon Trail Game!
    Please input a command:
                 
    1. Start Game
    2. Quit Game
        
    """)
    
    if menu == '1':
        name = input("What is the name of your first character? ")
        char1 = Character(name, 100)
        name = input("What is the name of your second character? ")
        char2 = Character(name, 100)
        startGame()
    elif menu == '2':
        exit()
    else:
        print("Invalid Command!")