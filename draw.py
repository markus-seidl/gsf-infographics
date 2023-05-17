import math
from domain import Point, BlockDescription
import svg
import copy
import constants
import locale

CO2_SIZE = Point(10, 10)
CO2_SPACING_1 = Point(3, 3)
CO2_SPACING_2 = Point(5, 5)


# https://developer.mozilla.org/en-US/docs/Web/SVG

def draw_co2_block(position: Point, count: Point, description: BlockDescription) -> []:
    print(f"Drawing block " + description.display_text.replace('\n', ' '))
    co2_pos = copy.copy(position)
    total = description.total

    drawn_boxes = 0
    max_bottom_right = copy.copy(co2_pos)
    ret = []
    for x in range(0, count.x):
        for y in range(0, count.y):
            co2_pos.y += CO2_SPACING_2.y if y % 6 == 5 else CO2_SPACING_1.y

            if drawn_boxes >= total:
                break

            ret += draw_co2_single(co2_pos)
            drawn_boxes += 1
            co2_pos.y += CO2_SIZE.y
            max_bottom_right = copy.copy(co2_pos) + CO2_SIZE

        co2_pos.x += CO2_SIZE.x + (CO2_SPACING_2.x if x % 6 == 5 else CO2_SPACING_1.x)
        co2_pos.y = position.y

        if drawn_boxes >= total:
            break

    if drawn_boxes != total:
        raise ValueError(f"drawn_boxes ({drawn_boxes}) != total ({total})")

    text_element = position_text(svg.Text(), position, max_bottom_right, description)
    display_text = description.display_text + "\n" + format_total(description.total, description.unit)
    text_element.text = format_text(display_text, text_element.x)
    position_text_pass_2(text_element, position, max_bottom_right, description)

    return [svg.G(elements=[
        svg.G(elements=ret),
        text_element,
    ])]


def format_total(total: int, unit: str) -> str:
    # https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
    # https://stackoverflow.com/questions/17484631/format-string-spaces-between-every-three-digit
    total_str = "{:,}".format(int(total)).replace(',',' ')
    unit_str = unit

    return f"""<tspan class="bold">{total_str} {unit_str}</tspan>"""


def format_text(text: str, x_pos: int) -> str:
    # https://stackoverflow.com/questions/16701522/how-to-linebreak-an-svg-text-within-javascript
    temp = text.split("\n")
    temp = [x.strip() for x in temp]
    temp = [x for x in temp if x != ""]

    ret = ""
    for line in temp:
        ret += f"""<tspan x="{x_pos}" dy="1.2em">{line}</tspan>\n"""
    return ret


def position_text(
        text_element: svg.Text, start_pos: Point, max_bottom_right: Point,
        description: BlockDescription
) -> svg.Text:
    if description.text_compass == "east":
        y = start_pos.y + (max_bottom_right.y - start_pos.y) / 2
        text_element.x = max_bottom_right.x + description.text_offset.x
        text_element.y = y + description.text_offset.y
    elif description.text_compass == "west":
        text_element.text_anchor = "end"
        y = start_pos.y + (max_bottom_right.y - start_pos.y) / 2
        text_element.x = start_pos.x + description.text_offset.x
        text_element.y = y + description.text_offset.y

    return text_element


def position_text_pass_2(
        text_element: svg.Text, start_pos: Point, max_bottom_right: Point,
        description: BlockDescription
) -> svg.Text:
    lines = len(text_element.text.split("\n")) - 1
    if description.text_compass in ["east", "west"]:
        # try to center vertically on the right side of the block
        text_element.y -= lines / 2.0 * constants.LINE_HEIGHT

    return text_element


def draw_co2_single(position: Point = None) -> []:
    return [svg.Rect(
        x=position.x,
        y=position.y,
        width=CO2_SIZE.x,
        height=CO2_SIZE.y,
        fill="rgb(159, 196, 66)",
    )]
