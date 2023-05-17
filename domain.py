from dataclasses import dataclass, field


class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )


@dataclass
class BlockDescription:
    unit: str = "g"
    total: int = 0
    display_text: str = ""
    """Total amount of boxes to draw (= CO2 boxes). Raises an error if boxes are left over after count(x,y) is reached.
    """
    text_offset: str = field(default_factory=lambda: Point(-5, 0))
    text_compass: str = "west"
    """
        North
    West    East
        South
    """
