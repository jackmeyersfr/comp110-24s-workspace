"""Splitting a dictionary into two lists."""

__author__: str = "730646830"


def get_keys(dictionary: dict[str, int]) -> list[str]:
    """List of all keys in dictionary."""
    keys: list[str] = []
    for item in dictionary:
        keys.append(item)
    return keys


def get_values(dictionary: dict[str, int]) -> list[int]:
    """List of all values in dictionary."""
    values: list[int] = []
    for item in dictionary:
        values.append(dictionary[item])
    return values