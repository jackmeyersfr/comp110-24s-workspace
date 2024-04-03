"""EX02 - One Shot Battleship - A not-so-cute step toward Battleship."""

__author__: str = "730646830"
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

enter_row: str = input("Guess a row: ")
row_picked: int = int(enter_row)

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

while row_picked > grid_size or row_picked < 1:
    new_row: str = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    new_row_picked: int = int(new_row)
    row_picked = new_row_picked

enter_column: str = input("Guess a column: ")
column_picked: int = int(enter_column)

while column_picked > grid_size or column_picked < 1: 
    new_column: str = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    new_column_picked: int = int(new_column)
    column_picked = new_column_picked

right_choice: str = RED_BOX
row_counter: int = 1

if row_picked == secret_row and column_picked == secret_column:
    right_choice = RED_BOX
else:
    right_choice = WHITE_BOX

while row_counter <= grid_size:
    emoji_row: str = ""
    column_counter: int = 1
    if row_picked == row_counter:
        while column_counter <= grid_size:    
            if column_picked == column_counter:
                emoji_row = emoji_row + right_choice
            else:
                emoji_row = emoji_row + BLUE_BOX
            column_counter += 1
    else:
        while column_counter <= grid_size:
            emoji_row = emoji_row + BLUE_BOX
            column_counter += 1
    print(emoji_row)
    row_counter += 1

if row_picked == secret_row and column_picked == secret_column: 
    print("Hit!")
else: 
    print("Miss!")

if row_picked == secret_row and column_picked != 2:
    print("Close! Correct row, wrong column.")
if row_picked != 3 and column_picked == secret_column:
    print("Close! Correct column, wrong row.")
