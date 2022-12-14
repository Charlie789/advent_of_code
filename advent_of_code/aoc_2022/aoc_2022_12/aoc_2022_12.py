from pathlib import Path
from string import ascii_lowercase
import numpy as np
from collections import namedtuple


Map = namedtuple("Map", "map start finish")

def parse(raw_input):
    parsed_input = []
    start = None
    finish = None
    for i, line in enumerate(raw_input.splitlines()):
        parsed_line = []
        for j, char in enumerate(line):
            try:
                parsed_line.append(ascii_lowercase.index(char))
            except ValueError:
                if char == "S":
                    start = (i, j)
                    parsed_line.append(0)
                elif char == "E":
                    finish = (i, j)
                    parsed_line.append(ascii_lowercase.index("z"))
        parsed_input.append(parsed_line)
    _map = np.array(parsed_input)

    return Map(_map, start, finish)


def task1(parsed_input):

    def make_step(k):
        for i in range(len(_map)):
            for j in range(len(_map[0])):
                if map_of_movements[i, j] == k:
                    # UP
                    if i > 0 and map_of_movements[i - 1, j] == -1 and _map[i - 1, j] - _map[i, j] <= 1:
                        map_of_movements[i - 1, j] = k + 1
                    # LEFT
                    if j > 0 and map_of_movements[i, j - 1] == -1 and _map[i, j - 1] - _map[i, j] <= 1:
                        map_of_movements[i, j - 1] = k + 1
                    # DOWN
                    if i < len(_map) - 1 and map_of_movements[i + 1, j] == -1 and _map[i + 1, j] - _map[i, j] <= 1:
                        map_of_movements[i + 1, j] = k + 1
                    # RIGHT
                    if j < len(_map[0]) - 1 and map_of_movements[i, j + 1] == -1 and _map[i, j + 1] - _map[i, j] <= 1:
                        map_of_movements[i, j + 1] = k + 1

    _map = parsed_input.map

    map_of_movements = np.full((len(_map),len(_map[0])), -1)
    map_of_movements[parsed_input.start] = 0
    k = 0
    while map_of_movements[parsed_input.finish] == -1:
        make_step(k)
        k += 1

    return map_of_movements[parsed_input.finish]


def task2(parsed_input):

    def make_step(k):
        marked_points = 0
        for i in range(len(_map)):
            for j in range(len(_map[0])):
                if map_of_movements[i, j] == k:
                    # UP
                    if i > 0 and map_of_movements[i - 1, j] == -1 and _map[i - 1, j] - _map[i, j] <= 1:
                        map_of_movements[i - 1, j] = k + 1
                        marked_points += 1
                    # LEFT
                    if j > 0 and map_of_movements[i, j - 1] == -1 and _map[i, j - 1] - _map[i, j] <= 1:
                        map_of_movements[i, j - 1] = k + 1
                        marked_points += 1
                    # DOWN
                    if i < len(_map) - 1 and map_of_movements[i + 1, j] == -1 and _map[i + 1, j] - _map[i, j] <= 1:
                        map_of_movements[i + 1, j] = k + 1
                        marked_points += 1
                    # RIGHT
                    if j < len(_map[0]) - 1 and map_of_movements[i, j + 1] == -1 and _map[i, j + 1] - _map[i, j] <= 1:
                        map_of_movements[i, j + 1] = k + 1
                        marked_points += 1
        return marked_points > 0

    _map = parsed_input.map
    starting_points = (np.where(_map == 0))

    steps_to_finish = []
    for start in zip(starting_points[0], starting_points[1]):
        map_of_movements = np.full((len(_map),len(_map[0])), -1)
        map_of_movements[start] = 0
        k = 0
        while map_of_movements[parsed_input.finish] == -1:
            if not make_step(k):
                break
            k += 1
        if map_of_movements[parsed_input.finish] > 0:
            steps_to_finish.append(map_of_movements[parsed_input.finish])

    return min(steps_to_finish)


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().rstrip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
