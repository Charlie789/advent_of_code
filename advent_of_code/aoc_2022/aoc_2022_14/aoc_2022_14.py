import math
import numpy as np
from pathlib import Path
from enum import Enum


class TileContent(Enum):
    empty = "."
    rock = "#"
    sand = "o"


def parse(raw_input):
    rocks = []
    min_x = math.inf
    max_x = -math.inf
    max_y = -math.inf
    for line in raw_input.splitlines():
        coords = []
        for coord in line.split(" -> "):
            x,y = coord.split(",")
            x = int(x)
            y = int(y)
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            coords.append([x, y])
        rocks.append(coords)

    normalized_starting_point = 500 - min_x
    normalized_max_x = max_x - min_x

    cave_map = np.chararray((max_y + 1, normalized_max_x + 1))
    cave_map[:] = TileContent.empty.value

    for rock in rocks:
        last_coord = None
        for coord in rock:
            coord[0] -= min_x
            if last_coord:
                if last_coord[0] != coord[0]:
                    cave_map[coord[1], min(last_coord[0], coord[0]) : max(last_coord[0], coord[0]) + 1] = TileContent.rock.value
                elif last_coord[1] != coord[1]:
                    cave_map[min(last_coord[1], coord[1]) : max(last_coord[1], coord[1]) + 1, coord[0]] = TileContent.rock.value
            last_coord = coord

    # for line in cave_map:
    #     print(b"".join(line))

    return cave_map, normalized_starting_point


def parse2(raw_input):
    extend_by = 1000
    rocks = []
    min_x = math.inf
    max_x = -math.inf
    max_y = -math.inf
    for line in raw_input.splitlines():
        coords = []
        for coord in line.split(" -> "):
            x,y = coord.split(",")
            x = int(x)
            y = int(y)
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            coords.append([x, y])
        rocks.append(coords)

    normalized_starting_point = extend_by + 500 - min_x
    normalized_max_x = extend_by + max_x - min_x

    cave_map = np.chararray((max_y + 3, normalized_max_x + 1 + extend_by))
    cave_map[:] = TileContent.empty.value
    cave_map[-1,:] = TileContent.rock.value

    for rock in rocks:
        last_coord = None
        for coord in rock:
            coord[0] -= min_x
            coord[0] += extend_by
            if last_coord:
                if last_coord[0] != coord[0]:
                    cave_map[coord[1], min(last_coord[0], coord[0]) : max(last_coord[0], coord[0]) + 1] = TileContent.rock.value
                elif last_coord[1] != coord[1]:
                    cave_map[min(last_coord[1], coord[1]) : max(last_coord[1], coord[1]) + 1, coord[0]] = TileContent.rock.value
            last_coord = coord

    return cave_map, normalized_starting_point

def task1(parsed_input):

    def drop_sand():

        def simulate_drop(x, y):
            while True:
                if cave_map[y + 1, x] == bytes(TileContent.empty.value, "utf-8"):
                    y += 1
                else:
                    if cave_map[y + 1, x - 1] == bytes(TileContent.empty.value, "utf-8"):
                        simulate_drop(x - 1, y)
                    elif cave_map[y + 1, x + 1] == bytes(TileContent.empty.value, "utf-8"):
                        simulate_drop(x + 1, y)
                    else:
                        cave_map[y, x] = TileContent.sand.value
                    break

        x = starting_point
        y = 0
        simulate_drop(x, y)

    cave_map, starting_point = parsed_input

    sands = 0
    while True:
        try:
            drop_sand()
        except IndexError:
            break
        else:
            sands += 1

    return sands


def task2(parsed_input):

    def drop_sand():

        def simulate_drop(x, y):
            while True:
                if cave_map[y + 1, x] == bytes(TileContent.empty.value, "utf-8"):
                    y += 1
                else:
                    if x == 0:
                        raise ValueError
                    if cave_map[y, x] == bytes(TileContent.sand.value, "utf-8"):
                        raise IndexError
                    if cave_map[y + 1, x - 1] == bytes(TileContent.empty.value, "utf-8"):
                        simulate_drop(x - 1, y)
                    elif cave_map[y + 1, x + 1] == bytes(TileContent.empty.value, "utf-8"):
                        simulate_drop(x + 1, y)
                    else:
                        cave_map[y, x] = TileContent.sand.value
                    break

        x = starting_point
        y = 0
        simulate_drop(x, y)

    cave_map, starting_point = parsed_input

    sands = 0
    while True:
        try:
            drop_sand()
        except IndexError:
            break
        else:
            sands += 1

    return sands


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().rstrip()
    parsed_data = parse(data)
    parsed_data2 = parse2(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data2)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
