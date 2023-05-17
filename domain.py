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

    def __str__(self):
        return f"({self.x}, {self.y})"


class Rect:
    def __init__(self, x=0, y=0, width=0, height=0):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def extend_point(self, p: Point):
        """Extend the rectangle to include the given point."""
        if p.x < self._x:
            self._width += self._x - p.x
            self._x = p.x
        elif p.x > self._x + self._width:
            self._width = p.x - (self._x + self._width)

        if p.y < self._y:
            self._height += self._y - p.y
            self._y = p.y
        elif p.y > self._y + self._height:
            self._height = p.y - (self._y + self._height)

    def extend_rect(self, r: Rect):
        """Extends the rectangle to include the given rectangle."""
        self.extend_point(Point(r.x, r.y))
        self.extend_point(Point(r.x + r.width, r.y + r.height))

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

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    def __str__(self):
        return f"({self.x}, {self.y}, {self.width}, {self.height})"


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
