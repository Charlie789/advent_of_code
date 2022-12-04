from pathlib import Path

def parse(raw_input):
    parsed_input = []
    for line in raw_input.splitlines():
        elf_ranges = []
        for elf in line.split(","):
            elf_range = elf.split("-")
            elf_ranges.append(range(int(elf_range[0]), int(elf_range[-1]) + 1))
        parsed_input.append(elf_ranges)

    return parsed_input


def task1(parsed_input):
    fully_contain_couter = 0
    for i, elf_pair in enumerate(parsed_input):
        elf1 = set(elf_pair[0])
        intersection = list(elf1.intersection(elf_pair[1]))
        if not len(intersection):
            continue
        intersection_range = range(min(intersection), max(intersection) + 1)
        if intersection_range in elf_pair:
            fully_contain_couter += 1
    return fully_contain_couter


def task2(parsed_input):
    overlap_couter = 0
    for i, elf_pair in enumerate(parsed_input):
        elf1 = set(elf_pair[0])
        intersection = elf1.intersection(elf_pair[1])
        if len(intersection):
            overlap_couter += 1
    return overlap_couter


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().strip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
