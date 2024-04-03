"""Mutating functions."""

__author__ = "730646830"


def manual_append(word: list[int], num: int) -> None:
    """Adding numbers."""
    word.append(num)


def double(wurd: list[int]) -> None:
    """Doubles each element of function."""
    counter: int = 0
    while counter < len(wurd):
        wurd[counter] = wurd[counter] * 2
        counter += 1
