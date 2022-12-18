from copy import deepcopy
from pathlib import Path
from collections import namedtuple

Position = namedtuple("Position", "x y")
Pair = namedtuple("Pair", "sensor beacon distance")

def find_in_radius(position: Position, radius: int, point_of_interest: int):
    positions = set()
    for i in range(-radius, radius + 1):
        pos_y = position.y + radius - abs(i)
        if pos_y == point_of_interest:
            positions = positions.union(set(range(position.x - i, position.x + i + 1)))
        pos_y = position.y - (radius - abs(i))
        if pos_y == point_of_interest:
            positions = positions.union(set(range(position.x - i, position.x + i + 1)))
    return positions


def parse(raw_input):
    pairs = []
    for line in raw_input.splitlines():
        sensor, beacon = line.split(":")
        sensor_x, sensor_y = sensor.split(",")
        sensor_position = Position(int(sensor_x.split("=")[-1]), int(sensor_y.split("=")[-1]))

        beacon_x, beacon_y = beacon.split(",")
        beacon_position = Position(int(beacon_x.split("=")[-1]), int(beacon_y.split("=")[-1]))

        pair = Pair(sensor_position, beacon_position, abs(beacon_position.x - sensor_position.x) + abs(beacon_position.y - sensor_position.y))
        pairs.append(pair)

    return pairs


def task1(parsed_input, row_of_interest):
    result = set()
    for i, pair in enumerate(parsed_input):
        result = result.union(find_in_radius(pair.sensor, pair.distance, row_of_interest))

    for pair in parsed_input:
        if pair.beacon.y == row_of_interest:
            try:
                result.remove(pair.beacon.x)
            except KeyError:
                continue
    return len(result)

def task2(parsed_input, max_size):

    return len(parsed_input)


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().rstrip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data, 2000000)
    solution2 = task2(parsed_data, 4000000)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
