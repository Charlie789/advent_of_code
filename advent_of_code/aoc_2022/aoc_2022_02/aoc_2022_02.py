from pathlib import Path


SYMBOL_POINTS = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

OPPONENT_SYMBOL_POINTS = {
    "A": 1,
    "B": 2,
    "C": 0
}

WIN_POINT = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

LOGIC = {
    "A": {
        "X": "Z",
        "Y": "X",
        "Z": "Y"
    },
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z"
    },
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X"
    }
}


def parse(raw_input):
    parsed_input = raw_input.splitlines()
    return parsed_input


def task1(parsed_input):
    total_points = 0
    for round in parsed_input:
        mapped_round = _map_round(round)
        total_points += _count_points(mapped_round)
    return total_points


def task2(parsed_input):
    total_points = 0
    for round in parsed_input:
        bets = round.split(" ")
        total_points += WIN_POINT[bets[1]]
        bet_symbol = LOGIC[bets[0]][bets[1]]
        total_points += SYMBOL_POINTS[bet_symbol]
    return total_points


def _map_round(round):
    symbols = round.split(" ")
    mapped_symbols = (OPPONENT_SYMBOL_POINTS[symbols[0]], SYMBOL_POINTS[symbols[1]])
    return mapped_symbols


def _count_points(mapped_round):
    points = 0
    round_result = mapped_round[1] - mapped_round[0]
    if round_result == 1 :
        points += 6
    elif round_result == 0 or round_result == 3:
        points += 3

    points += mapped_round[1]
    return points

if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().strip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
