import math
import copy
from collections import namedtuple
from domain import Point, BlockDescription
from draw import *
import svg
from textwrap import dedent
import constants

WIDTH, HEIGHT = 1024, 1024


def generate_styles() -> []:
    return [svg.Style(
        text=dedent("""
        text {
            font-size: """ + str(constants.FONT_SIZE) + """
            
        }
        .bold {
            font-weight: bold;
        }
        """)
    )]


def generate_one_g_co2() -> []:
    return [
        # 6g in carbonated drinks
        draw_co2_block(Point(100, 0), Point(1, 6), BlockDescription(
            total=6,
            display_text=dedent("""1 carbonated drink""")
        )),
        # 1 toy balloon filled with exhaled air
        draw_co2_block(Point(250, 0), Point(5, 10), BlockDescription(
            total=49,
            display_text=dedent("""
            1 toy balloon filled
            with exhaled air
            """)
        )),
        draw_co2_block(Point(100, 150), Point(1, 6), BlockDescription(
            total=6,
            display_text=dedent("""1 dice of dry ice""")
        )),
    ]


def generate_one_kg_co2() -> []:
    return [
        # 6g in carbonated drinks
        draw_co2_block(Point(100, 0), Point(2, 6), BlockDescription(
            total=10,
            display_text=dedent("""100km in a car"""),
            unit="kg"
        )),
        draw_co2_block(Point(100, 100), Point(2, 3), BlockDescription(
            total=6,
            display_text=dedent("""1 cow per day"""),
            unit="kg"
        )),
    ]


def metric_group(translate: Point, elements: []) -> []:
    return [svg.G(
        elements=elements,
        transform=[svg.Translate(translate.x, translate.y)],
    )]


if __name__ == "__main__":
    elements = generate_styles() + metric_group(
        # 1g of CO2
        Point(0, 0), generate_one_g_co2()
    ) + metric_group(
        # 1kg of CO2
        Point(10, 300), generate_one_kg_co2()
    )

    picture = svg.SVG(
        viewBox=svg.ViewBoxSpec(0, 0, WIDTH, HEIGHT),
        width=WIDTH,
        height=HEIGHT,
        elements=elements,
    )

    with open("example.svg", "w") as f:
        f.write(str(picture))
