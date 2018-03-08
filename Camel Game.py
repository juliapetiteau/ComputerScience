# CAMEL GAME
import random

print("Welcome to the Camel Game")
print("You have stolen a camel in order to cross the Mobi desert.")
print("The natives want their camel back and are hunting you down")
print("Survive your desert trek and outrun the natives.")
print(" ")
miles_travelled = 0
thirst = 0
camel_tired = 0
natives = -20
canteen = 4

while True:
    print(" A. Drink from your canteen")
    print(" B.  Ahead moderate speed.")
    print(" C. Ahead full speed.")
    print(" D. Stop for the night.")
    print(" E. Status check.")
    print(" Q. Quit.")
    print(" ")

    answer = input("What would you like to do? ")
    if answer == "Q" or answer == "q":
        break
    elif answer == "E" or answer == "e":
        print('miles travelled = ', miles_travelled)
        print('thirst =' thirst)
        print('camel tiredness levels =', camel_tired)
        print('Natives are', natives, 'miles behind you')
        print('Drinks in canteen = ', canteen)
    
    elif answer == "d" or answer == "D":
        camel_tired = 0
        natives = natives + random.randint(7,15)
        print("Your camel tiredness level is 0. It is happy !")
        print("The natives are %s miles behind you" %(natives))
        print("You have travelled %s miles" %(miles_travelled))

    elif answer == "c" or answer == "C":
        miles_travelled = miles_travelled + random.randint(20, 36)
        camel_tired = camel_tired + random.randint(1, 4)
        natives = natives + random.randint(7,15)
        thirst = thirst + 2
        print("The natives are %s miles behind you" %(natives))
        print("You have travelled %s miles" %(miles_travelled))

    elif answer == "B" or answer == "b":
        miles_travelled = miles_travelled + random.randint(10, 26)
        camel_tired = camel_tired + random.randint(1, 3)
        natives = natives + random.randint(7,15)
        thirst = thirst + 1
        print("The natives are %s miles behind you" %(natives))
        print("You have travelled %s miles" %(miles_travelled))

    elif answer == "a"
