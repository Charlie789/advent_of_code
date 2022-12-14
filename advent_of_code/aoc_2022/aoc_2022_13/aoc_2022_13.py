import math
from copy import deepcopy
from pathlib import Path
from collections import namedtuple

Pair = namedtuple("Pair", "first second")

class Packet:
    def __init__(self, packet):
        self.packet = packet

    def __repr__(self):
        return str(self.packet)

    def check_lists(self, l1, l2):
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
                result = self.check_lists(first_el, second_el)
                if result is None:
                    continue
                return result

            else:
                if type(first_el) == int:
                    result = self.check_lists([first_el], second_el)
                else:
                    result = self.check_lists(first_el, [second_el])
                if result is None:
                    continue
                return result
        if len(l2) > 0:
            is_valid = True
            return is_valid

    def __gt__(self, other):
        res = self.check_lists(deepcopy(self.packet), deepcopy(other.packet))
        return res is None or res



def parse(raw_input):
    lines = raw_input.splitlines()
    pairs = [Pair(eval(lines[i]), eval(lines[i+1])) for i in range(0, len(lines), 3)]

    return pairs


def task1(parsed_input):
    valid_pair_indexes = []
    for i, pair in enumerate(parsed_input):
        if Packet(pair.first) > Packet(pair.second):
            valid_pair_indexes.append(i + 1)

    return sum(valid_pair_indexes)

def task2(parsed_input):
    divider_packets = [Packet([[2]]), Packet([[6]])]
    packets = []
    packets.extend(divider_packets)
    for pair in parsed_input:
        packets.append(Packet(pair.first))
        packets.append(Packet(pair.second))

    sorted_packets = sorted(packets, reverse=True)

    return math.prod([sorted_packets.index(divider_packets[0]) + 1, sorted_packets.index(divider_packets[1]) + 1])


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().rstrip()
    parsed_data = parse(data)
    solution1 = task1(deepcopy(parsed_data))
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
