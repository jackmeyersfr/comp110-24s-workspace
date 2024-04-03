"""Humber Guessing Game"""
from random import randint

SECRET: int = randint(1,5)
correct: bool = False

while not correct: #correct == False
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"Correct! {guess} is the number!")
        exit()
        # something to help us exit
    elif guess > SECRET: 
        print("Guess again!")
        print("Too high!")
    else: 
        print("Too low!")
