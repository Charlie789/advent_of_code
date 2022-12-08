import math
from pathlib import Path
import numpy as np


def parse(raw_input):
    map = []
    for line in raw_input.splitlines():
        map.append([int(char) for char in line])

    parsed_input = np.array(map)
    return parsed_input


def task1(parsed_input):
    def check_if_visible(x, y):
        to_skip = [0, len(parsed_input[0]) - 1]
        if x in to_skip or y in to_skip:
            return True
        # print("CHECK")
        checked_value = parsed_input[x,y]

        def check_left_rigth():
            # print(x, y, checked_value, parsed_input[x, :y])
            for value_to_compare in parsed_input[x, :y]:
                if checked_value <= value_to_compare:
                    return False
            return True

        def check_right_left():
            # print(x, y, checked_value, parsed_input[x, y+1:])
            for value_to_compare in parsed_input[x, y+1:]:
                if checked_value <= value_to_compare:
                    return False
            return True
        
        def check_top_bottom():
            # print(x, y, checked_value, parsed_input[:x, y])
            for value_to_compare in parsed_input[:x, y]:
                if checked_value <= value_to_compare:
                    return False
            return True

        def check_bottom_top():
            # print(x, y, checked_value, parsed_input[x+1:, y])
            for value_to_compare in parsed_input[x+1:, y]:
                if checked_value <= value_to_compare:
                    return False
            return True

        results = [check_right_left(), check_left_rigth(), check_top_bottom(), check_bottom_top()]
        # print(checked_value, results)
        return any(results)

    visible_trees = 0
    for x in range(len(parsed_input)):
        for y in range(len(parsed_input)):
            if check_if_visible(x, y):
                visible_trees += 1
    return visible_trees


def task2(parsed_input):
    def check_if_visible(x, y):
        to_skip = [0, len(parsed_input[0]) - 1]
        if x in to_skip or y in to_skip:
            return True
        # print("CHECK")
        checked_value = parsed_input[x, y]

        def check_left_rigth():
            # print(x, y, checked_value, np.flip(parsed_input[x, :y]))
            visible_trees = 0
            for value_to_compare in np.flip(parsed_input[x, :y]):
                visible_trees += 1
                if checked_value <= value_to_compare:
                    break
            return visible_trees

        def check_right_left():
            # print(x, y, checked_value, parsed_input[x, y+1:])
            visible_trees = 0
            for value_to_compare in parsed_input[x, y + 1:]:
                visible_trees += 1
                if checked_value <= value_to_compare:
                    break
            return visible_trees

        def check_top_bottom():
            # print(x, y, checked_value, np.flip(parsed_input[:x, y]))
            visible_trees = 0
            for value_to_compare in np.flip(parsed_input[:x, y]):
                visible_trees += 1
                if checked_value <= value_to_compare:
                    break
            return visible_trees

        def check_bottom_top():
            # print(x, y, checked_value, parsed_input[x+1:, y])
            visible_trees = 0
            for value_to_compare in parsed_input[x + 1:, y]:
                visible_trees += 1
                if checked_value <= value_to_compare:
                    break
            return visible_trees

        results = [check_right_left(), check_left_rigth(), check_top_bottom(), check_bottom_top()]
        # print(checked_value, results)
        return math.prod(results)

    visibilities = []
    for x in range(len(parsed_input)):
        for y in range(len(parsed_input)):
            visibilities.append(check_if_visible(x, y))
    return max(visibilities)


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().rstrip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
