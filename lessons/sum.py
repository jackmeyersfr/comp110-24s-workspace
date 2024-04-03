"""Summing the elements of a list using different loops."""

__author__: str = "730646830"


def w_sum(vals: list[float]) -> float:
    """While loop sum of numbers."""
    idx_counter: int = 0
    sum_num: float = 0
    while idx_counter < len(vals):
        sum_num += vals[idx_counter]
        idx_counter += 1
    return sum_num


def f_sum(vals: list[float]) -> float:
    """For loop sum of numbers."""
    sum_num: float = 0
    for item in vals:
        sum_num += item
    return sum_num


def f_range_sum(vals: list[float]) -> float:
    """For loop range sum of numbers."""
    sum_num: float = 0
    for item in range(0, len(vals)):
        sum_num += vals[item]
    return sum_num
