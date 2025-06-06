import random
import time

# Game Rules
print("=== Welcome to the Number Guessing Game ===")
print("Rules:")
print("1. The system will randomly choose a number between 1 and 100.")
print("2. Your job is to guess the correct number.")
print("3. After each guess, you'll get a hint whether your guess was too high or too low.")
print("4. Type 'Q' to quit the game anytime.\n")

time.sleep(10)

target = random.randint(1,100)

while True:
    userChoice = input("Guess the target or Quit(Q) : ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        print()
        break
    elif(userChoice < target):
        print("Your number was too small. Take a Bigger Guess..")
        print()
    else:
        print("Your Number was too big. Take a Smaller Guess..")
        print()

print("---GAME OVER---")