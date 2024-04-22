"""Checking CQ08."""

from lessons.CQ08.point import Point

mutate_point: Point = Point(3.0, 5.0)
new_point: Point = Point(3.0, 5.0)

print(mutate_point.scale_by(3))
print(new_point.scale(2))
