#Hogwarts
#Program asks for a name and assigns that person to one of the four harry potter houses

#Init
import time
import random

#Func
def main():
    print("Welcome To Hogwarts")
    name = input("What is your name:")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print("......")
    print(house(name)) #house(name) will return one of the four houses

def house(name):
    if name == "Harry" or name == "Ron" or name == "Hermione":
        return ("Gryffindor")
    elif name == "Newt" or name == "Nymphadora" or name == "Pomona":
        return ("Hufflepuff")
    elif name == "Luna" or name == "Cho" or name == "Filius":
        return ("Ravenclaw")
    elif name == "Voldemort" or name == "Draco" or name == "Severus ":
        return ("Slytherin")
    else:
        num = random. randint(1,4)
        if num == (1):
            return ("Gryffindor")
        elif num == (2):
            return ("Hufflepuff")
        elif num == (3):
            return ("Ravenclaw")
        else:
            return ("Slytherin")

#Main
main()
