from pathlib import Path
from collections import namedtuple

Elves = namedtuple("Elves", "elf1 elf2")

def parse(raw_input):
    parsed_input = []
    for line in raw_input.splitlines():
        elf_ranges = []
        for elf in line.split(","):
            elf_range = elf.split("-")
            elf_ranges.append(set(range(int(elf_range[0]), int(elf_range[-1]) + 1)))
        elves = Elves(elf_ranges[0], elf_ranges[1])
        parsed_input.append(elves)

    return parsed_input


def task1(parsed_input):
    fully_contain_couter = 0
    for elf_pair in parsed_input:
        if elf_pair.elf1.issuperset(elf_pair.elf2) or elf_pair.elf1.issubset(elf_pair.elf2):
            fully_contain_couter += 1
    return fully_contain_couter


def task2(parsed_input):
    overlap_counter = 0
    for elf_pair in parsed_input:
        is_disjoint = elf_pair.elf1.isdisjoint(elf_pair.elf2)
        if not is_disjoint:
            overlap_counter += 1
    return overlap_counter


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().strip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
