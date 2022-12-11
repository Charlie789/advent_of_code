import math
from pathlib import Path
from collections import namedtuple
from itertools import groupby
from copy import deepcopy


Monkey = namedtuple("Monkey", "items operation divisible_by true_monkey false_monkey")


def parse(raw_input):
    def operation_factory(arg1, separator, arg2):
        if separator == "+":
            if arg2 == "old":
                return lambda x: x + x
            else:
                return lambda x: x + int(arg2)
        else:
            if arg2 == "old":
                return lambda x: x * x
            else:
                return lambda x: x * int(arg2)

    monkeys = []
    _input = [list(g) for k, g in groupby(raw_input.splitlines(), key=bool) if k]
    for line in _input:
        starting_items = list(map(int, [*line[1].split(":")[-1].split(",")]))
        operation = operation_factory(*line[2].split("= ")[-1].split(" "))
        divisible_by = int(line[3].split(" ")[-1])
        true_monkey = int(line[4].split(" ")[-1])
        false_monkey = int(line[5].split(" ")[-1])

        monkey = Monkey(
            starting_items,
            operation,
            divisible_by,
            true_monkey,
            false_monkey
        )
        monkeys.append(monkey)


    return monkeys


def task1(monkeys):
    inspections = [0] * len(monkeys)
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            for item in monkey.items:
                inspections[i] += 1
                worry_level = monkey.operation(item) // 3
                if worry_level % monkey.divisible_by == 0:
                    monkeys[monkey.true_monkey].items.append(worry_level)
                else:
                    monkeys[monkey.false_monkey].items.append(worry_level)
            monkey.items.clear()

    return math.prod(sorted(inspections)[-2:])


def task2(monkeys):
    inspections = [0] * len(monkeys)
    lcm = math.lcm(*[monkey.divisible_by for monkey in monkeys])
    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            for item in monkey.items:
                inspections[i] += 1
                worry_level = monkey.operation(item)
                worry_level %= lcm
                if worry_level % monkey.divisible_by == 0:
                    monkeys[monkey.true_monkey].items.append(worry_level)
                else:
                    monkeys[monkey.false_monkey].items.append(worry_level)
            monkey.items.clear()

    return math.prod(sorted(inspections)[-2:])


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().rstrip()
    parsed_data = parse(data)
    solution1 = task1(deepcopy(parsed_data))
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
