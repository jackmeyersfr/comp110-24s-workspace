"""EX03 - Functional Battleship - A really-not-cute step toward Battleship."""

__author__: str = "730646830"
import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(num_guess: int, column_or_row: str) -> int:
    """Returns guesses of battleship location."""
    assert column_or_row == "row" or column_or_row == "column"
    enter_row_column: str = input(f"Guess a {column_or_row}: ")
    choice_picked: int = int(enter_row_column)

    while choice_picked > num_guess or choice_picked < 1:
        new_row: str = input(f"The grid is only {num_guess} by {num_guess}. Try again: ")
        new_row_picked: int = int(new_row)
        choice_picked = new_row_picked
    return choice_picked


def print_grid(size_of_grid: int, row_guess: int, column_guess: int, correctness: bool) -> None:
    """Prints the Battleship Grid."""
    right_choice: str = RED_BOX
    row_counter: int = 1
    if correctness is True:
        right_choice = RED_BOX
    else:
        right_choice = WHITE_BOX
    
    while row_counter <= size_of_grid:
        emoji_row: str = ""
        column_counter: int = 1
        if row_guess == row_counter:
            while column_counter <= size_of_grid:    
                if column_guess == column_counter:
                    emoji_row = emoji_row + right_choice
                else:
                    emoji_row = emoji_row + BLUE_BOX
                column_counter += 1
        else:
            while column_counter <= size_of_grid:
                emoji_row = emoji_row + BLUE_BOX
                column_counter += 1
        print(emoji_row)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Correct guess of the program."""
    if secret_row == row_guess and secret_column == column_guess:
        answer: bool = True
    else: 
        answer = False
    return answer


def main(grid_size: int, secret_row: int, secret_column: int) -> None: 
    """Main function of the program."""
    total_turns: int = 5
    turn_count: int = 1
    victory: bool = False
    while turn_count <= total_turns and victory is False: 
        print(f"=== Turn {turn_count}/5 ===")
        row_pick: int = input_guess(grid_size, "row")
        column_pick: int = input_guess(grid_size, "column")
        corrected: bool = correct_guess(secret_row, secret_column, row_pick, column_pick)
        print_grid(grid_size, row_pick, column_pick, corrected)
        if corrected is True:
            print("Hit!")
            print(f"You won in {turn_count}/5 turns!")
            victory = True
        else: 
            print("Miss!")
        turn_count += 1
    if turn_count > total_turns: 
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))