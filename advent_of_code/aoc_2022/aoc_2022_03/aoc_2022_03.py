from pathlib import Path
from string import ascii_letters

def parse(raw_input):
    parsed_input = raw_input.splitlines()
    return parsed_input


def task1(parsed_input):
    parsed_input = map(lambda line: [line[:len(line) // 2], line[len(line) // 2:]], parsed_input)
    score = 0
    for backpack in parsed_input:
        compartment1 = set(backpack[0])
        compartment2 = set(backpack[1])
        for common in compartment1.intersection(compartment2):
            score += ascii_letters.find(common) + 1
    return score


def task2(parsed_input):
    score = 0
    for i in range(0, len(parsed_input), 3):
        backpack1 = set(parsed_input[i])
        backpack2 = set(parsed_input[i + 1])
        backpack3 = set(parsed_input[i + 2])

        badge = list(backpack1.intersection(backpack2).intersection(backpack3))[0]
        score += ascii_letters.find(badge) + 1
    return score


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().strip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
