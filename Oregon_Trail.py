class Character:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health
    
    def gainHealth(self, health):
        self.health += health

    def loseHealth(self, health):
        self.health -= health

def createCharacterMenu():
    name = input("What is the name of your first character?")
    char1 = Character(name, 40, 100)
    name = input("What is the name of your second character?")
    char2 = Character(name, 35, 100)

if __name__ == '__main__':
    menu = input("""Hello and Welcome to the Oregon Trail Game!
    Please input a command:
                 
    1. Start Game
    2. Quit Game
        
        """)
    
    if menu == '1':
        createCharacterMenu()
    elif menu == '2':
        exit()
    else:
        print("Invalid Command!")