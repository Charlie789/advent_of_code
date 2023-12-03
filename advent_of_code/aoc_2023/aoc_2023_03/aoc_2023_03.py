import math
from collections import namedtuple
from itertools import product
from pathlib import Path

Point = namedtuple("Point", "x y")
PosNumber = namedtuple("PosNumber", "value, start_pos")

def extract_numbers_and_symbols(line: str, row_nb: int, valid_symbols: list[str] = None):
    def _finalize_number():
        nonlocal current_number
        nonlocal current_number_pos
        number = PosNumber(current_number, current_number_pos)
        numbers.append(number)
        current_number = None
        current_number_pos = None

    def _init_new_number(first_digit, x, y):
        nonlocal current_number
        nonlocal current_number_pos
        current_number = first_digit
        current_number_pos = Point(x, y)

    def _extend_current_number(next_digit):
        nonlocal current_number
        current_number += next_digit

    def _add_symbol(x, y):
        symbols.append(Point(x, y))

    numbers = []
    symbols = []
    current_number = None
    current_number_pos = None

    for i, char in enumerate(line):
        if char.isdigit():
            if current_number is None and current_number_pos is None:
                _init_new_number(char, row_nb, i)
            else:
                _extend_current_number(char)
        else:
            if current_number is not None and current_number_pos is not None:
                _finalize_number()
            if char != ".":
                if valid_symbols:
                    if char in valid_symbols:
                        _add_symbol(row_nb, i)
                else:
                    _add_symbol(row_nb, i)
    if current_number is not None and current_number_pos is not None:
        _finalize_number()
    return numbers, symbols


def check_if_number_has_symbol_neighbour(number: PosNumber, symbols: list[Point]):
    def _generate_possible_neighbour_for_point(point: Point):
        return map(lambda coords: Point(point.x + coords[0], point.y + coords[1]), product([-1, 0, 1], [-1, 0, 1]))

    def _check_if_point_has_symbol_neighbour(point: Point, symbols: list[Point]):
        possible_neighbours = _generate_possible_neighbour_for_point(point)
        for poss_neigh in possible_neighbours:
            if poss_neigh in symbols:
                return True
        return False

    for i, digit in enumerate(number.value):
        point = Point(number.start_pos.x, number.start_pos.y + i)
        if _check_if_point_has_symbol_neighbour(point, symbols):
            return True
    return False


def get_number_neighbour_symbol(number: PosNumber, symbols: list[Point]):
    def _generate_possible_neighbour_for_point(point: Point):
        return map(lambda coords: Point(point.x + coords[0], point.y + coords[1]), product([-1, 0, 1], [-1, 0, 1]))

    def _get_point_neighbour_symbol(point: Point, symbols: list[Point]):
        possible_neighbours = _generate_possible_neighbour_for_point(point)
        for poss_neigh in possible_neighbours:
            if poss_neigh in symbols:
                return poss_neigh
        return None

    for i, digit in enumerate(number.value):
        point = Point(number.start_pos.x, number.start_pos.y + i)
        if neighbour := _get_point_neighbour_symbol(point, symbols):
            return neighbour
    return None

def parse(raw_input):
    parsed_input = raw_input.splitlines()
    return parsed_input


def task1(parsed_input):
    engine = {
        "numbers": [],
        "symbols": [],
    }
    for line_nb, line in enumerate(parsed_input):
        numbers, symbols = extract_numbers_and_symbols(line, line_nb)
        engine["numbers"].extend(numbers)
        engine["symbols"].extend(symbols)
    valid_numbers = filter(lambda number: check_if_number_has_symbol_neighbour(number, engine["symbols"]), engine["numbers"])
    return sum(map(lambda number: int(number.value), valid_numbers))


def task2(parsed_input):
    engine = {
        "numbers": [],
        "symbols": [],
    }
    symbol_neighbours = {}

    for line_nb, line in enumerate(parsed_input):
        numbers, symbols = extract_numbers_and_symbols(line, line_nb, ["*"])
        engine["numbers"].extend(numbers)
        engine["symbols"].extend(symbols)

    for number in engine["numbers"]:
        if symbol := get_number_neighbour_symbol(number, engine["symbols"]):
            if symbol not in symbol_neighbours:
                symbol_neighbours[symbol] = [number]
            else:
                symbol_neighbours[symbol].append(number)

    total_ratio = 0

    for numbers in symbol_neighbours.values():
        if len(numbers) <= 1:
            continue
        gear_ratio = math.prod(map(lambda number: int(number.value), numbers))
        total_ratio += gear_ratio

    return total_ratio

if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().strip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
