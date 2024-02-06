import random

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def gainHealth(self, health):
        self.health += health

def startGame():
    print("You set out on March 20th, 1857 on the Oregon Trail. Your destination is Oregon City. Your characters {} and {} must survive the grueling path.".format(char1.name, char2.name))
    
    while char1.health > 0 and char2.health > 0:
        print("{}'s health is {} and {}'s is {}".format(char1.name, char1.health, char2.name, char2.health))
        direction = input("You are face with three paths, left, right, and forward. Which way do you go? (Say q to quit)")
        if direction.lower() == 'left':
            print("{} was bitten by a snake!".format(char1.name))
            char1.health -= random.randint(1, 25)
        elif direction.lower() == 'right':
            print("{} was hit by a rock!".format(char2.name))
            char2.health -= random.randint(1, 25)
        elif direction.lower() == 'forward':
            heal = input("You have found a health potion. Will you heal {} or {}? ".format(char1.name, char2.name))
            if heal.lower() == char1.name.lower():
                num = random.randint(0, 10)
                char1.gainHealth(num)
                print('{} was healed by {} points'.format(char1.name, num))
            elif heal.lower() == char2.name.lower():
                num = random.randint(0, 10)
                char2.gainHealth(num)
                print('{} was healed by {} points'.format(char2.name, num))
            else:
                print("You dropped the health potion! Time to move on!")
        else:
            exit()


    if not char1.health > 0 or not char2.health > 0:
        print("Oh no, someone died :(")

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