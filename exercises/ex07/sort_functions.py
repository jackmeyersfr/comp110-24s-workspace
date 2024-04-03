"""Functions that implement sorting algorithms."""

__author__ = "730646830"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    length: int = len(x)
    for i in range(1, length):
        current_elem = x[i]
        unsort_idx: int = i
        sorted_idx: int = i - 1
        while x[sorted_idx] > current_elem and sorted_idx >= 0:
            x[unsort_idx] = x[sorted_idx]
            unsort_idx -= 1
            sorted_idx -= 1
        x[unsort_idx] = current_elem
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    length: int = len(x)
    for i in range(0, length):
        min_idx = i
        for new_min in range(i+1, len(x)):
            if x[new_min] < x[min_idx]:
                min_idx = new_min
        if min_idx != i:
            spot = x[i]
            x[i] = x[min_idx]
            x[min_idx] = spot
    return None