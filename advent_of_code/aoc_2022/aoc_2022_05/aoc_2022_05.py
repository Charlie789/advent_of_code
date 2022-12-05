from pathlib import Path
from collections import namedtuple
from copy import deepcopy

Procedure = namedtuple("Procedure", "stacks instructions")
Intruction = namedtuple("Instruction", "quantity move_from move_to")


def parse(raw_input):
    stacks = {}
    instructions = []
    for line_id, line in enumerate(raw_input):
        if "[" in line:
            for stack_id, i in enumerate(range(1, len(line), 4)):
                try:
                    stacks[stack_id].append(line[i])
                except KeyError:
                    stacks[stack_id] = [line[i]]
        if "move" in line:
            _, quantity, _, move_from, _, move_to = line.split(" ")
            instruction = Intruction(int(quantity), int(move_from) - 1, int(move_to.rstrip()) - 1)
            instructions.append(instruction)

    for key in stacks:
        while True:
            try:
                stacks[key].remove(" ")
            except ValueError:
                break
        stacks[key].reverse()

    parsed_input = Procedure(stacks, instructions)
    return parsed_input




def task1(parsed_input):
    stacks = parsed_input.stacks
    for instruction in parsed_input.instructions:
        for i in range(instruction.quantity):
            element = stacks[instruction.move_from].pop()
            stacks[instruction.move_to].append(element)

    answer = "".join([stack[-1] for stack in stacks.values()])
    return answer


def task2(parsed_input):
    stacks = parsed_input.stacks
    for instruction in parsed_input.instructions:
        elements_to_move = []
        for i in range(instruction.quantity):
            element = stacks[instruction.move_from].pop()
            elements_to_move.append(element)
        elements_to_move.reverse()
        stacks[instruction.move_to].extend(elements_to_move)

    answer = "".join([stack[-1] for stack in stacks.values()])
    return answer


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.readlines()
    parsed_data = parse(data)
    solution1 = task1(deepcopy(parsed_data))
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
