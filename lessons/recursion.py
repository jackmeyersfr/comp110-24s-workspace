"""CQ 05."""

__author__: str = '730646830'


def f(n: int, k: int) -> int:
    """Multiplying n by k."""
    if n == 0:
        return 0
    else: 
        if n == 1:
            return k
        else:
            return f(n - 1, k) + k