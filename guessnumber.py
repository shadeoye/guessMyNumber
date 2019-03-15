#import random
#choose random number for computer
#if answer is = computer, print you guessed right
#if else statement, if too high or low guess again

import random

computer = random.randint(1,10)

user = int(input("Guess what number i'm thinking of\n"))

for i in range(10):
    if user == computer:
        print("YOU GUESSED RIGHT!")
        print("The computer's number was " + str(computer))
        break
    elif user < computer:
        print("The number is too low")
        user = int(input("Please try again\n"))
    else:
        print("The number is too high")
        user = int(input("Please try again\n"))
