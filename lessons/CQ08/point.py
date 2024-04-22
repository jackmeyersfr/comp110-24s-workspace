"""CQ08."""

from __future__ import annotations


class Point: 
    """Class for Point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Initial function."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scales the x and y values by a factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Scales the x and y values by a factor with a new point."""
        new_x: float = self.x * factor
        new_y: float = self.y * factor
        return Point(new_x, new_y)
        