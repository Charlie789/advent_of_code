from pathlib import Path


def parse(raw_input):
    parsed_input = raw_input.split("\n\n")
    return parsed_input


def task1(parsed_input):
    sum_list = []
    splitted_input = [x.splitlines() for x in parsed_input]
    for sublist in splitted_input:
        sum_list.append(sum([int(x) for x in sublist]))
    return max(sum_list)


def task2(parsed_input):
    sum_list = []
    splitted_input = [x.splitlines() for x in parsed_input]
    for sublist in splitted_input:
        sum_list.append(sum([int(x) for x in sublist]))
    return sum(sorted(sum_list)[-3:])


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().strip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
