import math
import copy
from collections import namedtuple

import cairo

Point = namedtuple('Point', 'x y')

WIDTH, HEIGHT = 1024, 1024
CO2_SIZE = Point(10, 10)
CO2_SPACING_1 = Point(3, 3)
CO2_SPACING_2 = Point(0, 0)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )


# https://pycairo.readthedocs.io/en/latest/reference/index.html

def draw_co2_block(c: cairo.Context, position: Point, count: Point):
    co2_pos = copy.copy(position)

    for x in range(0, count.x):
        for y in range(0, count.y):
            if y % 6 == 5:
                co2_pos.y += CO2_SPACING_2.y
            else:
                co2_pos.y += CO2_SPACING_1.y

            draw_co2_single(c, co2_pos)
            co2_pos.y += CO2_SIZE.y

        if x % 6 == 5:
            co2_pos.x += CO2_SPACING_2.x
        else:
            co2_pos.x += CO2_SPACING_1.x
        co2_pos.x += CO2_SIZE.x
        co2_pos.y = position.y


def draw_co2_single(c: cairo.Context, coords: Point = None):
    if coords is None:
        coords = Point(0, 0)

    c.set_source_rgb(0.0, 0.8, 0.1)  # Solid color

    c.set_line_width(2)
    c.rectangle(coords.x, coords.y, CO2_SIZE.x, CO2_SIZE.y)
    c.fill_preserve()
    c.stroke()


if __name__ == "__main__":
    # surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    surface = cairo.SVGSurface("example.svg", WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    draw_co2_block(ctx, Point(0, 0), Point(10, 5))

# pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
# pat.add_color_stop_rgba(1, 0.7, 0, 0, 0.5)  # First stop, 50% opacity
# pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity
#
# ctx.rectangle(0, 0, 1, 1)  # Rectangle(x0, y0, x1, y1)
# ctx.set_source(pat)
# ctx.fill()
#
# ctx.translate(0.1, 0.1)  # Changing the current transformation matrix
#
# ctx.move_to(0, 0)
# # Arc(cx, cy, radius, start_angle, stop_angle)
# ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
# ctx.line_to(0.5, 0.1)  # Line to (x,y)
# # Curve(x1, y1, x2, y2, x3, y3)
# ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
# ctx.close_path()
#
# ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
# ctx.set_line_width(0.02)
# ctx.stroke()
#
# surface.write_to_png("example.png")  # Output to PNG
