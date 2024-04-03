"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730646830"

##enter_number: str = input("Pick a secret boat location between 1 and 4:")
##number_picked: int = int(enter_number)

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


if number_picked >= 5:
    print("Error! " + str(number_picked) + " too high!")
    exit()
if number_picked < 1:
    print("Error! " + str(number_picked) + " too low!")
    exit()

p2_guess: str = input("Guess a number between 1 and 4:")
p2_number: int = int(p2_guess)

if p2_number >= 5:
    print("Error! " + str(p2_number) + " too high!")
    exit()
if p2_number < 1:
    print("Error! " + str(p2_number) + " too low!")
    exit()

right_choice: str = ""
if p2_number == 1:
    if p2_number == number_picked:
        right_choice = RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX
    else:
        right_choice = WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX

if p2_number == 2:
    if number_picked == p2_number:
        right_choice = BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX
    else:
        right_choice = BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX

if p2_number == 3:
    if number_picked == p2_number:
        right_choice = BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX
    else:
        right_choice = BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX

if p2_number == 4: 
    if number_picked == p2_number:
        right_choice = BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX
    else:
        right_choice = BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX

print(right_choice)

if number_picked == p2_number:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")
