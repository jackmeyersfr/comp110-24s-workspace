"""EX05 - What is battleship? - A small step for man away from Battleship."""

__author__: str = "730646830"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values in dictionaries."""
    new_dict: dict[str, str] = {}
    for item in dictionary:
        if dictionary[item] in new_dict:
            raise KeyError("Repetition of key values!")
        new_dict[dictionary[item]] = item
    return new_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns color that appears most frequently."""
    new_dict: dict[str, int] = {}
    for key in dictionary:
        color = dictionary[key]
        if color not in new_dict:
            new_dict[color] = 1
        else:
            new_dict[color] += 1
    max_fav: int = 0
    max_value: str = ""
    for key in new_dict:
        value = new_dict[key]
        if value > max_fav:
            max_fav = value
            max_value = key
    return max_value


def count(list: list[str]) -> dict[str, int]:
    """Counts the number of key appearances."""
    new_dict: dict[str, int] = {}
    for item in list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Sorts words under their first letters."""
    new_dict: dict[str, list[str]] = {}
    for elem in list1:
        letter: str = elem[0].lower()
        if letter in new_dict:
            new_dict[letter].append(elem)
        else:
            new_dict[letter] = [elem]
    return new_dict


def update_attendance(new_dict: dict[str, list[str]], dow: str, student: str) -> None:
    """Mutate and return that string."""
    if dow in new_dict and student not in new_dict[dow]:
        new_dict[dow].append(student)
    else:
        new_dict[dow] = [student]
    return None
