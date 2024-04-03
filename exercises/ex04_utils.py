"""EX04 - We Ditched Battleship - A cute step away from Battleship."""


def all(listed: list[int], given_int: int) -> bool:
    """The Honey-do List."""
    idx_counter: int = 0
    the_bool: bool = True
    while idx_counter < len(listed):
        if listed[idx_counter] == given_int:
            the_bool = True
        else: 
            the_bool = False
            return the_bool
        idx_counter += 1
    if len(listed) == 0:
        return False
    return the_bool


def max(max_list: list[int]) -> int:
    """MAX POWER."""
    idx_counter: int = 0
    current_max: int = -1000
    while idx_counter < len(max_list):
        if max_list[idx_counter] > current_max:
            current_max = max_list[idx_counter]
        idx_counter += 1
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
        exit()
    return current_max


def is_equal(one_list: list[int], two_list: list[int]) -> bool:
    """Red list blue list."""
    idx_counter: int = 0
    the_bool: bool = True
    if len(one_list) != len(two_list):
        the_bool = False
        return the_bool
    while idx_counter < len(one_list):
        if one_list[idx_counter] == two_list[idx_counter]:
            the_bool = True
        else: 
            the_bool = False
            return the_bool
        idx_counter += 1
    return the_bool


def extend(da_list: list[int], de_list: list[int]) -> None:
    """Extending those numbers."""
    idx_counter: int = 0
    while idx_counter < len(de_list):
        num: int = de_list[idx_counter]
        da_list.append(num)
        idx_counter += 1