import math
from pathlib import Path


def count_distance(time_to_hold, max_time):
    return time_to_hold * (max_time - time_to_hold)


def parse(raw_input):
    return raw_input


def task1(parsed_input):
    times = parsed_input[0].split(":")[1].split()
    distances = parsed_input[1].split(":")[1].split()

    pairs = zip(map(int, times), map(int, distances))

    points = 1
    for pair in pairs:
        in_valid_range = False
        count = 0
        for i in range(1, pair[0]):
            distance = count_distance(i, pair[0])
            if distance > pair[1]:
                in_valid_range = True
                count += 1
            elif in_valid_range:
                break
        points *= count
    return points



def task2(parsed_input):
    time = int("".join(parsed_input[0].split(":")[1].split()))
    distance = int("".join(parsed_input[1].split(":")[1].split()))

    in_valid_range = False
    count = 0
    for i in range(1, math.ceil(time)):
        distance_ = count_distance(i, time)
        if distance_ > distance:
            in_valid_range = True
            count += 1
        elif in_valid_range:
            break
    return count


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.readlines()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
