import math
from pathlib import Path

max_values = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def parse_game(game):
    game, reveals = game.split(":")
    game_id = int(game[5:])
    sets = reveals.split(";")
    maxes = {}
    for set_ in sets:
        color_qubes = set_.split(",")
        for single_color in color_qubes:
            quantity, color = single_color.split()
            maxes[color] = max(int(quantity), maxes.get(color, 0))

    return game_id, maxes


def parse(raw_input):
    parsed_input = raw_input.splitlines()
    return parsed_input


def task1(parsed_input):
    sum_ = 0
    for line in parsed_input:
        game_id, maxes = parse_game(line)
        is_game_valid = True
        for k, v in maxes.items():
            if v > max_values[k]:
                is_game_valid = False
        if is_game_valid:
            sum_ += game_id
    return sum_


def task2(parsed_input):
    sum_ = 0
    for line in parsed_input:
        _, maxes = parse_game(line)
        power = math.prod(maxes.values())
        sum_ += power
    return sum_


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().strip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
