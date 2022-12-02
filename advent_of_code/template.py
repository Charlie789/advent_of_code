from pathlib import Path


def parse(raw_input):
    pass


def task1(parsed_input):
    pass


def task2(parsed_input):
    pass


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
