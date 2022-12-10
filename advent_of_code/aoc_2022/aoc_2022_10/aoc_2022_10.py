from pathlib import Path


def parse(raw_input):
    operations = []
    for line in raw_input.splitlines():
        if "noop" in line:
            operations.append((1, 0))
        else:
            _, value = line.split(" ")
            operations.append((2, int(value)))

    return operations


def task1(parsed_input):
    cycles_to_check = list(range(20, 221, 40))
    cycle = 0
    X = 1
    signal_strength = 0
    for operation in parsed_input:
        cycle += operation[0]
        if not len(cycles_to_check):
            break
        if cycle >= cycles_to_check[0]:
            current_cycle = cycles_to_check.pop(0)
            signal_strength += current_cycle * X
        X += operation[1]

    return signal_strength


def task2(parsed_input):
    cycle = 0
    X = 1
    display = []
    current_line = ""
    for operation in parsed_input:
        for _cycle in range(operation[0]):
            if cycle == 40:
                cycle = 0
                display.append(current_line)
                current_line = ""
            current_line += "#" if cycle in range(X - 1, X + 2) else "."
            cycle += 1
        X += operation[1]
    for line in display:
        print(line)
    return display


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().rstrip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
