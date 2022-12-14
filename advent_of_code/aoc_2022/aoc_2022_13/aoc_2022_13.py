from pathlib import Path
from collections import namedtuple

Pair = namedtuple("Pair", "first second")


def parse(raw_input):
    lines = raw_input.splitlines()
    pairs = [Pair(eval(lines[i]), eval(lines[i+1])) for i in range(0, len(lines), 3)]

    return pairs


def task1(parsed_input):

    def check_lists(l1, l2):
        is_valid = None
        while l1:
            first_el = l1.pop(0)
            try:
                second_el = l2.pop(0)
            except IndexError:
                is_valid = False
                return is_valid

            if type(first_el) == int and type(second_el) == int:
                if first_el < second_el:
                    is_valid = True
                    return is_valid
                elif first_el == second_el:
                    continue
                else:
                    is_valid = False
                    return is_valid

            elif isinstance(first_el, list) and isinstance(second_el, list):
                result = check_lists(first_el, second_el)
                if result is None:
                    continue
                return result

            else:
                if type(first_el) == int:
                    result = check_lists([first_el], second_el)
                else:
                    result = check_lists(first_el, [second_el])
                if result is None:
                    continue
                return result
        if len(l2) > 0:
            is_valid = True
            return is_valid

    valid_pair_indexes = []
    for i, pair in enumerate(parsed_input):
        res = check_lists(pair.first, pair.second)
        if res is None or res:
            valid_pair_indexes.append(i + 1)

    return sum(valid_pair_indexes)

def task2(parsed_input):
    return parsed_input


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().rstrip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
