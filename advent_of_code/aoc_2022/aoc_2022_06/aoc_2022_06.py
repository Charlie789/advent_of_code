from pathlib import Path


def parse(raw_input):
    parsed_input = raw_input[0]
    return parsed_input


def _check_window(window_size, parsed_input):
    for i in range(len(parsed_input) - window_size):
        window = set(parsed_input[i:i+window_size])
        if len(window) == window_size:
            return i + window_size


def task1(parsed_input):
    return _check_window(4, parsed_input)


def task2(parsed_input):
    return _check_window(14, parsed_input)


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.readlines()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
